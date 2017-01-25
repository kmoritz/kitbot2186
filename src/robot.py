#!/usr/bin/env python3

import wpilib
from magicbot.magicrobot import MagicRobot
from common import gearbox
from components import drive, climber
from robotpy_ext.common_drivers import navx, xl_max_sonar_ez
from wpilib.smartdashboard import SmartDashboard

class MyRobot(MagicRobot):
    
    drive = drive.Drive
    #vision = vision.Vision
    climber = climber.Climber
    
    def createObjects(self):
        self.left_side = gearbox.Gearbox([0, 1])
        self.right_side = gearbox.Gearbox([2, 3])
        
        self.climber_motor = wpilib.Spark(4)
        
        #self.navx = navx.AHRS.create_spi()
        
        self.controller = wpilib.Joystick(0)
        
        self.ultrasonic = xl_max_sonar_ez.MaxSonarEZAnalog(0)
        
    def teleopPeriodic(self):
        self.climber.set(self.controller.getRawAxis(1))
        #SmartDashboard.putNumber("heading", self.navx.getFusedHeading())
        
        """
        SmartDashboard.putNumber("On Target", self.vision.detects_hook)
        SmartDashboard.putNumber("Hook X", self.vision.hook_x)
        SmartDashboard.putNumber("Hook Y", self.vision.hook_y)
        """

if __name__ == "__main__":
    wpilib.run(MyRobot)

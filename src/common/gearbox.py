'''
Created on Dec 11, 2016

@author: Kenny
'''

import wpilib

class Gearbox:
        def __init__(self, ports):
            self.motors = []
            for port in ports:
                self.motors.append(wpilib.VictorSP(port))
                
        def set(self, value):
            for m in self.motors:
                m.set(value)
                
        def stopMotor(self):
            for m in self.motors:
                m.set(0)
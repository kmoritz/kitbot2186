'''
Created on Jan 14, 2017

@author: Kenny
'''
import wpilib
class Climber:
    '''
    classdocs
    '''
    
    climber_motor = wpilib.Spark
    
    def __init__(self):
        self.speed = 0
    
    def set(self, speed):
        self.speed = speed
        
    def execute(self):
        self.climber_motor.set(self.speed)
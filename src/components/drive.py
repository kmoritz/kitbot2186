'''
Created on Jan 4, 2017

@author: Kenny
'''

from common import gearbox
from robotpy_ext.common_drivers import navx

class Drive:
    '''
    classdocs
    '''
    left_side = gearbox.Gearbox
    right_side = gearbox.Gearbox
    navx = navx.AHRS
    
    left = 0
    right = 0
    
    def tankdrive(self, left, right):
        self.left = left
        self.right = right
        
    def drive(self, x, y):
        if y > 0.0:
            if x > 0.0:
                self.left = y - x
                self.right = max(y, x)
            else:
                self.left = max(y, -x)
                self.right = x + y
        else:
            if x > 0.0:
                self.left = -max(-y, x)
                self.right = y + x
            else:
                self.left = y - x
                self.right = -max(-y, -x)
                
    def execute(self):
        self.left_side.set(self.left)
        self.right_side.set(self.right)
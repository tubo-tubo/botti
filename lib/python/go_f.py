#!coding:utf-8
#import serial
#import math
import gpsnavi
class getdistance:

    def __init__(self):
        pass

    @property
    def goal(self):
        return self._goal

    @goal.setter
    def goal(self, value):
        self._goal = value

    
    @property
    def nowpos(self):
        return self._nowpos

    @nowpos.setter
    def nowpos(self, value):
        self._nowpos = value



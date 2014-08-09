#!coding:utf-8
#import serial
#import math

class getdistance:

    def __init__(self):
        self._goal = []
        pass

    @property
    def goal(self):
        return self._goal

    @goal.setter
    def goal(self, value):
        self._goal.extend(value)

    @property
    def nowpos(self):
        return self._nowpos

    @nowpos.setter
    def nowpos(self, value):
        self._nowpos = value

    @property
    def ratio(self):
        return self._ratio
    
    @ratio.setter
    def ratio(self, value):
        self._ratio = value
    


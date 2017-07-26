'''
Created on 26.07.2017

@author: mcbg
'''
class Stock(object):
    def __init__(self, name):
        self.name = name
        
    def getName(self):
        return self.name
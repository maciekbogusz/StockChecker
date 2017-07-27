'''
Created on 26.07.2017

@author: mcbg
'''
class Stock(object):
    def __init__(self, name):
        self.name = name
    
    def setPrice(self, price):
        self.price = price
            
    def getName(self):
        return self.name
    
    def getPrice(self):
        return self.price
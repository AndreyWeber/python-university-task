#-*- coding:utf-8 -*-
from general import general

class kindService(general):
    def __init__(self, code, name = '', typeservice = '', price = 0):
        general.__init__(self, code)
        self.setName(name)
        self.setType(typeservice)
        self.setPrice(price)
        
    def getName(self): return self.__name
    def getType(self): return self.__typeofservice
    def getPrice(self): return self.__price
    def setName(self, value): self.__name = value
    def setType(self, value): self.__typeofservice = value
    def setPrice(self, value): self.__price = int(value)
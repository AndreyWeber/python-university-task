#-*- coding:utf-8 -*-

from general import general
from kindService import kindService
from client import client

class service(general):
    def __init__(self, code=0, kindService = None, count = 1, client = None,dateReception = None,dateReturn = None):
        general.__init__(self, code)
        self.setClient(client)
        self.setKindService(kindService)
        self.setCount(count)
        self.setDateReception(dateReception)
        self.setDateReturn(dateReturn)
        self.calculate();
        
    def getKindService(self): return self.__kindService
    def getClient(self): return self.__client
    def getDateReception(self): return self.__dateReception
    def getDateReturn(self): return self.__dateReturn
    def getPrice(self):return self.__kindService.getPrice()
    def getCount(self): return self.__count
    def getSum(self):return self.__sum
    
    def setKindService(self, value): 
        if isinstance(value, kindService): self.__kindService = value
    def setClient(self, value): 
        if isinstance(value, client): self.__client = value
    def setDateReception(self, value): self.__dateReception = value
    def setDateReturn(self, value): self.__dateReturn = bool(value)
    def setCount(self,value):self.__count = value
    def setSum(self,value):self.__sum = value
    
    def calculate(self):
        discount = 0
        if self.__client.getRegular() == True: discount = 0.03
        self.__sum = self.__count * self.__kindService.getPrice()*(1-discount);
    def getDecription(self):
        s = ''
        s = '%s %s %s %s %s' %(self.getClient().getDecription(), self.getKindService().getName(), self.getPrice(), self.getCount(), self.getSum())
        return s
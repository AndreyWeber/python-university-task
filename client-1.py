#-*- coding:utf-8 -*-
from general import general

class client(general):
    def __init__(self, code, surname = '', name = '', secname=''):
        general.__init__(self, code)
        self.setName(name)
        self.setSurname(surname)
        self.setSecname(secname)
        self.setRegular(False)
        
    def getName(self): return self.__name
    def getSurname(self): return self.__surname
    def getSecname(self): return self.__secname
    def getRegular(self): return self.__regular
    def getDecription(self):
        return '%s %s %s' %(self.__surname, self.__name, self.__secname)
    
    def setName(self, value): self.__name = value
    def setSecname(self, value): self.__secname = value
    def setSurname(self, value): self.__surname = value
    def setRegular(self, value): self.__regular = bool(value)
    
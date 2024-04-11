#-*- coding:utf-8 -*-

from datetime import datetime
from generalList import generalList
from service import service

class serviseList(generalList):
    def __init__(self):
        generalList.__init__(self)
    def getCountClient(self, value):
        i = 0
        for l in self.getList():
            if l.getClient() == value: i = i+1
        return i
    def receptionItem(self,value):
        if isinstance(value, service): super().appendList(value)
        value.setDateReception(datetime.now())
        client = value.getClient()
        if client.getRegular != True:
            if self.getCountClient(client) >= 3:
                client.setRegular(True)
    def returnItem(self, value):
        if isinstance(value, service): value.setDateReturn(datetime.now())
# -*- coding:utf-8 -*-
from general import General


class generalList:
    def __init__(self):
        self.__list = []

    def clear(self):
        self.__list = []

    def findByCode(self, code):
        for l in self.__list:
            if l.getCode() == code:
                return l

    def getCodes(self):
        return [s.getCode() for s in self.__list]

    def appendList(self, value):
        self.__list.append(value)

    def removeList(self, code):
        for s in self.__list:
            if s.getCode() == code:
                self.__list.remove(s)

    def getList(self):
        return self.__list

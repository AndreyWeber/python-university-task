#-*- coding:utf-8 -*-
from datetime import datetime
from client import client
from kindService import kindService
from service import service
from serviceList import serviseList

serviseList1 = serviseList()
k1 = kindService(1,'Химчистка костюма' , 'Чистка текстильных изделий', 1000)
client1 = client(1,'Иванов', 'Иван', 'Иванович')

s1 = service(1,k1, 2, client1)
print (s1.getDecription())
serviseList1.receptionItem(s1)
serviseList1.returnItem(s1)

s2 = service(1,k1, 2, client1)
print (s2.getDecription())
serviseList1.receptionItem(s2)
serviseList1.returnItem(s2)

s3 = service(1,k1, 2, client1)
print (s3.getDecription())
serviseList1.receptionItem(s3)
serviseList1.returnItem(s3)

s4 = service(1,k1, 2, client1)
print (s4.getDecription())
serviseList1.receptionItem(s4)
serviseList1.returnItem(s4)
#-*- coding:utf-8 -*-
import datetime
import os,xml.dom.minidom

class client:
    def __init__(self,code=0,surname='',name='',secname='',regular = False ):
        self.setSurname(surname)
        self.setCode(code)
        self.setName(name)
        self.setSecname(secname)
        self.setRegular(regular)
    def setSurname(self,value):
        self.__surname=value
    def setName(self,value):
        self.__name=value
    def setSecname(self,value):
        self.__secname=value
    def setRegular(self,value):
        self.__regular= bool(value)
    def setCode(self,value):
        self.__code=value
    def getSurname(self):
        return self.__surname
    def getName(self):
        return self.__name
    def getSecname(self):
        return self.__secname
    def getRegular(self):
        return self.__regular
    def getCode(self):
        return self.__code
        
class service:
    def __init__(self,code=0,kindService = None, count = 0, client = None,dateReception = '',dateReturn = ''):
        self.setCode(code)
        self.setClient(client)
        self.setKindService(kindService)
        self.setCount(count)
        self.setDateReception(dateReception)
        self.setDateReturn(dateReturn)
    def setCode(self,value):
        self.__code=value
    def setKindService(self, value):
        if isinstance(value, kindService): #сохранено ли значение как определенный тип данных 
            self.__kindService = value 
    def setClient(self, value):
        if isinstance(value, client): 
            self.__client = value
    def setDateReception(self, value):
            self.__dateReception = value
    def setDateReturn(self, value):
            self.__dateReturn = value
    def setCount(self,value):
            self.__count = value
    def setSum(self,value): 
            self.__sum = value
    def getKindService(self):
            return self.__kindService
    def getClient(self):
            return self.__client
    def getDateReception(self):
            return self.__dateReception
    def getDateReturn(self):
            return self.__dateReturn
    def getPrice(self):
            return self.__kindService.getPrice() #цена это свойство вида услуги
    def getCount(self):
            return self.__count
    def getSum(self):
            return self.__sum
    def getCode(self):
            return self.__code
    def finalprice(self):
        s=self.getClient().getRegular()
        q=self.getKindService().getPrice()
        count=1
        if s==1:
            count=count-0.03
        q=q*count
        d1=self.getDateReception()
        d11=datetime.datetime.strptime(d1,'%d.%m.%Y')
        d2=self.getDateReturn()
        d22=datetime.datetime.strptime(d2,'%d.%m.%Y')
        result=(d22-d11).days*q
        return result
               
    def print(self):
        print('Client - ', self.getClient().getSurname(),' ',self.getClient().getName(),' ',self.getClient().getSecname(),'; ','KindService - ',self.getKindService().getTypeService(), 
        '; ', 'finalprice - ',self.finalprice())
        
class kindService: 
    def __init__(self, code, name = '', typeservice = '', price = 0):
        self.setCode(code)
        self.setName(name)
        self.setTypeService(typeservice)
        self.setPrice(price)
    def setCode(self, value):
        self.__code = value
    def setName(self, value):
        self.__name = value
    def setTypeService(self, value):
        self.__typeofservice = value
    def setPrice(self, value):
        self.__price = int(value)
    def getName(self):
        return self.__name
    def getTypeService(self):
        return self.__typeofservice
    def getPrice(self):
        return self.__price
    def getCode(self):
        return self.__code
    
               
class ClientList:
    def __init__(self):
        self.__list=[]
    def clear(self):
        self.__list=[]
    def findByCode(self,code):
        for l in self.__list:
            if l.getCode()==code:
                return l
    def getNewCode(self):
        return max(self.getCodes())+1
    def getCodes(self):
        return [s.getCode() for s in self.__list]
    def getItems(self):
        return self.__list
    def appendItem(self, value):
        if isinstance(value, client):
            self.__list.append(value)
    def removeItem(self, value):
        if isinstance(value, client):
            self.__list.remove(value)
        if isinstance(value, int):
            client = self.findByCode(value)
            if client:
                self.__list.remove(client)
    def createItem(self, code=0, surname="", name="", secname="", regular=0):
        if code in self.getCodes():
            print('Client with code %s already exists' % code)
        else:self.appendItem(client(code, surname, name, secname, regular))
    def newItem(self, surname="", name="", secname="", regular=0):
            self.appendItem(client(self.getNewCode(), surname, name, secname, regular))
                                 
class ServiceList:
    def __init__(self):
        self.__list = []
    def clear(self):
        self.__list = []
    def findByCode(self, code):
        for l in self.__list:
            if l.getCode() == code:
                return l
            return None
    def getNewCode(self):
        if len(self.__list) == 0:
            return 1
        return max(self.getCodes()) + 1
    def getCodes(self):
        return [s.getCode() for s in self.__list]
    def getItems(self):
        return self.__list
    def appendItem(self, value):
          if isinstance(value, service):
              self.__list.append(value)
    def removeItem(self, value):
          if isinstance(value, service):
              self.__list.remove(value)
              if isinstance(value, int):
                  service = self.findByCode(value)
                  if service:
                      self.__list.remove(service)
    def createItem(self, code=0, kindService=None, count=0, client=None, dateReception=None, dateReturn=None):
        if code in self.getCodes():
            print('Service with code %s already exists' % code)
        else:self.appendItem(service(code, kindService, count, client, dateReception, dateReturn))
    def newItem(self, kindService, count, client, dateReception, dateReturn):
            self.appendItem(service(self.getNewCode(), kindService, count, client, dateReception, dateReturn))
      
class KindServiceList:
    def __init__(self):self.__list=[]
    def clear(self):self.__list=[]
    def findByCode(self,code):
        for l in self.__list:
            if l.getCode()==code:
                return l
    def getNewCode(self):return max(self.getCodes())+1
    def getCodes(self):return [s.getCode() for s in self.__list]
    def getItems(self):return [s for s in self.__list]
    def removeItem(self,value):
        if isinstance(value,kindService):self.__list.remove(value)
        if isinstance(value,int):self.__list.remove(self.findByCode(value))
    def appendItem(self,value):
        if isinstance(value,kindService):self.__list.append(value)
    def createItem(self,code=0,name = '', typeservice = '', price = 0):
        if code in self.getCodes():print('KindService with code %s already exists')
        else:self.appendItem(kindService(code,name,typeservice,price))
    def newItem(self,name,typeservice,price):
        self.appendItem(kindService(self.getNewCode(),name,typeservice,price))

class Himchistka:
    def __init__(self):
       self.__clientlist=ClientList()
       self.__serviceList=ServiceList()
       self.__kindServiceList=KindServiceList()
    def clear(self):
       self.__clientlist.clear()
       self.__serviceList.clear()
       self.__kindServiceList.clear()
    def createClient(self,code=0,surname='',name='',secname='', regular =0):
       self.__clientlist.createItem(code,surname,name,secname,regular)
    def newClient(self,surname='',name='',secname='',regular =0):
       self.__clientlist.newItem(surname,name,secname,regular)
    def removeClient(self,value):
       self.__clientlist.removeItem(value)
    def getClient(self,code):return self.__clientlist.findByCode(code)
    def getClientList(self):return self.__clientlist.getItems()
    def getClientCodes(self):return self.__clientlist.getCodes()
    def createService(self,code=0,kindService = None, count = 0, client = None,dateReception = None,dateReturn = None):
       self.__serviceList.createItem(code,kindService,count,client,dateReception,dateReturn)
    def newService(self,code, kindService = None, count = 0, client = None,dateReception = None,dateReturn = None):
       self.__serviceList.newItem(code,kindService,count,client,dateReception,dateReturn)
    def removeService(self,code,kindService = None, count = 0, client = None, dateReception = None, dateReturn = None):
       self.__serviceList.removeItem(code)
       for b in self.__serviceList.getItems():
            b.setService(None)
    def getService(self,code):return self.__serviceList.findByCode(code)
    def getServiceList(self):return self.__serviceList.getItems()
    def getServiceCodes(self):return self.__serviceList.getCodes()
    def createKindService(self,code=0,name = '', typeservice = '', price = 0):
        self.__kindServiceList.createItem(code,name, typeservice,price)
    def newKindService(self,code=0,name = '', typeservice = '', price = 0):
        self.__kindServiceList.newItem(code,name, typeservice,price)
    def removeKindService(self,code):self.__kindServiceList.removeItem(code)
    def getKindService(self,code):return self.__kindServiceList.findByCode(code)
    def getKindServiceList(self):return self.__kindServiceList.getItems()
    def getKindServiceCodes(self):return self.__kindServiceList.getCodes()
 
class data:
    def __init__(self,ras=None,inp='',out=''):
        self.setRas(ras)
        self.setInp(inp)
        self.setOut(out)
    def setRas(self,value):self.__ras=value
    def setInp(self,value):self.__inp=value
    def setOut(self,value):self.__out=value
    def getRas(self):return self.__ras
    def getInp(self):return self.__inp
    def getOut(self):return self.__out
    def readFile(self,filename):
        self.setInp(filename)
        self.read()
    def writeFile(self,filename):
        self.setOut(filename)
        self.write()
    def read(self):pass
    def write(self):pass


class dataxml(data):
    def read(self):
        dom=xml.dom.minidom.parse(self.getInp())
        dom.normalize()
        for node in dom.childNodes[0].childNodes:
            if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName=="client"):
                code,surname,name,secname,regular=0,"","","",""
                for t in node.attributes.items():
                    if t[0]=="code":code=int(t[1])
                    if t[0]=="surname":surname=t[1]
                    if t[0]=="name":name=t[1]
                    if t[0]=="secname":secname=t[1]
                    if t[0]=="regular":regular=int(t[1])
                self.getRas().createClient(code,surname,name,secname,regular)
            if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName=="kindService"):
                code,name, typeservice, price =0,"","",0
                for t in node.attributes.items():
                    if t[0]=="code":code=int(t[1])
                    if t[0]=="name":name=t[1]
                    if t[0]=="typeservice":typeservice=t[1]
                    if t[0]=="price":price=t[1]
                self.getRas().createKindService(code,name,typeservice,price)                    
            if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName=="service"):
                code,count,dateReception,dateReturn = 0,0,"",""
                for t in node.attributes.items():
                    if t[0]=="code":code=int(t[1])
                    if t[0]=="count":count=int(t[1])
                    if t[0]=="dateReception":dateReception=t[1]
                    if t[0]=="dateReturn":dateReturn=t[1] 
                    if t[0]=="client":client=self.getRas().getClient(int(t[1]))
                    if t[0]=="kindService":kindService=self.getRas().getKindService(int(t[1]))
                self.getRas().createService(code,kindService,count,client,dateReception,dateReturn)
    def write(self):
        dom=xml.dom.minidom.Document()
        root=dom.createElement("himchistka")
        dom.appendChild(root)
        for a in self.getRas().getClientList():
            sot=dom.createElement("client")
            sot.setAttribute('code',str(a.getCode()))
            sot.setAttribute('surname',a.getSurname())
            sot.setAttribute('name',a.getName())
            sot.setAttribute('secname',a.getSecname())
            sot.setAttribute('regular',str(a.getRegular()))
            root.appendChild(sot)
        for p in self.getRas().getKindServiceList():
            wtp=dom.createElement("KindService")
            wtp.setAttribute('code',str(p.getCode()))
            wtp.setAttribute('name',p.getName())
            wtp.setAttribute('typeservice',p.getTypeService())
            wtp.setAttribute('price',str(p.getPrice()))
            root.appendChild(wtp)
        for b in self.getRas().getServiceList():
            wor=dom.createElement("Service")
            wor.setAttribute('code',str(b.getCode()))
            wor.setAttribute('kindService',str(b.getKindService().getCode()))
            wor.setAttribute('count',str(b.getCount()))
            wor.setAttribute('dateReception',str(b.getDateReception()))
            wor.setAttribute('dateReturn',str(b.getDateReturn()))
            wor.setAttribute('client',str(b.getClient().getCode()))
            root.appendChild(wor)
        f = open(self.getOut(),"w",encoding='utf-8')
        #f.write(dom.toprettyxml(encoding='utf-8'))
        f.write(dom.toprettyxml())                        


ras1=Himchistka()
dat1=dataxml(ras1,r'C:\python\source\repos\PythonApplication\oldfile.xml',r'C:\python\source\repos\PythonApplication\newfile.xml')
dat1.read()
dat1.write()

for k in ras1.getServiceList():
 
    k.print()
    print(' ')

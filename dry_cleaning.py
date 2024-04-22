from general import General
from service_type import ServiceType
from service_type_dict import ServiceTypeDict
from service import Service
from client import Client


class DryCleaning:
    def __init__(self):
        self.__service_types: ServiceTypeDict = ServiceTypeDict()
        self.__clients = {}
        self.__services = {}

    @property
    def service_types(self):
        return self.__service_types

    @property
    def clients(self):
        return self.__clients

    @property
    def services(self):
        return self.__services

    def add_service_type(self, service_type: ServiceType):
        self.service_types.add_item(service_type)

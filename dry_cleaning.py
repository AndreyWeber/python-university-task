from datetime import datetime
from service_type import ServiceType
from service import Service
from client import Client
from service_type_dict import ServiceTypeDict
from service_dict import ServiceDict
from client_dict import ClientDict


class DryCleaning:
    def __init__(self):
        self.__service_types: ServiceTypeDict = ServiceTypeDict()
        self.__clients: ClientDict = ClientDict()
        self.__services: ServiceDict = ServiceDict()

    @property
    def service_types(self):
        return self.__service_types

    @property
    def clients(self):
        return self.__clients

    @property
    def services(self):
        return self.__services

    def add_service_type(self, service_type: ServiceType) -> None:
        self.service_types.add_item(service_type)

    def make_client_regular(self, service: Service) -> None:
        if self.services.get_client_count(service.client) >= 3:
            service.client.is_regular = True

    def add_client(self, client: Client) -> None:
        self.clients.add_item(client)

    def add_service(self, service: Service) -> None:
        self.services.add_item(service)

    def start_service(self, service: Service) -> None:
        if not isinstance(service, Service):
            raise TypeError(
                f"Expected an item of type 'Service', but received '{type(service).__name__}'"
            )

        self.make_client_regular(service)
        service.start_service()
        self.add_service(service)

    def finalize_service(self, code: int) -> None:
        if not isinstance(code, int):
            raise TypeError(
                f"Expected code of type 'int', but received '{type(code).__name__}'"
            )

        service_to_finalize: Service = self.services.item_dict.get(code, None)
        if service_to_finalize is None:
            raise ValueError(f"Service with code: {code} is not registered")

        if not service_to_finalize.date_returned is None:
            raise ValueError(f"Service with code: {code} is already finalized")

        service_to_finalize.finalize_service()

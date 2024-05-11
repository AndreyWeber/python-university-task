from entities.service_type import ServiceType
from entities.service import Service
from entities.client import Client
from entities.service_type_dict import ServiceTypeDict
from entities.service_dict import ServiceDict
from entities.client_dict import ClientDict


class DryCleaning:
    def __init__(self):
        self._service_types: ServiceTypeDict = ServiceTypeDict()
        self._clients: ClientDict = ClientDict()
        self._services: ServiceDict = ServiceDict()

    @property
    def service_types(self):
        return self._service_types

    @property
    def clients(self):
        return self._clients

    @property
    def services(self):
        return self._services

    def add_service_type(self, service_type: ServiceType) -> None:
        self.service_types.add_item(service_type)

    def remove_service_type_by_code(self, code: int) -> None:
        self.service_types.remove_item_by_code(code)

    def add_client(self, client: Client) -> None:
        self.clients.add_item(client)

    def remove_client_by_code(self, code: int) -> None:
        self.clients.remove_item_by_code(code)

    def make_client_regular(self, service: Service) -> None:
        if self.services.get_client_count(service.client) >= 3:
            service.client.is_regular = True

    def add_service(self, service: Service) -> None:
        self.services.add_item(service)

    def remove_service_by_code(self, code: int) -> None:
        self.services.remove_item_by_code(code)

    def start_service(self, service: Service) -> None:
        self.make_client_regular(service)
        service.start_service()
        self.add_service(service)

    def finalize_service(self, code: int) -> None:
        service_to_finalize: Service = self.services.get(code, None)
        if service_to_finalize is None:
            raise ValueError(f"Service with code: {code} is not registered")

        if not service_to_finalize.date_returned is None:
            raise ValueError(f"Service with code: {code} is already finalized")

        service_to_finalize.finalize_service()

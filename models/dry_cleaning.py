from entities.service_type import ServiceType
from entities.service import Service
from entities.client import Client
from entities.service_type_dict import ServiceTypeDict
from entities.service_dict import ServiceDict
from entities.client_dict import ClientDict


class DryCleaning:

    regular_client_threshold: int = 3

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
        if service is None or service.client is None or service.client.code is None:
            raise ValueError(
                "service, service.client or service.client.code cannot be None"
            )

        if (
            self.services.get_client_count(service.client)
            >= self.regular_client_threshold
        ):
            service.client.is_regular = True

    def add_service(self, service: Service) -> None:
        self.services.add_item(service)

    def remove_service_by_code(self, code: int) -> None:
        self.services.remove_item_by_code(code)

    def start_service(self, code: int) -> None:
        service_to_start: Service = self.services.get(code, None)
        if service_to_start is None:
            raise ValueError(f"Service with code {code} doesn't exist")

        if not service_to_start.date_received is None:
            raise ValueError(f"Service with code {code} is already started")

        service_to_start.start_service()
        # At this point we know that the service is new, because it wasn't
        # in the started state by this moment, so we need to make sure
        # if its client should become a regular one
        self.make_client_regular(service_to_start)

    def finalize_service(self, code: int) -> None:
        service_to_finalize: Service = self.services.get(code, None)
        if service_to_finalize is None:
            raise ValueError(f"Service with code: {code} doesn't exist")

        if service_to_finalize.date_received is None:
            raise ValueError(
                f"Failed to finalize service with code {code}. It is not started"
            )

        if not service_to_finalize.date_returned is None:
            raise ValueError(
                f"Failed to finalize service with code {code}. It is already finalized"
            )

        service_to_finalize.finalize_service()

    def remove_service_type_from_services_by_code(self, code: int) -> None:
        for service in self.services.values():
            if not service.service_type is None and service.service_type.code == code:
                service.service_type = None

    def remove_client_from_services_by_code(self, code: int) -> None:
        for service in self.services.values():
            if not service.client is None and service.client.code == code:
                service.client = None

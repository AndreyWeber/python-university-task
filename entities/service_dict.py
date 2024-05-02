from entities.general import General
from entities.service import Service
from entities.client import Client
from entities.general_dict import GeneralDict


class ServiceDict(GeneralDict):
    def add_item(self, item: Service) -> None:
        if not isinstance(item, Service):
            raise TypeError(
                f"Expected an item of type 'Service', but received '{type(item).__name__}'"
            )
        return super().add_item(item)

    def remove_item(self, item: General) -> None:
        if not isinstance(item, Service):
            raise TypeError(
                f"Expected an item of type 'Service', but received '{type(item).__name__}'"
            )
        return super().remove_item(item)

    def get_client_count(self, client: Client) -> int:
        if not isinstance(client, Client):
            raise TypeError(
                f"Expected an item of type 'Client', but received '{type(client).__name__}'"
            )
        return sum(1 for service in self.item_dict if service.client == client)

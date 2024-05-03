from entities.client import Client
from entities.general_dict import GeneralDict


class ServiceDict(GeneralDict):
    def get_client_count(self, client: Client) -> int:
        if not isinstance(client, Client):
            raise TypeError(
                f"Expected an item of type 'Client', but received '{type(client).__name__}'"
            )
        return sum(1 for service in self if service.client == client)

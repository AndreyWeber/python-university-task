from entities.client import Client
from entities.general_dict import GeneralDict


class ClientDict(GeneralDict):
    def add_item(self, item: Client) -> None:
        if not isinstance(item, Client):
            raise TypeError(
                f"Expected an item of type 'Client', but received '{type(item).__name__}'"
            )
        return super().add_item(item)

    def remove_item(self, item: Client) -> None:
        if not isinstance(item, Client):
            raise TypeError(
                f"Expected an item of type 'Client', but received '{type(item).__name__}'"
            )
        return super().remove_item(item)

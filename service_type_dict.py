from service_type import ServiceType
from general_dict import GeneralDict


class ServiceTypeDict(GeneralDict):
    def add_item(self, item: ServiceType) -> None:
        super().add_item(item)

    def remove_item(self, item: ServiceType) -> None:
        super().remove_item(item)

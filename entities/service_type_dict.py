from entities.service_type import ServiceType
from entities.general_dict import GeneralDict


class ServiceTypeDict(GeneralDict):
    def add_item(self, item: ServiceType) -> None:
        if not isinstance(item, ServiceType):
            raise TypeError(
                f"Expected an item of type 'ServiceType', but received '{type(item).__name__}'"
            )
        super().add_item(item)

    def remove_item(self, item: ServiceType) -> None:
        if not isinstance(item, ServiceType):
            raise TypeError(
                f"Expected an item of type 'ServiceType', but received '{type(item).__name__}'"
            )
        super().remove_item(item)

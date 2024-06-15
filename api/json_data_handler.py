import os
import json
from datetime import datetime
from api.base_data_handler import BaseDataHandler
from entities.client import Client
from entities.service_type import ServiceType
from entities.service import Service


class JsonDataHandler(BaseDataHandler):

    def read(self) -> None:
        if not os.path.exists(self.input):
            raise FileNotFoundError(f"The file '{self.input}' doesn't exist.")

        with open(self.input, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Load Clients
        for client_data in data.get("clients", []):
            self.data_source.add_client(
                Client(
                    code=int(client_data["code"]),
                    name=client_data["name"],
                    surname=client_data["surname"],
                    second_name=client_data["second_name"],
                    is_regular=client_data["is_regular"],
                )
            )
        # Load ServiceTypes
        for service_type_data in data.get("service_types", []):
            self.data_source.add_service_type(
                ServiceType(
                    code=int(service_type_data["code"]),
                    name=service_type_data["name"],
                    type=service_type_data["type"],
                    price=int(service_type_data["price"]),
                )
            )
        # Load Services
        for service_data in data.get("services", []):
            self.data_source.add_service(
                Service(
                    code=int(service_data["code"]),
                    service_type=self.data_source.service_types.get(
                        int(service_data["service_type"]), None
                    ),
                    client=self.data_source.clients.get(
                        int(service_data["client"]), None
                    ),
                    items_count=int(service_data["items_count"]),
                    date_received=datetime.strptime(
                        service_data["date_received"], self.date_format
                    ),
                    date_returned=datetime.strptime(
                        service_data["date_returned"], self.date_format
                    ),
                )
            )

    def write(self) -> None:
        data = {
            "clients": [],
            "service_types": [],
            "services": [],
        }

        # Populate the JSON with Client data
        for client in self.data_source.clients.values():
            data["clients"].append(
                {
                    "code": client.code,
                    "name": client.name,
                    "surname": client.surname,
                    "second_name": client.second_name,
                    "is_regular": client.is_regular,
                }
            )
        # Populate the JSON with ServiceType data
        for service_type in self.data_source.service_types.values():
            data["service_types"].append(
                {
                    "code": service_type.code,
                    "name": service_type.name,
                    "type": service_type.type,
                    "price": service_type.price,
                }
            )
        # Populate the JSON with Service data
        for service in self.data_source.services.values():
            data["services"].append(
                {
                    "code": service.code,
                    "service_type": service.service_type.code,
                    "client": service.client.code,
                    "items_count": service.items_count,
                    "date_received": service.date_received.strftime(self.date_format),
                    "date_returned": service.date_returned.strftime(self.date_format),
                }
            )

        with open(self.output, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

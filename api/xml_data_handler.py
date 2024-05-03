import os
from datetime import datetime
from lxml import etree
from api.base_data_handler import BaseDataHandler
from entities.client import Client
from entities.service_type import ServiceType
from entities.service import Service


class XmlDataHandler(BaseDataHandler):
    DATE_FORMAT = "%d.%m.%Y"

    def read(self) -> None:
        if not os.path.exists(self.input):
            raise FileNotFoundError(f"The file '{self.input}' doesn't exist.")

        with open(self.input, "rb") as file:
            tree = etree.parse(file)
            root = tree.getroot()
            # Load Clients
            for client_element in root.findall("client"):
                self.data_source.add_client(
                    Client(
                        code=int(client_element.get("code")),
                        name=client_element.get("name"),
                        surname=client_element.get("surname"),
                        second_name=client_element.get("secondName"),
                        is_regular=self.str_to_bool(client_element.get("isRegular")),
                    )
                )
            # Load ServiceTypes
            for service_type_element in root.findall("serviceType"):
                self.data_source.add_service_type(
                    ServiceType(
                        code=int(service_type_element.get("code")),
                        name=service_type_element.get("name"),
                        type=service_type_element.get("type"),
                        price=int(service_type_element.get("price")),
                    )
                )
            # Load Services
            for service_element in root.findall("service"):
                self.data_source.add_service(
                    Service(
                        code=int(service_element.get("code")),
                        service_type=self.data_source.service_types.get(
                            int(service_element.get("serviceType")), None
                        ),
                        client=self.data_source.clients.get(
                            int(service_element.get("client")), None
                        ),
                        items_count=int(service_element.get("itemsCount")),
                        date_received=datetime.strptime(
                            service_element.get("dateReceived"), self.DATE_FORMAT
                        ),
                        date_returned=datetime.strptime(
                            service_element.get("dateReturned"), self.DATE_FORMAT
                        ),
                    )
                )

    def write(self) -> None:
        # Create the root element
        root = etree.Element("dryCleaning")

        # Populate the XML with Client data
        for client in self.data_source.clients.values():
            client_element = etree.SubElement(root, "client")
            client_element.set("code", str(client.code))
            client_element.set("name", client.name)
            client_element.set("surname", client.surname)
            client_element.set("secondName", client.second_name)
            client_element.set("isRegular", str(client.is_regular))
        # Populate the XML with ServiceType data
        for service_type in self.data_source.service_types.values():
            service_type_element = etree.SubElement(root, "serviceType")
            service_type_element.set("code", str(service_type.code))
            service_type_element.set("name", service_type.name)
            service_type_element.set("type", service_type.type)
            service_type_element.set("price", str(service_type.price))
        # Populate the XML with Service data
        for service in self.data_source.services.values():
            service_element = etree.SubElement(root, "service")
            service_element.set("code", str(service.code))
            service_element.set("serviceType", str(service.service_type.code))
            service_element.set("client", str(service.client.code))
            service_element.set("itemsCount", str(service.items_count))
            service_element.set(
                "dateReceived", service.date_received.strftime(self.DATE_FORMAT)
            )
            service_element.set(
                "dateReturned", service.date_returned.strftime(self.DATE_FORMAT)
            )

        tree = etree.ElementTree(root)
        with open(self.output, "wb") as file:
            tree.write(file, pretty_print=True, xml_declaration=True, encoding="UTF-8")

import sqlite3
from sqlite3 import Cursor
from contextlib import contextmanager
from typing import Generator, Any
from datetime import datetime
from api.base_data_handler import BaseDataHandler
from entities.client import Client
from entities.service_type import ServiceType
from entities.service import Service


class SqliteDataHandler(BaseDataHandler):

    create_emptydb = """
        PRAGMA foreign_keys = ON;
        DROP TABLE IF EXISTS service;
        DROP TABLE IF EXISTS service_type;
        DROP TABLE IF EXISTS client;
        CREATE TABLE client (
            code INTEGER PRIMARY KEY,
            name TEXT,
            surname TEXT,
            second_name TEXT,
            is_regular INTEGER
        );
        CREATE TABLE service_type (
            code INTEGER PRIMARY KEY,
            name TEXT,
            [type] TEXT,
            price INTEGER
        );
        CREATE TABLE service (
            code INTEGER PRIMARY KEY,
            service_type INTEGER REFERENCES service_type(code)
                ON UPDATE CASCADE
                ON DELETE SET NULL,
            client INTEGER REFERENCES client(code)
                ON UPDATE CASCADE
                ON DELETE SET NULL,
            items_count INTEGER,
            date_received TEXT,
            date_returned TEXT
        );
    """

    def read(self) -> None:
        with self.open_db(self.input) as cursor:
            # Fetch clients
            cursor.execute(
                """
                SELECT
                    code,
                    name,
                    surname,
                    second_name,
                    is_regular
                FROM client
                """
            )
            for client_data in cursor.fetchall():
                self.data_source.add_client(
                    Client(
                        code=int(client_data[0]),
                        name=client_data[1],
                        surname=client_data[2],
                        second_name=client_data[3],
                        is_regular=client_data[4],
                    )
                )

            # Fetch service_types
            cursor.execute(
                """
                SELECT
                    code,
                    name,
                    [type],
                    price
                FROM service_type
                """
            )
            for service_type_data in cursor.fetchall():
                self.data_source.add_service_type(
                    ServiceType(
                        code=int(service_type_data[0]),
                        name=service_type_data[1],
                        type=service_type_data[2],
                        price=int(service_type_data[3]),
                    )
                )

            # Fetch services
            cursor.execute(
                """
                SELECT
                    code,
                    service_type,
                    client,
                    items_count,
                    date_received,
                    date_returned
                FROM service
                """
            )
            for service_data in cursor.fetchall():
                self.data_source.add_service(
                    Service(
                        code=int(service_data[0]),
                        service_type=self.data_source.service_types.get(
                            int(service_data[1]), None
                        ),
                        client=self.data_source.clients.get(int(service_data[2]), None),
                        items_count=int(service_data[3]),
                        date_received=datetime.strptime(
                            service_data[4], self.date_format
                        ),
                        date_returned=datetime.strptime(
                            service_data[5], self.date_format
                        ),
                    )
                )

    def write(self) -> None:
        with self.open_db(self.output, with_commit=True) as cursor:
            # Create DB schema
            cursor.executescript(self.create_emptydb)
            # Fill clients
            clients_data = [
                (
                    client.code,
                    client.name,
                    client.surname,
                    client.second_name,
                    client.is_regular,
                )
                for client in self.data_source.clients.values()
            ]
            cursor.executemany(
                """
                INSERT INTO client (
                    code,
                    name,
                    surname,
                    second_name,
                    is_regular
                ) VALUES (?, ?, ?, ?, ?)
                """,
                clients_data,
            )
            # Fill service_types
            service_types_data = [
                (
                    service_type.code,
                    service_type.name,
                    service_type.type,
                    service_type.price,
                )
                for service_type in self.data_source.service_types.values()
            ]
            cursor.executemany(
                """
                INSERT INTO service_type (
                    code,
                    name,
                    [type],
                    price
                ) VALUES (?, ?, ?, ?)
                """,
                service_types_data,
            )
            # Fill services
            services_data = [
                (
                    service.code,
                    service.service_type.code,
                    service.client.code,
                    service.items_count,
                    service.date_received.strftime(self.date_format),
                    service.date_received.strftime(self.date_format),
                )
                for service in self.data_source.services.values()
            ]
            cursor.executemany(
                """
                INSERT INTO service (
                    code,
                    service_type,
                    client,
                    items_count,
                    date_received,
                    date_returned
                ) VALUES (?, ?, ?, ?, ?, ?)
                """,
                services_data,
            )

    @contextmanager
    def open_db(
        self, name: str, with_commit: bool = False
    ) -> Generator[Cursor, Any, None]:
        try:
            conn = sqlite3.connect(name)
            cursor = conn.cursor()
            yield cursor
        finally:
            if with_commit:
                conn.commit()
            conn.close()

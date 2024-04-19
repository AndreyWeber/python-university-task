# -*- coding:utf-8 -*-
from dataclasses import dataclass
from datetime import date
from general import General
from serviceKind import ServiceKind
from client import Client


@dataclass(slots=True)
class Service(General):
    """Class representing Dry Cleaning service"""

    client: Client = None
    service_kind: ServiceKind = None
    count: int = 1
    reception_date: date = None
    return_date: date = None

    @property
    def price(self):
        """Service price"""
        return (
            self.service_kind.price if self.service_kind else ServiceKind.default_price
        )

    @property
    def sum(self):
        """Service orders sum with discount applied"""
        if self.client is None or self.service_kind is None:
            return 0
        discount = 0.03 if self.client.is_regular else 0
        return self.count * self.price * (1 - discount)

    @property
    def description(self):
        """Service instance string description"""
        return (
            f"{self.client.description} "
            f"{self.service_kind.name} "
            f"{self.price} {self.count} {self.sum}"
        )

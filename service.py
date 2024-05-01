# -*- coding:utf-8 -*-
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from general import General
from service_type import ServiceType
from client import Client


@dataclass(slots=True)
class Service(General):
    """Class representing Dry Cleaning service"""

    discount_factor: float = 0.97

    service_type: Optional[ServiceType] = None
    items_count: int = 0
    client: Optional[Client] = None
    date_received: Optional[datetime] = None
    date_returned: Optional[datetime] = None

    def calculate_cost(self) -> float:
        if self.client is None or self.service_type is None:
            raise ValueError(
                "Both 'client' and 'service_type' must be set to calculate the service cost."
            )
        total_cost = self.service_type.price * self.items_count
        return (
            total_cost * self.discount_factor if self.client.is_regular else total_cost
        )

    def start_service(self) -> None:
        self.date_received = datetime.now()

    def finalize_service(self) -> None:
        self.date_returned = datetime.now()

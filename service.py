# -*- coding:utf-8 -*-
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from general import General
from service_type import ServiceType
from client import Client


@dataclass(slots=True)
class Service(General):
    """Class representing Dry Cleaning service"""

    discount_factor: float = field(default=0.97, init=False, repr=False)

    service_type: Optional[ServiceType] = None
    client: Optional[Client] = None
    date_received: Optional[datetime] = None
    date_returned: Optional[datetime] = None

    def calculate_cost(self):
        if self.client is None or self.service_type is None:
            raise ValueError(
                "Both 'client' and 'service_type' must be set to calculate the service cost."
            )
        return (
            self.service_type.price * Service.discount_factor
            if self.client.is_regular
            else self.service_type.price
        )

    def finalize_service(self):
        self.date_returned = datetime.now()

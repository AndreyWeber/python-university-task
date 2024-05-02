# -*- coding:utf-8 -*-
from dataclasses import dataclass, field
from entities.general import General


@dataclass(slots=True)
class ServiceType(General):
    """Class representing Dry Cleaning service type"""

    # Class attribute - default price value equal to 0
    default_price: int = field(default=0, init=False, repr=False)

    name: str = ""
    type: str = ""
    price: int = field(default_factory=lambda: ServiceType.default_price)

    def __str__(self) -> str:
        return f"{self.type}: {self.name}"

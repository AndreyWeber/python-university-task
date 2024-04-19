# -*- coding:utf-8 -*-
from dataclasses import dataclass, field
from general import General


@dataclass(slots=True)
class ServiceKind(General):
    """Class representing Dry Cleaning service type"""

    # Class attribute - default price value equal to 0
    default_price: int = field(default=0, init=False, repr=False)

    name: str = ""
    service_type: str = ""
    price: int = field(default_factory=lambda: ServiceKind.default_price)

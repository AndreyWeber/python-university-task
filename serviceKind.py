# -*- coding:utf-8 -*-
from dataclasses import dataclass
from general import General


@dataclass(slots=True)
class ServiceKind(General):
    """Class representing Dry Cleaning service type"""

    name: str = ""
    service_type: str = ""
    price: int = 0

# -*- coding:utf-8 -*-
from dataclasses import dataclass
from general import General


@dataclass(slots=True)
class Client(General):
    """Class representing Dry Cleaning service client"""

    name: str = ""
    surname: str = ""
    second_name: str = ""
    is_regular: bool = False

    @property
    def description(self):
        """Client instance string description"""
        return f"{self.surname} {self.name} {self.second_name}"

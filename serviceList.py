# -*- coding:utf-8 -*-

from datetime import datetime
from generalList import GeneralList
from service import Service


class ServiseList(GeneralList):
    # __init__(self) doesn't required
    # because it doesn't do anything

    def get_client_count(self, value):
        return sum(1 for service in self.list if service.client == value)

    def submit_item(self, value):
        if not isinstance(value, Service):
            raise TypeError("submit_item only accepts Service type")

        value.submission_date = datetime.now()

        if value.client.is_regular:
            return
        if self.get_client_count(value.client) >= 3:
            value.client.is_regular = True

        super().append(value)

    def return_item(self, value):
        if not isinstance(value, Service):
            raise TypeError("return_item only accepts Service type")
        value.return_date = datetime.now()

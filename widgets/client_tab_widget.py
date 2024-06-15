from widgets.base_tab_widget import BaseTabWidget
from widgets.client_table_widget import ClientTableWidget
from widgets.client_edit_form_widget import ClientEditFormWidget
from entities.client_dict import ClientDict
from entities.client import Client


class ClientTabWidget(BaseTabWidget):
    def initUI(self):
        self.table_widget = ClientTableWidget(self._parent_window)
        self.edit_form_widget = ClientEditFormWidget()

        super().initUI()

    def populate_table(self, items: ClientDict) -> None:
        return super().populate_table(items)

    def populate_edit_controls(self, item: Client, **kwargs) -> None:
        return super().populate_edit_controls(item, **kwargs)

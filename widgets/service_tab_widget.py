from widgets.base_tab_widget import BaseTabWidget
from widgets.service_table_widget import ServiceTableWidget
from widgets.service_edit_form_widget import ServiceEditFormWidget
from entities.service_dict import ServiceDict
from entities.service import Service


class ServiceTabWidget(BaseTabWidget):
    def initUI(self):
        self.table_widget = ServiceTableWidget()
        self.edit_form_widget = ServiceEditFormWidget()

        super().initUI()

    def populate_table(self, items: ServiceDict) -> None:
        super().populate_table(items)

    def populate_edit_controls(self, item: Service, **kwargs) -> None:
        super().populate_edit_controls(item, **kwargs)

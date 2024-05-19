from widgets.base_tab_widget import BaseTabWidget
from widgets.service_type_table_widget import ServiceTypeTableWidget
from widgets.service_type_edit_form_widget import ServiceTypeEditFormWidget
from entities.service_type_dict import ServiceTypeDict
from entities.service_type import ServiceType


class ServiceTypeTabWidget(BaseTabWidget):
    def initUI(self):
        self.table_widget = ServiceTypeTableWidget()
        self.edit_form_widget = ServiceTypeEditFormWidget()

        super().initUI()

    def populate_table(self, items: ServiceTypeDict) -> None:
        super().populate_table(items)

    def populate_edit_controls(self, item: ServiceType, **kwargs) -> None:
        super().populate_edit_controls(item, **kwargs)

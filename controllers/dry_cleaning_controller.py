import logging
from pathlib import Path
from entities.general import General
from entities.general_dict import GeneralDict
from widgets.base_tab_widget import BaseTabWidget
from views.dry_cleaning_view import DryCleaningView
from models.dry_cleaning import DryCleaning
from api.base_data_handler import BaseDataHandler
from api.xml_data_handler import XmlDataHandler
from api.json_data_handler import JsonDataHandler
from api.sqlite_data_handler import SqliteDataHandler
from api.handler_type import HandlerType


class DryCleaningController:

    @property
    def active_tab_index(self) -> int:
        return self._view.active_tab_index

    @property
    def active_tab_widget(self) -> BaseTabWidget:
        return self._view.active_tab_widget

    def __init__(self, model: DryCleaning, view: DryCleaningView):
        self.logger = logging.getLogger(__name__)

        self._available_tabs = {}

        self._model: DryCleaning = model
        self._view: DryCleaningView = view
        self._data_handlers: dict[HandlerType, BaseDataHandler] = {
            HandlerType.XML: XmlDataHandler(
                self._model,
                str(Path(".\\oldfile.xml").resolve()),
                str(Path(".\\newfile.xml").resolve()),
            ),
            HandlerType.JSON: JsonDataHandler(
                self._model,
                str(Path(".\\oldfile.json").resolve()),
                str(Path(".\\newfile.json").resolve()),
            ),
            HandlerType.SQLITE: SqliteDataHandler(
                self._model,
                str(Path(".\\oldSqlite.db").resolve()),
                str(Path(".\\newSqlite.db").resolve()),
            ),
        }

        # Connect signals to slots

        # Top menu signals
        self._view.load_data_signal.connect(self.load_data)
        self._view.save_data_signal.connect(self.save_data)

        # Tabs and tab widgets signals
        self._view.tab_changed_signal.connect(self.on_tab_change)
        self.connect_tab_widget_signals()

        # Populate initial data
        self.populate_active_tab_table()
        self.pre_populate_active_tab_edit_controls(set_default_item_only=True)

    def on_tab_change(self) -> None:
        self.connect_tab_widget_signals()
        self.populate_active_tab_table()
        self.pre_populate_active_tab_edit_controls()

    def connect_tab_widget_signals(self) -> None:
        # Connect table widget signals to slots
        table_widget = self.active_tab_widget.table_widget
        edit_form_widget = self.active_tab_widget.edit_form_widget

        # Table widget signals
        self.disconnect_signal_gracefully(table_widget.table_cell_clicked_signal)
        self.disconnect_signal_gracefully(table_widget.table_row_header_clicked_signal)
        table_widget.table_cell_clicked_signal.connect(self.on_cell_clicked)
        table_widget.table_row_header_clicked_signal.connect(self.on_row_header_clicked)

        # Edit form signals
        self.disconnect_signal_gracefully(edit_form_widget.add_button_signal)
        self.disconnect_signal_gracefully(edit_form_widget.update_button_signal)
        self.disconnect_signal_gracefully(edit_form_widget.delete_button_signal)
        edit_form_widget.add_button_signal.connect(self.on_add_button_clicked)
        edit_form_widget.update_button_signal.connect(self.on_update_button_clicked)
        edit_form_widget.delete_button_signal.connect(self.on_delete_button_clicked)
        # Special case of Service tab
        if self.active_tab_index == 0:
            self.disconnect_signal_gracefully(edit_form_widget.receive_button_signal)
            self.disconnect_signal_gracefully(edit_form_widget.return_button_signal)
            edit_form_widget.receive_button_signal.connect(
                self.on_receive_button_clicked
            )
            edit_form_widget.return_button_signal.connect(self.on_return_button_clicked)

    def populate_active_tab_table(self) -> None:
        items: GeneralDict = {}
        match self.active_tab_index:
            case 0:
                items = self._model.services
            case 1:
                items = self._model.service_types
            case 2:
                items = self._model.clients
            case _:
                raise ValueError(f"Invalid active tab index: {self.active_tab_index}")

        # Populate table widget
        self.active_tab_widget.populate_table(items)

    def pre_populate_active_tab_edit_controls(
        self, set_default_item_only: bool = False
    ) -> None:
        if set_default_item_only:
            self.active_tab_widget.pre_populate_edit_controls()
        else:
            self.active_tab_widget.pre_populate_edit_controls(
                clients=self._model.clients,
                service_types=self._model.service_types,
            )

    def clear_active_tab_edit_controls(self) -> None:
        self.active_tab_widget.clear_edit_controls()

    def on_add_button_clicked(self, item: General) -> None:
        match self.active_tab_index:
            case 0:
                if item.code in self._model.services:
                    self.active_tab_widget.show_warning_message_signal.emit(
                        f"Can't add existing Service with code: '{item.code}'"
                    )
                item.client = self._model.clients[item.client.code]
                item.service_type = self._model.service_types[item.service_type.code]
                self._model.add_service(item)
            case 1:
                if item.code in self._model.service_types:
                    self.active_tab_widget.show_warning_message_signal.emit(
                        f"Can't add existing Service Type with code: '{item.code}'"
                    )
                    return
                self._model.add_service_type(item)
            case 2:
                if item.code in self._model.clients:
                    self.active_tab_widget.show_warning_message_signal.emit(
                        f"Can't add existing Client with code: '{item.code}'"
                    )
                    return
                self._model.add_client(item)
            case _:
                raise ValueError(f"Invalid active tab index: {self.active_tab_index}")

        self.populate_active_tab_table()
        self.clear_active_tab_edit_controls()

    def on_update_button_clicked(self, item: General) -> None:
        if item.code is None:
            raise ValueError("'item' argument cannot be None")

        match self.active_tab_index:
            case 0:
                if not item.code in self._model.services:
                    self.active_tab_widget.show_warning_message_signal.emit(
                        f"Update failed. Service with code: '{item.code}' doesn't exist"
                    )
                    return
                item.client = self._model.clients[item.client.code]
                item.service_type = self._model.service_types[item.service_type.code]
                self._model.services[item.code] = item
            case 1:
                if not item.code in self._model.service_types:
                    self.active_tab_widget.show_warning_message_signal.emit(
                        f"Update failed. Client with code: '{item.code}' doesn't exist"
                    )
                    return
                self._model.service_types[item.code] = item
            case 2:
                if not item.code in self._model.clients:
                    self.active_tab_widget.show_warning_message_signal.emit(
                        f"Update failed. Client with code: '{item.code}' doesn't exist"
                    )
                    return
                self._model.clients[item.code] = item
            case _:
                raise ValueError(f"Invalid active tab index: {self.active_tab_index}")

        self.populate_active_tab_table()

    def on_delete_button_clicked(self, code: int) -> None:
        match self.active_tab_index:
            case 0:
                self._model.remove_service_by_code(code)
            case 1:
                self._model.remove_service_type_by_code(code)
                self._model.remove_service_type_from_services_by_code(code)
            case 2:
                self._model.remove_client_by_code(code)
                self._model.remove_client_from_services_by_code(code)
            case _:
                raise ValueError(f"Invalid active tab index: {self.active_tab_index}")

        self.populate_active_tab_table()
        self.clear_active_tab_edit_controls()

    def on_receive_button_clicked(self, code: int) -> None:
        if self.active_tab_index != 0:
            raise ValueError(f"Invalid active tab index: {self.active_tab_index}")

        try:
            self._model.start_service(code)
        except ValueError:
            self.logger.error(
                "Items already received for the service with code %s", code
            )
        self.populate_active_tab_table()
        self.active_tab_widget.populate_edit_controls(self._model.services[code])
        self.active_tab_widget.set_enabled_edit_controls()

    def on_return_button_clicked(self, code: int) -> None:
        if self.active_tab_index != 0:
            raise ValueError(f"Invalid active tab index: {self.active_tab_index}")

        try:
            self._model.finalize_service(code)
        except ValueError:
            self.logger.error(
                "Items already returned for the service with code %s", code
            )
        self.populate_active_tab_table()
        self.active_tab_widget.populate_edit_controls(self._model.services[code])
        self.active_tab_widget.set_enabled_edit_controls()

    def on_cell_clicked(self, cell_index) -> None:
        row_index = cell_index.row()
        self.on_row_header_clicked(row_index)

    def on_row_header_clicked(self, row_index) -> None:
        code = self.active_tab_widget.get_table_widget_item_code_value(row_index)
        if code is None:
            raise ValueError(
                f"Failed to get entity code. row_index: {row_index}, "
                + f"active_tab_index: {self.active_tab_index}"
            )

        item: General = None
        match self.active_tab_index:
            case 0:
                item = self._model.services.get(code, None)
            case 1:
                item = self._model.service_types.get(code, None)
            case 2:
                item = self._model.clients.get(code, None)
            case _:
                raise ValueError(f"Invalid active tab index: {self.active_tab_index}")
        self.active_tab_widget.populate_edit_controls(item)
        self.active_tab_widget.set_enabled_edit_controls()

    def disconnect_signal_gracefully(self, signal) -> None:
        try:
            signal.disconnect()
        except TypeError:
            self.logger.info("No connection to disconnect for '%s'", signal)

    def adjust_columns_size(self):
        pass

    def adjust_window_size(self):
        pass

    #
    # Top menu action handlers
    #
    def load_data(self, handler_type: HandlerType) -> None:
        self._data_handlers[handler_type].read()
        self.populate_active_tab_table()
        self.pre_populate_active_tab_edit_controls()

    def save_data(self, handler_type: HandlerType) -> None:
        data_handler = self._data_handlers[handler_type]
        if not data_handler is None:
            data_handler.write()

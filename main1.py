import sys
from pathlib import Path

# pylint: disable=no-name-in-module
from PyQt5.QtWidgets import QApplication
from dry_cleaning import DryCleaning
from xml_data_handler import XmlDataHandler
from dry_cleaning_view import DryCleaningView
from dry_cleaning_controller import DryCleaningController


def main():
    # try:
    app = QApplication(sys.argv)

    model = DryCleaning()  # xml_data_handler.data_source
    view = DryCleaningView()

    controller = DryCleaningController(model, view)

    view.show()
    sys.exit(app.exec_())

    # except Exception as e:
    #     print(f"An error occurred: {e}")
    #     sys.exit()


if __name__ == "__main__":
    main()

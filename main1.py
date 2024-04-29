import sys
from pathlib import Path

# pylint: disable=no-name-in-module
from PyQt5.QtWidgets import QApplication
from dry_cleaning import DryCleaning
from xml_data_handler import XmlDataHandler
from dry_cleaning_view import DryCleaningView
from dry_cleaning_controller import DryCleaningController


def main():
    try:
        # xml_data_handler = XmlDataHandler(
        #     DryCleaning(),
        #     str(Path(".\\oldfile.xml").resolve()),
        #     str(Path(".\\newfile.xml").resolve()),
        # )
        # xml_data_handler.read()
        # xml_data_handler.write()

        app = QApplication(sys.argv)

        model = None
        view = DryCleaningView()
        DryCleaningController(model, view)

        view.show()
        sys.exit(app.exec_())

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit()


if __name__ == "__main__":
    main()

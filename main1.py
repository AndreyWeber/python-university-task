import sys
from pathlib import Path

# pylint: disable=no-name-in-module
from PyQt5.QtWidgets import QApplication
from dry_cleaning import DryCleaning
from xml_data_handler import XmlDataHandler
from main_window import MainWindow

try:
    xml_data_handler = XmlDataHandler(
        DryCleaning(),
        str(Path(".\\oldfile.xml").resolve()),
        str(Path(".\\newfile.xml").resolve()),
    )
    xml_data_handler.read()

    app = QApplication(sys.argv)
    main_window = MainWindow(xml_data_handler.data_source)
    main_window.show()
    sys.exit(app.exec_())
    # xml_data_handler.write()
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit()

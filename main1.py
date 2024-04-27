import sys
from pathlib import Path
from dry_cleaning import DryCleaning
from xml_data_handler import XmlDataHandler

try:
    xml_data_handler = XmlDataHandler(
        DryCleaning(),
        str(Path(".\\oldfile.xml").resolve()),
        str(Path(".\\newfile.xml").resolve()),
    )
    xml_data_handler.read()
    xml_data_handler.write()
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit()

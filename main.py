# import os
import sys
import logging

# pylint: disable=no-name-in-module
from PyQt5.QtWidgets import (
    QApplication,
    QMessageBox,
)
from models.dry_cleaning import DryCleaning
from views.dry_cleaning_view import DryCleaningView
from controllers.dry_cleaning_controller import DryCleaningController

# os.environ["QT_DEBUG_PLUGINS"] = "1"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(filename)s, line %(lineno)d - %(message)s",
)


def global_exception_hook(exctype, value, traceback):
    logging.error("Application error", exc_info=(exctype, value, traceback))
    QMessageBox.critical(
        None,
        "Application error",
        "Unexpected application error occurred: " + str(value),
    )
    sys.exit(1)


def main() -> None:
    sys.excepthook = global_exception_hook

    app = QApplication(sys.argv)

    model = DryCleaning()
    view = DryCleaningView()

    # pylint: disable=unused-variable
    controller = DryCleaningController(model, view)

    view.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

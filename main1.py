import sys
import logging

# pylint: disable=no-name-in-module
from PyQt5.QtWidgets import QApplication
from models.dry_cleaning import DryCleaning
from views.dry_cleaning_view import DryCleaningView
from controllers.dry_cleaning_controller import DryCleaningController

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    try:
        app = QApplication(sys.argv)

        model = DryCleaning()
        view = DryCleaningView()

        # pylint: disable=unused-variable
        controller = DryCleaningController(model, view)

        view.show()
        sys.exit(app.exec_())

    # pylint: disable=broad-exception-caught
    except Exception as e:
        logging.error("An error occurred: %s", e, exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()

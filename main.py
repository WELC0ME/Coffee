import sys

from PyQt5.QtWidgets import QApplication
from MainMenu import MainMenu
from Dialog import Dialog


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_menu = MainMenu()
    dialog = Dialog()

    main_menu.set_bond(dialog)
    dialog.set_bond(main_menu)

    main_menu.show()
    sys.exit(app.exec())

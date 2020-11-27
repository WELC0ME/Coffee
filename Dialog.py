import sqlite3

from PyQt5.QtWidgets import QMainWindow
from ui_addEditCoffeeForm import Ui_MainWindow

from config import DATABASE_PATH


class Dialog(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Add/Edit dialog')

        self.main_menu_bond = None
        self.btn_confirm.clicked.connect(self.confirm)

    def set_bond(self, obj):
        self.main_menu_bond = obj

    def confirm(self):
        try:
            connection = sqlite3.connect(DATABASE_PATH)
            cur = connection.cursor()

            assert self.le_sort.text() != ''
            assert self.le_grade.text() != ''
            assert self.le_tasty.text() != ''
            assert self.sb_price.value() != 0.0
            assert self.sb_volume.value() != 0.0

            cur.execute("DELETE FROM varieties WHERE id = ?", (self.lab_id.text(), ))
            cur.execute("""INSERT INTO varieties(id, sort, grade, state, tasty, price, volume) VALUES
            (?, ?, ?, ?, ?, ?, ?)""", (self.lab_id.text(), self.le_sort.text(), self.le_grade.text(),
                                       self.cb_state.currentIndex() + 1, self.le_tasty.text(),
                                       self.sb_price.value(), self.sb_volume.value()))

            connection.commit()
            connection.close()

            self.main_menu_bond.load_table()
            self.hide()
        except AssertionError:
            self.statusBar().showMessage('Error. Incorrect input')

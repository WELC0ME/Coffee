import sqlite3

from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from ui_main import Ui_MainWindow

from config import DATABASE_PATH


class MainMenu(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Coffee')

        self.dialog_bond = None
        self.btn_add.clicked.connect(self.add)
        self.btn_remove.clicked.connect(self.remove)
        self.tableWidget.cellDoubleClicked.connect(self.edit)

        self.length = 0
        self.load_table()

    def set_bond(self, obj):
        self.dialog_bond = obj

    def load_table(self):
        connection = sqlite3.connect(DATABASE_PATH)
        cur = connection.cursor()

        request = "SELECT varieties.id, varieties.sort, varieties.grade, states.state, varieties.tasty, "
        request += "varieties.price, varieties.volume "
        request += "FROM varieties JOIN states ON states.id = varieties.state"
        res = cur.execute(request).fetchall()

        connection.close()

        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels([i[0] for i in cur.description])
        self.tableWidget.setRowCount(0)

        for i, row in enumerate(res):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))

        if self.tableWidget.rowCount() == 0:
            self.length = 0
        else:
            self.length = int(self.tableWidget.item(self.tableWidget.rowCount() - 1, 0).text()) + 1

    def add(self):
        self.dialog_bond.lab_id.setText(str(self.length))
        self.dialog_bond.le_sort.setText('')
        self.dialog_bond.le_grade.setText('')
        self.dialog_bond.cb_state.setCurrentIndex(0)
        self.dialog_bond.le_tasty.setText('')
        self.dialog_bond.sb_price.setValue(0.0)
        self.dialog_bond.sb_volume.setValue(0.0)
        self.dialog_bond.statusBar().showMessage('')
        self.dialog_bond.show()

    def edit(self, row):
        trans = {'В зернах': 0, 'Молотый': 1}
        self.dialog_bond.lab_id.setText(self.tableWidget.item(row, 0).text())
        self.dialog_bond.le_sort.setText(self.tableWidget.item(row, 1).text())
        self.dialog_bond.le_grade.setText(self.tableWidget.item(row, 2).text())
        self.dialog_bond.cb_state.setCurrentIndex(trans[self.tableWidget.item(row, 3).text()])
        self.dialog_bond.le_tasty.setText(self.tableWidget.item(row, 4).text())
        self.dialog_bond.sb_price.setValue(float(self.tableWidget.item(row, 5).text()))
        self.dialog_bond.sb_volume.setValue(float(self.tableWidget.item(row, 6).text()))
        self.dialog_bond.statusBar().showMessage('')
        self.dialog_bond.show()

    def remove(self):
        connection = sqlite3.connect(DATABASE_PATH)
        cur = connection.cursor()

        for i in sorted(list(set([i.row() for i in self.tableWidget.selectedIndexes()])))[::-1]:
            cur.execute("DELETE FROM varieties WHERE id = ?",
                        (self.tableWidget.item(i, 0).text(),))

        connection.commit()
        connection.close()
        self.load_table()

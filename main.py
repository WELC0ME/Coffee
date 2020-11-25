import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QComboBox


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('Coffee')

        self.btn_add.clicked.connect(self.add)
        self.btn_remove.clicked.connect(self.remove)
        self.tableWidget.cellDoubleClicked.connect(self.edit)

        self.length = 0
        self.load_table()

    def load_table(self):
        connection = sqlite3.connect("coffee.db")
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
        dialog.lab_id.setText(str(self.length))
        dialog.le_sort.setText('')
        dialog.le_grade.setText('')
        dialog.cb_state.setCurrentIndex(0)
        dialog.le_tasty.setText('')
        dialog.sb_price.setValue(0.0)
        dialog.sb_volume.setValue(0.0)
        dialog.statusBar().showMessage('')
        dialog.show()

    def edit(self, row):
        trans = {'В зернах': 0, 'Молотый': 1}
        dialog.lab_id.setText(self.tableWidget.item(row, 0).text())
        dialog.le_sort.setText(self.tableWidget.item(row, 1).text())
        dialog.le_grade.setText(self.tableWidget.item(row, 2).text())
        dialog.cb_state.setCurrentIndex(trans[self.tableWidget.item(row, 3).text()])
        dialog.le_tasty.setText(self.tableWidget.item(row, 4).text())
        dialog.sb_price.setValue(float(self.tableWidget.item(row, 5).text()))
        dialog.sb_volume.setValue(float(self.tableWidget.item(row, 6).text()))
        dialog.statusBar().showMessage('')
        dialog.show()

    def remove(self):

        connection = sqlite3.connect("coffee.db")
        cur = connection.cursor()

        for i in sorted(list(set([i.row() for i in self.tableWidget.selectedIndexes()])))[::-1]:
            cur.execute("DELETE FROM varieties WHERE id = ?",
                        (self.tableWidget.item(i, 0).text(),))

        connection.commit()
        connection.close()
        self.load_table()


class Dialog(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.setWindowTitle('Add/Edit dialog')

        self.btn_confirm.clicked.connect(self.confirm)

    def confirm(self):

        try:
            connection = sqlite3.connect("coffee.db")
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

            ex.load_table()
            self.hide()
        except AssertionError:
            self.statusBar().showMessage('Error. Incorrect input')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    dialog = Dialog()
    ex.show()
    sys.exit(app.exec())

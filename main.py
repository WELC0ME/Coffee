import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('Coffee')

        self.connection = sqlite3.connect("coffee.db")
        cur = self.connection.cursor()

        request = "SELECT varieties.id, varieties.sort, varieties.grade, states.state, varieties.tasty, "
        request += "varieties.price, varieties.volume "
        request += "FROM varieties JOIN states ON states.id = varieties.state"
        res = cur.execute(request).fetchall()

        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels([i[0] for i in cur.description])
        self.tableWidget.setRowCount(0)

        for i, row in enumerate(res):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

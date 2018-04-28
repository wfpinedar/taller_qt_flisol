import sys
from PyQt5 import QtWidgets


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    b = QtWidgets.QLabel(w)
    b.setText("Hello World!")
    w.setGeometry(500, 500, 300, 100)
    b.move(110, 40)
    w.setWindowTitle("My first PyQt App ;)")
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()

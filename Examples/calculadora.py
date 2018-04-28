import sys
from PyQt5 import QtWidgets, uic, QtGui


class MyWindow(QtWidgets.QDialog):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('calculadora.ui', self)
        self.oper.addItems(["Suma", "Resta", "Producto", "Division"])
        self.opButton.clicked.connect(self.operar)
        self.show()

    def operar(self):
        n1 = int(self.num1.text())
        n2 = int(self.num2.text())
        op = self.oper.currentText()
        re = self.operacion(n1, n2, op)
        self.res.setText("Resultado: " + str(re))

    def operacion(self, n1, n2, op):
        if op == "Suma":
            re = n1 + n2
        elif op == "Resta":
            re = n1 - n2
        elif op == "Producto":
            re = n1 * n2
        elif op == "Division":
            if n2 == 0:
                re = " OPERACIÓN NO SE PUEDE REALIZAR"
            else:
                re = n1 / n2
        return re


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())

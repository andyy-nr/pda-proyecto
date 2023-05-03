import sys
from PyQt5 import QtWidgets, QtCore
from vistas.frmEmpleados import Ui_frmEmpleados

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    frm = QtWidgets.QWidget()
    ui = Ui_frmEmpleados()
    ui.setupUi(frm)
    frm.showMaximized()
    sys.exit(app.exec_())




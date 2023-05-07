import sys
from PyQt5 import QtWidgets, QtCore
from vistas.frmInicio import Ui_mw_inicio

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    frm = QtWidgets.QMainWindow()
    ui = Ui_mw_inicio()
    ui.setupUi(frm)
    frm.showMaximized()
    sys.exit(app.exec_())




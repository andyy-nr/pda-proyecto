import sys
from PyQt5 import QtWidgets, QtCore
from vistas.inicio import Ui_frmInicio

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    frm = QtWidgets.QWidget()
    ui = Ui_frmInicio()
    ui.setupUi(frm)
    frm.showMaximized()
    sys.exit(app.exec_())




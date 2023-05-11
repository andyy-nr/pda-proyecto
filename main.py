import sys
from PyQt5 import QtWidgets, QtCore
from controlador.ctrFrmInicioSesion import CtrlInicioSesion

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    frm = CtrlInicioSesion()
    frm.show()
    sys.exit(app.exec_())




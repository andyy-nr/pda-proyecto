import sys
from PyQt5 import QtWidgets, QtCore
from controlador.ctrInicio import CtrlFrmMainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    frm = CtrlFrmMainWindow()
    frm.show()
    sys.exit(app.exec_())




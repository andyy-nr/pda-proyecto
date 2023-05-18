from vistas.frmOpcion import Ui_frmOpcion
from PyQt5 import QtWidgets


class CtrlFrmGestionOpcion(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmOpcion()
        self.ui.setupUi(self)
        self.initControlGui()

    def agregarOpcion(self):
        print("Se unio!")

    def initControlGui(self):
        print("xd")

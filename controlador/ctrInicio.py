from vistas.frmInicio import Ui_mw_inicio
from PyQt5 import QtWidgets
from controlador.ctrOpciones import CtrlFrmGestionOpcion
from controlador.ctrGestionUsuarios import CtrlFrmGestionUser
from controlador.ctrGestionEmpleados import CtrlGestionEmpleados


class CtrlFrmMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mw_inicio()
        self.ui.setupUi(self)
        self.initControlGui()

    def initControlGui(self):
        ctrlUsuarios = CtrlFrmGestionUser()
        self.ui.btn_usuarios.clicked.connect(lambda : ctrlUsuarios.show())
        #ctrlOpcion = CtrlFrmGestionOpcion()
        #self.ui.btn_opcion.clicked.connect(lambda : ctrlOpcion.show())
        ctrlEmpleados = CtrlGestionEmpleados()
        self.ui.btn_empleados.clicked.connect(lambda : ctrlEmpleados.show())



from PyQt5.QtCore import Qt
from vistas.frmInicio import Ui_mw_inicio
from PyQt5 import QtWidgets

from datos.employees import Dt_employees
from datos.Dt_Tbl_user import Dt_tbl_user
from datos.departments import Dt_departments

from controlador.ctrGestionOpciones import CtrlFrmGestionOpcion
from controlador.ctrGestionUsuarios import CtrlFrmGestionUser
from controlador.ctrGestionEmpleados import CtrlGestionEmpleados
from controlador.ctrGestionRegiones import CtrlGestionRegiones
from controlador.ctrGestionTrabajos import CtrlGestionTrabajos
from controlador.ctrGestionOpciones import CtrlFrmGestionOpcion
from controlador.ctrGestionPaises import CtrlGestionPaises
from controlador.ctrGestionRoles import CtrlFrmGestionRoles
from controlador.ctrGestionLocalidades import CtrlGestionLocalidades
from controlador.ctrGestionDepartamentos import CtrlGestionDepartaments

class CtrlFrmMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mw_inicio()
        self.ui.setupUi(self)
        self.initControlGui()
        self.mostrarDatos()

    def mostrarDatos(self):
        dt_Empleados = Dt_employees()
        self.ui.lbl_cant_empleados.setText(dt_Empleados.totalEmpleados())
        self.ui.lbl_cant_empleados.setAlignment(Qt.AlignCenter)

        dt_Usuarios = Dt_tbl_user()
        self.ui.lbl_cant_usuarios.setText(dt_Usuarios.totalUsuarios())
        self.ui.lbl_cant_usuarios.setAlignment(Qt.AlignCenter)

        dt_Departamentos = Dt_departments()
        self.ui.lbl_cant_departamentos.setText(dt_Departamentos.totalDepartamentos())
        self.ui.lbl_cant_departamentos.setAlignment(Qt.AlignCenter)


    def initControlGui(self):
        ctrlUsuarios = CtrlFrmGestionUser()
        self.ui.btn_usuarios.clicked.connect(lambda : ctrlUsuarios.show())

        ctrlOpcion = CtrlFrmGestionOpcion()
        self.ui.btn_opcion.clicked.connect(lambda : ctrlOpcion.show())

        ctrlEmpleados = CtrlGestionEmpleados()
        self.ui.btn_empleados.clicked.connect(lambda : ctrlEmpleados.show())

        ctrlRegiones  = CtrlGestionRegiones()
        self.ui.btn_regiones.clicked.connect(lambda : ctrlRegiones.show())

        ctrlTrabajos = CtrlGestionTrabajos()
        self.ui.btn_trabajos.clicked.connect(lambda : ctrlTrabajos.show())

        ctrlOpcion = CtrlFrmGestionOpcion()
        self.ui.btn_opcion.clicked.connect(lambda : ctrlOpcion.show())

        ctrlPaises = CtrlGestionPaises()
        self.ui.btn_paises.clicked.connect(lambda : ctrlPaises.show())

        ctrlRoles = CtrlFrmGestionRoles()
        self.ui.btn_roles.clicked.connect(lambda : ctrlRoles.show())

        ctrlLocalidades = CtrlGestionLocalidades()
        self.ui.btn_localidades.clicked.connect(lambda : ctrlLocalidades.show())

        ctrlDepartamentos = CtrlGestionDepartaments()
        self.ui.btn_departamentos.clicked.connect(lambda : ctrlDepartamentos.show())

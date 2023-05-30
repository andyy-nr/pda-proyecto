from PyQt5.QtCore import Qt, pyqtSignal
from vistas.frmInicio import Ui_mw_inicio
from PyQt5 import QtWidgets

from datos.employees import Dt_employees
from datos.Dt_Tbl_user import Dt_tbl_user
from datos.departments import Dt_departments
from datos.dependents import Dt_dependents
from datos.Dt_tbl_UserRol import Dt_tbl_UserRol
from datos.Dt_Tbl_opcion import Dt_tbl_opcion

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
from controlador.ctrGestionRolOpcion import CtrlGestionRolOpcion
from controlador.ctrGestionRolUsuario import CtrlGestionRolUsuario
from controlador.ctrGestionDependientes import CtrlGestionDependientes

class CtrlFrmMainWindow(QtWidgets.QMainWindow):
    def __init__(self, usuario):
        super().__init__()
        self.ui = Ui_mw_inicio()
        self.ui.setupUi(self)
        self.initControlGui()
        self._usuario = usuario
        self.mostrarInfoUsuario()
        self.mostrarDatos()

    def mostrarInfoUsuario(self):
        # Informacion de usuario
        dru = Dt_tbl_UserRol()
        rolUsuario = dru.obtenerRolXUser(self._usuario._user)
        self.ui.lbl_nombre_usuario.setText(self._usuario._user)
        self.ui.lbl_nombre_usuario.setAlignment(Qt.AlignCenter)
        self.ui.lbl_rol_usuario.setText(rolUsuario)
        self.ui.lbl_rol_usuario.setAlignment(Qt.AlignCenter)
        self.ui.lbl_correo.setText(self._usuario._email)
        self.ui.lbl_correo.setAlignment(Qt.AlignCenter)

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

        dt_dependientes = Dt_dependents()
        self.ui.lbl_cant_dependientes.setText(dt_dependientes.totalDependientes())
        self.ui.lbl_cant_dependientes.setAlignment(Qt.AlignCenter)

    def mostrarFormulario(self, form):
        self.form = form()
        self.form.showMaximized()

    def initControlGui(self):
        self.ui.btn_empleados.clicked.connect(lambda: self.mostrarFormulario(CtrlGestionEmpleados))
        self.ui.btn_departamentos.clicked.connect(lambda: self.mostrarFormulario(CtrlGestionDepartaments))
        self.ui.btn_dependientes.clicked.connect(lambda: self.mostrarFormulario(CtrlGestionDependientes))
        self.ui.btn_localidades.clicked.connect(lambda: self.mostrarFormulario(CtrlGestionLocalidades))
        self.ui.btn_opcion.clicked.connect(lambda: self.mostrarFormulario(CtrlFrmGestionOpcion))
        self.ui.btn_opcionRol.clicked.connect(lambda: self.mostrarFormulario(CtrlGestionRolOpcion))
        self.ui.btn_paises.clicked.connect(lambda: self.mostrarFormulario(CtrlGestionPaises))
        self.ui.btn_regiones.clicked.connect(lambda: self.mostrarFormulario(CtrlGestionRegiones))
        self.ui.btn_roles.clicked.connect(lambda: self.mostrarFormulario(CtrlFrmGestionRoles))
        self.ui.btn_rolUsuario.clicked.connect(lambda: self.mostrarFormulario(CtrlGestionRolUsuario))
        self.ui.btn_trabajos.clicked.connect(lambda: self.mostrarFormulario(CtrlGestionTrabajos))
        self.ui.btn_usuarios.clicked.connect(lambda: self.mostrarFormulario(CtrlFrmGestionUser))
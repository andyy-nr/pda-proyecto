from vistas.frmInicio import Ui_mw_inicio
from PyQt5 import QtWidgets
from vistas.frmDepartamentos import Ui_frmDepartamentos
from vistas.frmDependientes import Ui_frmDependientes
from vistas.frmEmpleados import Ui_frmEmpleados
from vistas.frmLocalidades import Ui_frmLocalidades
from vistas.frmOpcion import Ui_frmOpcion
from vistas.frmOpcionRol import Ui_frmOpcionRol
from vistas.frmPaises import Ui_frmPaises
from vistas.frmRegiones import Ui_frmRegiones
from vistas.frmRoles import Ui_frmRoles
from vistas.frmRolesUsuario import Ui_frmRolesUsuario
from vistas.frmTrabajo import Ui_frmTrabajo
from vistas.frmUsuario import Ui_frmUsuario

class CtrlFrmMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mw_inicio()
        self.ui.setupUi(self)
        self.initControlGui()

    def mostrarFormulario(self, form):
        self.window = QtWidgets.QWidget()
        self.ui = form()
        self.ui.setupUi(self.window)
        self.window.showMaximized()


    def initControlGui(self):
        self.ui.btn_empleados.clicked.connect(lambda : self.mostrarFormulario(Ui_frmEmpleados))
        self.ui.btn_departamentos.clicked.connect(lambda : self.mostrarFormulario(Ui_frmDepartamentos))
        self.ui.btn_dependientes.clicked.connect(lambda : self.mostrarFormulario(Ui_frmDependientes))
        self.ui.btn_localidades.clicked.connect(lambda : self.mostrarFormulario(Ui_frmLocalidades))
        self.ui.btn_opcion.clicked.connect(lambda : self.mostrarFormulario(Ui_frmOpcion))
        self.ui.btn_opcionRol.clicked.connect(lambda : self.mostrarFormulario(Ui_frmOpcionRol))
        self.ui.btn_paises.clicked.connect(lambda : self.mostrarFormulario(Ui_frmPaises))
        self.ui.btn_regiones.clicked.connect(lambda : self.mostrarFormulario(Ui_frmRegiones))
        self.ui.btn_roles.clicked.connect(lambda : self.mostrarFormulario(Ui_frmRoles))
        self.ui.btn_rolUsuario.clicked.connect(lambda : self.mostrarFormulario(Ui_frmRolesUsuario))
        self.ui.btn_trabajos.clicked.connect(lambda : self.mostrarFormulario(Ui_frmTrabajo))
        self.ui.btn_usuarios.clicked.connect(lambda : self.mostrarFormulario(Ui_frmUsuario))




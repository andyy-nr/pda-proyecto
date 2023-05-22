from vistas.frmNuevoUsuario import Ui_Form
from PyQt5 import QtWidgets
from datos.Dt_Tbl_user import Dt_tbl_user
from controlador.ctrInicioSesion import CtrlInicioSesion


class CtrlPrimerUsuario(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.inicioSesion = CtrlInicioSesion()
        self.ui.btn_agregar.clicked.connect(self.agregarUsuario)
    dtu = Dt_tbl_user()


    def agregarUsuario(self):
        if self.validarVacios():
            nombre_usuario = self.ui.le_nombre_usuario.text()
            nombres = self.ui.le_nombres.text()
            apellidos = self.ui.le_apellidos.text()
            email = self.ui.le_email.text()
            contrasena = self.ui.le_contrasena.text()
            confirmacion = self.ui.le_confirmacion.text()
            estado = 1
            try:
                if self.dtu.agregarUsuario(nombre_usuario, contrasena, nombres, apellidos, email, confirmacion, estado):
                    self.abrirInicioSesion()
            except Exception as e:
                print(f"Error al agregar usuario: {e}")
        else:
            print("Campos vacios")

    def validarVacios(self):
        if self.ui.le_email.text() == "":
            return False
        if self.ui.le_nombres.text() == "":
            return False
        if self.ui.le_nombre_usuario.text() == "":
            return False
        if self.ui.le_apellidos.text() == "":
            return False
        if self.ui.le_contrasena.text() == "":
            return False
        if self.ui.le_confirmacion.text() == "":
            return False
        if self.ui.le_confirmar_correo.text() == "":
            return False
        return True

    def abrirInicioSesion(self):
        self.inicioSesion.show()
        self.close()

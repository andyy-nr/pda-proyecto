from PyQt5.QtWidgets import QMessageBox

from vistas.frmUsuario import Ui_frmUsuario
from datos.Dt_Tbl_user import Dt_tbl_user
from PyQt5 import QtWidgets


class CtrlFrmGestionUser(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmUsuario()
        self.ui.setupUi(self)
        self.initControlGui()
    dtu = Dt_tbl_user()

    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.agregarUsuario)
        self.ui.btn_limpiar.clicked.connect(self.limpiarCampos)
        self.cargarDatos()


    def limpiarCampos(self):
        self.ui.le_codigo.setText("")
        self.ui.le_nombres.setText("")
        self.ui.le_nombre_usuario.setText("")
        self.ui.le_apellidos.setText("")
        self.ui.le_email.setText("")
        self.ui.le_contrasena.setText("")
        self.ui.le_confirmacion.setText("")
        self.ui.le_confirmar_correo.setText("")

    def cargarDatos(self):
        listUsuario = self.dtu.listUsuarios()
        i = len(listUsuario)
        self.ui.tbl_Usuario.setRowCount(i)
        tablerow = 0
        for row in listUsuario:
            self.ui.tbl_Usuario.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row._user))
            self.ui.tbl_Usuario.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row._nombres))
            self.ui.tbl_Usuario.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row._apellidos))
            self.ui.tbl_Usuario.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row._email))
            tablerow = tablerow + 1

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

    def validarUsuarioRepetido(self):
        usuarios = self.dtu.listUsuarios()
        for usuario in usuarios:
            if usuario._user == self.ui.le_nombre_usuario.text():
                return False
        return True

    def agregarUsuario(self):
        if self.validarVacios():
            if self.validarUsuarioRepetido():
                user = self.ui.le_nombre_usuario.text()
                pwd = self.ui.le_contrasena.text()
                nombres = self.ui.le_nombres.text()
                apellidos = self.ui.le_apellidos.text()
                email = self.ui.le_email.text()
                pwd_temp = self.ui.le_confirmacion.text()
                estado = 1
                try:
                    self.dtu.agregarUsuario(user, pwd, nombres, apellidos, email, pwd_temp, estado)
                    self.cargarDatos()
                    self.limpiarCampos()
                except Exception as e:
                    print(f"Error al agregar el registro: {e}")
                else:
                    print("El usuario ya se encuentra en la BD")
                    self.limpiarCampos()
        else:
            print("Campos vacios")


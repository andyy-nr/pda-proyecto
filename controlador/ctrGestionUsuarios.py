from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMessageBox

from vistas.frmUsuario import Ui_frmUsuario
from datos.Dt_Tbl_user import Dt_tbl_user
from PyQt5 import QtWidgets
from entidades.Tbl_user import Tbl_user
from negocio.ngUsuarios import ngUsuarios

class CtrlFrmGestionUser(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmUsuario()
        self.ui.setupUi(self)
        self.initControlGui()
        self.ui.tbl_Usuario.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
    actualizar_info = pyqtSignal()
    dtu = Dt_tbl_user()
    ngu = ngUsuarios()

    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.agregarUsuario)
        self.ui.btn_editar.clicked.connect(self.editarUsuario)
        self.ui.btn_eliminar.clicked.connect(self.eliminarUsuario)
        self.ui.btn_limpiar.clicked.connect(self.limpiarCampos)
        self.ui.btn_buscar.clicked.connect(lambda: self.cargarDatos(1))
        self.ui.tbl_Usuario.clicked.connect(self.seleccionarElemento)
        self.ui.le_buscar.textChanged.connect(self.buscarVacio)
        self.cargarDatos(0)

    def buscarVacio(self):
        if self.ui.le_buscar.text() == "":
            self.cargarDatos(0)

    def limpiarCampos(self):
        self.ui.le_codigo.setText("")
        self.ui.le_nombres.setText("")
        self.ui.le_nombre_usuario.setText("")
        self.ui.le_apellidos.setText("")
        self.ui.le_email.setText("")
        self.ui.le_contrasena.setText("")
        self.ui.le_confirmacion.setText("")
        self.ui.le_confirmar_correo.setText("")
        self.ui.le_buscar.setText("")
        self.cargarDatos(0)

    def cargarDatos(self, modo):
        if modo == 1: # Buscar
            texto = self.ui.le_buscar.text()
            if texto != "":
                self.ui.tbl_Usuario.clearSelection()
                listUsuario = self.dtu.buscarUsuario(texto)
            else:
                QMessageBox.warning(self, "Advertencia", "Ingrese un texto para buscar")
                return
        else: # Cargar todos los datos
            listUsuario = self.dtu.listUsuariosNoEliminados()
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

    def validarCorreo(self):
        if self.ui.le_email.text() == self.ui.le_confirmar_correo.text():
            return True
        return False

    def seleccionarElemento(self):
        try:
            fila = self.ui.tbl_Usuario.selectedIndexes()[0].row()
            usuarios = self.dtu.listUsuariosNoEliminados()
            usuario = usuarios[fila]
            self.ui.le_codigo.setText(str(usuario._id_user))
            self.ui.le_nombres.setText(usuario._nombres)
            self.ui.le_nombre_usuario.setText(usuario._user)
            self.ui.le_apellidos.setText(usuario._apellidos)
            self.ui.le_email.setText(usuario._email)
            self.ui.le_confirmar_correo.setText(usuario._email)
        except Exception as e:
            print(e)


    def agregarUsuario(self):
        if not self.validarVacios():
            print("Campos vacios")
            return
        if not self.validarCorreo():
            print("Correos no coinciden")
            return

        user = self.ui.le_nombre_usuario.text()
        pwd = self.ui.le_contrasena.text()
        nombres = self.ui.le_nombres.text()
        apellidos = self.ui.le_apellidos.text()
        email = self.ui.le_email.text()
        pwd_temp = self.ui.le_confirmacion.text()
        estado = 1
        usuario = Tbl_user(user=user, pwd=pwd, nombres=nombres, apellidos=apellidos, email=email,
                           pwd_temp=pwd_temp, estado=estado)
        try:
            self.ngu.agregarUsuario(usuario)
            self.cargarDatos(0)
            self.limpiarCampos()
            self.actualizar_info.emit()
        except Exception as e:
            print(f"Error al agregar el registro: {e}")

    def eliminarUsuario(self):
        try:
            fila = self.ui.tbl_Usuario.selectedIndexes()[0].row()
            usuarios = self.dtu.listUsuariosNoEliminados()
            usuario = usuarios[fila]
            self.dtu.eliminarUsuario(usuario)
            self.cargarDatos(0)
            self.limpiarCampos()
            self.actualizar_info.emit()
        except IndexError as e:
            QMessageBox.warning(self, "Advertencia", "Seleccione un registro para eliminar")
        except Exception as e:
            print(e)

    def editarUsuario(self):
        if self.validarVacios():
            user = self.ui.le_nombre_usuario.text()
            pwd = self.ui.le_contrasena.text()
            nombres = self.ui.le_nombres.text()
            apellidos = self.ui.le_apellidos.text()
            email = self.ui.le_email.text()
            pwd_temp = self.ui.le_confirmacion.text()
            estado = 2
            usuario = Tbl_user(user=user, pwd=pwd, nombres=nombres, apellidos=apellidos, email=email,
                               pwd_temp=pwd_temp, estado=estado)
            try:
                fila = self.ui.tbl_Usuario.selectedIndexes()[0].row()
                usuarios = self.dtu.listTodosUsuarios()
                user_act = usuarios[fila]
                usr_id = user_act[fila]._id_user
                contra_vieja = user_act[fila]._pwd
                self.ngu.modificarUsuario(usuario, contra_vieja, usr_id)
                self.cargarDatos(0)
                self.limpiarCampos()
                self.ui.tbl_Usuario.clearSelection()
            except IndexError as e:
                QMessageBox.warning(self, "Advertencia", "Seleccione un registro para editar")
        else:
            print("Campos vacios")

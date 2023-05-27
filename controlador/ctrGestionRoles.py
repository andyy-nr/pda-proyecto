from PyQt5.QtWidgets import QMessageBox

from vistas.frmRoles  import Ui_frmRoles
from datos.Dt_Tbl_rol import Dt_tbl_rol
from entidades.Tbl_rol import Tbl_rol
from PyQt5 import QtWidgets

class CtrlFrmGestionRoles(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmRoles()
        self.ui.setupUi(self)
        self.initControlGui()
    dto = Dt_tbl_rol()

    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.agregarRol)
        self.ui.btn_eliminar_2.clicked.connect(self.limpiarCampos)
        self.ui.btn_buscar.clicked.connect(lambda: self.cargarDatos(1))
        self.cargarDatos(0)

    def limpiarCampos(self):
        self.ui.txt_codigo.setText("")
        self.ui.txt_rol.setText("")
        self.cargarDatos(0)
        self.ui.txt_buscar.setText("")

    def cargarDatos(self, modo):
        if modo == 1:
            texto = self.ui.txt_buscar.text()
            if texto != "":
                listaRoles = self.dto.buscarRol(texto)
            else:
                QMessageBox.warning(self, "Error", "No se ha ingresado un rol a buscar")
                return
        else:
            listaRoles = self.dto.listaRoles()
        i = len(listaRoles)
        self.ui.tbl_roles.setRowCount(i)
        tablerow = 0
        for row in listaRoles:
            self.ui.tbl_roles.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row._id_rol)))
            self.ui.tbl_roles.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row._rol))
            tablerow = tablerow + 1

    def validarVacios(self):
        if self.ui.txt_rol.text() == "":
            return False
        return True

    def validarNoRepetido(self):
        listaRoles = self.dto.listaRoles()
        for row in listaRoles:
            if row._rol == self.ui.txt_rol.text():
                return False
        return True

    def agregarRol(self):
        if self.validarVacios():
            if not self.validarNoRepetido():
                print("Rol ya existe")
                return
            rol_texto = self.ui.txt_rol.text()
            estado = 1
            rol = Tbl_rol(rol=rol_texto, estado=estado)
            try:
                self.dto.agregarRol()
                self.cargarDatos()
                self.limpiarCampos()
            except Exception as e:
                print(f"Error al agregar rol: {e}")


from PyQt5.QtWidgets import QMessageBox

from vistas.frmRolesUsuario import Ui_frmRolesUsuario
from datos.Dt_Tbl_rol import Dt_tbl_rol
from datos.Dt_Tbl_user import Dt_tbl_user
from datos.Dt_tbl_UserRol import Dt_tbl_UserRol
from entidades.Tbl_UserRol import Tbl_UserRol
from negocio.ngUserRol import ngUserRol
from PyQt5 import QtWidgets

class CtrlGestionRolUsuario(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmRolesUsuario()
        self.ui.setupUi(self)
        self.initControlGui()
        self.ui.tbl_opcionRol.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
    dr = Dt_tbl_rol()
    du = Dt_tbl_user()
    dur = Dt_tbl_UserRol()
    ngur = ngUserRol()

    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.agregarRolUsuario)
        self.ui.btn_limpiar.clicked.connect(self.limpiarCampos)
        self.ui.btn_eliminar.clicked.connect(self.eliminarRolUsuario)
        self.ui.btn_buscar.clicked.connect(lambda: self.cargarDatos(1))
        self.ui.tbl_opcionRol.clicked.connect(self.seleccionarElementos)
        self.ui.txt_buscar.textChanged.connect(self.buscarVacio)
        self.cargarDatos(0)
        self.cargarCombobox()

    def buscarVacio(self):
        if self.ui.txt_buscar.text() == "":
            self.cargarDatos(0)

    def cargarDatos(self, modo):
        if modo == 1:
            texto = self.ui.txt_buscar.text()
            if texto != "":
                self.ui.tbl_opcionRol.clearSelection()
                listaRolUsuario = self.dur.buscarUserRol(texto)
            else:
                QMessageBox.about(self, "Error", "No se puede buscar con el campo vacio")
                return
        else:
            listaRolUsuario = self.dur.listaUserRol()
        i = len(listaRolUsuario)
        self.ui.tbl_opcionRol.setRowCount(i)
        tablerow = 0
        for row in listaRolUsuario:
            self.ui.tbl_opcionRol.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row._id_UserRol)))
            self.ui.tbl_opcionRol.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row._user)))
            self.ui.tbl_opcionRol.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row._rol)))
            tablerow = tablerow + 1

    def cargarCombobox(self):
        try:
            listaRol = self.dr.listaRoles()
            self.ui.cbox_rol.addItem("Rol*")
            for rol in listaRol:
                self.ui.cbox_rol.addItem(str(rol._rol), int(rol._id_rol))
        except Exception as e:
            print(e)
        try:
            listaUser = self.du.listUsuariosNoEliminados()
            self.ui.cbox_opcion.addItem("Usuario*")
            for user in listaUser:
                self.ui.cbox_opcion.addItem(str(user._user), int(user._id_user))
        except Exception as e:
            print(e)

    def validarVacios(self):
        if self.ui.cbox_rol.currentData() is None:
            return False
        if self.ui.cbox_opcion.currentData() is None:
            return False
        return True

    def validarNoRepetido(self):
        rolUsuario = self.dur.listaUserRol()
        for row in rolUsuario:
            if row._id_user == self.ui.cbox_opcion.currentData() and row._id_rol == self.ui.cbox_rol.currentData():
                return False
        return True

    def limpiarCampos(self):
        self.ui.cbox_rol.setCurrentIndex(0)
        self.ui.cbox_opcion.setCurrentIndex(0)
        self.ui.txt_buscar.setText("")
        self.cargarDatos(0)

    def seleccionarElementos(self):
        try:
            fila = self.ui.tbl_opcionRol.selectedIndexes()[0].row()
            rolUsuarios = self.dur.listaUserRol()
            rolUsuario = rolUsuarios[fila]
            self.ui.cbox_rol.setCurrentText(rolUsuario._rol)
            self.ui.cbox_opcion.setCurrentText(rolUsuario._user)
        except Exception as e:
            print(e)
        except IndexError as e:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Seleccione un elemento de la tabla")

    def agregarRolUsuario(self):
        if self.validarVacios():
            if not self.validarNoRepetido():
                print("Rol repetido")
                return
            rol = self.ui.cbox_rol.currentData()
            user = self.ui.cbox_opcion.currentData()
            rolUsuario = Tbl_UserRol(id_user=user, id_rol=rol)
            self.ngur.agregarUserRol(rolUsuario)
            self.cargarDatos(0)
            self.limpiarCampos()
        else:
            print("Campos vacios")

    def eliminarRolUsuario(self):
        try:
            fila = self.ui.tbl_opcionRol.selectedIndexes()[0].row()
            rolUsuarios = self.dur.buscarUserRol(self.ui.txt_buscar.text())
            rolUsuario = rolUsuarios[fila]
            self.dur.eliminarUserRol(rolUsuario)
            self.cargarDatos(0)
            self.limpiarCampos()
        except Exception as e:
            print(e)
        except IndexError as e:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Seleccione un elemento de la tabla")

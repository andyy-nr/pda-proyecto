from PyQt5.QtWidgets import QMessageBox

from vistas.frmRoles  import Ui_frmRoles
from datos.Dt_Tbl_rol import Dt_tbl_rol
from entidades.Tbl_rol import Tbl_rol
from negocio.ngRol import ngTbl_rol
from PyQt5 import QtWidgets

class CtrlFrmGestionRoles(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmRoles()
        self.ui.setupUi(self)
        self.initControlGui()
        self.ui.tbl_roles.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
    dto = Dt_tbl_rol()
    ngr = ngTbl_rol()

    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.agregarRol)
        self.ui.btn_limpiar.clicked.connect(self.limpiarCampos)
        self.ui.btn_eliminar.clicked.connect(self.eliminarRol)
        self.ui.btn_editar.clicked.connect(self.modificarRol)
        self.ui.btn_buscar.clicked.connect(lambda: self.cargarDatos(1))
        self.ui.tbl_roles.clicked.connect(self.seleccionarElemento)
        self.ui.txt_buscar.textChanged.connect(self.buscarVacio)
        self.cargarDatos(0)

    def buscarVacio(self):
        if self.ui.txt_buscar.text() == "":
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
                self.ui.tbl_roles.clearSelection()
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

    def seleccionarElemento(self):
        try:
            fila = self.ui.tbl_roles.selectedIndexes()[0].row()
            roles = self.dto.listaRoles()
            rol = roles[fila]
            self.ui.txt_codigo.setText(str(rol._id_rol))
            self.ui.txt_rol.setText(rol._rol)
            return rol
        except Exception as e:
            print(f"Error al seleccionar elemento: {e}")
        except IndexError as e:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Seleccione un elemento de la tabla")

    def agregarRol(self):
        if self.validarVacios():
            rol_texto = self.ui.txt_rol.text()
            estado = 1
            rol = Tbl_rol(rol=rol_texto, estado=estado)
            try:
                self.ngr.agregarRol(rol)
                self.cargarDatos(0)
                self.limpiarCampos()
            except Exception as e:
                print(f"Error al agregar rol: {e}")

    def modificarRol(self):
        if self.validarVacios():
            codigo = self.ui.txt_codigo.text()
            rol_texto = self.ui.txt_rol.text()
            estado = 1
            rol = Tbl_rol(codigo, rol_texto, estado)
            try:
                self.ngr.modificarRol(rol, codigo)
                self.cargarDatos(0)
                self.limpiarCampos()
                self.ui.tbl_roles.clearSelection()
            except Exception as e:
                print(f"Error al agregar rol: {e}")

    def eliminarRol(self):
        rol = self.seleccionarElemento()
        if rol is not None:
            self.dto.eliminarRol(rol)
            self.cargarDatos(0)
            self.limpiarCampos()
            self.ui.tbl_roles.clearSelection()
        else:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Seleccione un elemento de la tabla")

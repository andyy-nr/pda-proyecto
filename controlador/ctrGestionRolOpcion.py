from PyQt5.QtWidgets import QMessageBox

from vistas.frmOpcionRol import Ui_frmOpcionRol
from datos.Dt_Tbl_rol import Dt_tbl_rol
from datos.Dt_Tbl_opcion import Dt_tbl_opcion
from datos.Dt_tbl_rolOpcion import Dt_tbl_rolOpcion
from entidades.Tbl_rolOpcion import Tbl_rolOpcion
from PyQt5 import QtWidgets

class CtrlGestionRolOpcion(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmOpcionRol()
        self.ui.setupUi(self)
        self.initControlGui()
        self.ui.tbl_opcionRol.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
    dro = Dt_tbl_rolOpcion()
    do = Dt_tbl_opcion()
    dr = Dt_tbl_rol()

    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.agregarRolOpcion)
        self.ui.btn_limpiar.clicked.connect(self.limpiarCampos)
        self.ui.btn_buscar.clicked.connect(lambda: self.cargarDatos(1))
        self.ui.tbl_opcionRol.clicked.connect(self.seleccionarElemento)
        self.ui.txt_buscar.textChanged.connect(self.buscarVacio)
        self.cargarDatos(0)
        self.cargarCombobox()

    def buscarVacio(self):
        if self.ui.txt_buscar.text() == "":
            self.cargarDatos(0)

    def cargarDatos(self, modo):
        if modo == 1:
            texto = self.ui.txt_buscar.text()
            if not texto == "":
                self.ui.tbl_opcionRol.clearContents()
                listaRolOpcion = self.dro.buscarRolOpcion(texto)
            else:
                QMessageBox.about(self, "Error", "Ingrese un texto para buscar")
                return
        else:
            listaRolOpcion = self.dro.listaRolOpcion()
        i = len(listaRolOpcion)
        self.ui.tbl_opcionRol.setRowCount(i)
        tablerow = 0
        for row in listaRolOpcion:
            self.ui.tbl_opcionRol.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row._id_rolOpcion)))
            self.ui.tbl_opcionRol.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row._opcion))
            self.ui.tbl_opcionRol.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row._rol))
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
            listaOpcion = self.do.listaOpciones()
            self.ui.cbox_opcion.addItem("Opcion*")
            for opcion in listaOpcion:
                self.ui.cbox_opcion.addItem(str(opcion._opcion), int(opcion._id_opcion))
        except Exception as e:
            print(e)

    def validarVacio(self):
        if self.ui.cbox_opcion.currentData() is None:
            return False
        if  self.ui.cbox_rol.currentData() is None:
            return False
        return True

    def limpiarCampos(self):
        self.ui.cbox_rol.setCurrentIndex(0)
        self.ui.cbox_opcion.setCurrentIndex(0)
        self.ui.txt_buscar.setText("")
        self.cargarDatos(0)

    def validarNoRepetido(self):
        rolOpcion = self.dro.listaRolOpcion()
        for row in rolOpcion:
            if row._rol == self.ui.cbox_rol.currentText() and row._opcion == self.ui.cbox_opcion.currentText():
                return False
        return True

    def seleccionarElemento(self):
        try:
            fila = self.ui.tbl_opcionRol.selectedIndexes()[0].row()
            rolOpciones = self.dro.listaRolOpcion()
            rolOpcion = rolOpciones[fila]
            self.ui.cbox_rol.setCurrentText(rolOpcion._rol)
            self.ui.cbox_opcion.setCurrentText(rolOpcion._opcion)
        except Exception as e:
            print(e)
        except IndexError as e:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Seleccione un elemento de la tabla")

    def agregarRolOpcion(self):
        if self.validarVacio():
            if not self.validarNoRepetido():
                print("Rol y opcion ya existen")
                return
            rol = self.ui.cbox_rol.currentData()
            opcion = self.ui.cbox_opcion.currentData()
            rolOpcion = Tbl_rolOpcion(id_opcion=opcion, id_rol=rol)
            self.dro.agregarRolOpcion(opcion)
            self.cargarDatos(0)
            self.limpiarCampos()
        else:
            print("Hay campos vacios")



from vistas.frmOpcion import Ui_frmOpcion
from PyQt5 import QtWidgets
from datos.Dt_Tbl_opcion import Dt_tbl_opcion
from negocio.ngOpciones import ngOpciones
from PyQt5.QtWidgets import QMessageBox, QTableView
from entidades.Tbl_opcion import Tbl_opcion

class CtrlFrmGestionOpcion(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmOpcion()
        self.ui.setupUi(self)
        self.initControlGui()
        self.ui.tbl_opcion.setSelectionBehavior(QTableView.SelectRows)
    dto = Dt_tbl_opcion() # Instancia de la clase Dt_tbl_opcion
    ngo = ngOpciones()

    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.agregarOpcion)
        self.ui.btn_editar.clicked.connect(self.modificarOpcion)
        self.ui.btn_eliminar.clicked.connect(self.eliminarOpcion)
        self.ui.btn_limpiar.clicked.connect(self.limpiarCampos)
        self.ui.tbl_opcion.clicked.connect(self.seleccionarElemento)
        self.ui.btn_buscar.clicked.connect(lambda: self.cargarDatos(1))
        self.ui.txt_buscar.textChanged.connect(self.buscarVacio)
        self.cargarDatos(0)

    def buscarVacio(self):
        if self.ui.txt_buscar.text() == "":
            self.cargarDatos(0)

    def limpiarCampos(self):
        self.ui.txt_codigo.setText("")
        self.ui.txt_opcion.setText("")
        self.ui.btn_buscar.setText("")
        self.cargarDatos(0)

    def cargarDatos(self, modo):
        if modo == 1: # Buscar
            texto = self.ui.txt_buscar.text()
            if texto != "":
                self.ui.tbl_opcion.clearSelection()
                listaOpciones = self.dto.buscarOpcion(texto)
            else:
                QtWidgets.QMessageBox.warning(self, "Advertencia", "Ingrese un texto para buscar")
                return
        else: # Cargar todos los datos
            listaOpciones = self.dto.listaOpciones()
        i = len(listaOpciones)
        self.ui.tbl_opcion.setRowCount(i)
        tablerow = 0
        for row in listaOpciones:
            self.ui.tbl_opcion.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row._id_opcion)))
            self.ui.tbl_opcion.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row._opcion))
            tablerow = tablerow + 1

    def validarVacios(self):
        if self.ui.txt_opcion.text() == "":
            return False
        return True

    def seleccionarElemento(self):
        try:
            fila = self.ui.tbl_opcion.selectedIndexes()[0].row()
            opciones = self.dto.buscarOpcion(self.ui.txt_buscar.text())
            opc_seleccionada = opciones[fila]
            self.ui.txt_codigo.setText(str(opc_seleccionada._id_opcion))
            self.ui.txt_opcion.setText(opc_seleccionada._opcion)
            return opc_seleccionada
        except IndexError as e:
            QMessageBox.warning(self, "Advertencia", "Seleccione un elemento de la tabla")

    def agregarOpcion(self):
        if self.validarVacios():
            opc = self.ui.txt_opcion.text()
            estado = 1
            opcion = Tbl_opcion(None, opc, estado)
            try:
                self.ngo.agregarOpcion(opcion)
                self.cargarDatos(0)
                self.limpiarCampos()
            except Exception as e:
                print(f"Error al agregar opcion: {e}")
        else:
            QMessageBox.warning(self, "Advertencia", "Rellene todos los campos")

    def modificarOpcion(self):
        if self.validarVacios():
            codigo = self.ui.txt_codigo.text()
            opc = self.ui.txt_opcion.text()
            estado = 2
            opcion = Tbl_opcion(codigo, opc, estado)
            try:
                self.ngo.modificarOpcion(opcion, codigo)
                self.cargarDatos(0)
                self.limpiarCampos()
                self.ui.tbl_opcion.clearSelection()
            except Exception as e:
                print(f"ctrModificarOpcion: {e}")
        else:
            QMessageBox.warning(self, "Advertencia", "Seleccione un rol")

    def eliminarOpcion(self):
        opcion = self.seleccionarElemento()
        if opcion is not None:
            try:
                self.dto.eliminarOpcion(opcion)
                self.cargarDatos(0)
                self.limpiarCampos()
                self.ui.tbl_opcion.clearSelection()
            except Exception as e:
                print(f"Error al eliminar opcion: {e}")

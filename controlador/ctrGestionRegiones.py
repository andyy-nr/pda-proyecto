from PyQt5.QtWidgets import QMessageBox

from vistas.frmRegiones import Ui_frmRegiones
from datos.regions import Dt_Regions
from entidades.Regions import regions
from negocio.ngRegiones import ngRegiones
from PyQt5 import QtWidgets


class CtrlGestionRegiones(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmRegiones()
        self.ui.setupUi(self)
        self.initControlGui()
        self.ui.tbl_regiones.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
    dtu = Dt_Regions()
    ngr = ngRegiones()

    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.agregarRegion)
        self.ui.btn_limpiar.clicked.connect(self.limpiarCampos)
        self.ui.btn_editar.clicked.connect(self.modificarRegion)
        self.ui.btn_eliminar.clicked.connect(self.eliminarRegion)
        self.ui.btn_buscar.clicked.connect(lambda: self.cargarDatos(1))
        self.ui.tbl_regiones.clicked.connect(self.seleccionarElemento)
        self.ui.txt_buscar.textChanged.connect(self.buscarVacio)
        self.cargarDatos(0)

    def buscarVacio(self):
        if self.ui.txt_buscar.text() == "":
            self.cargarDatos(0)

    def limpiarCampos(self):
        self.ui.txt_codigo.setText("")
        self.ui.txt_nombre_region.setText("")
        self.cargarDatos(0)
        self.ui.txt_buscar.setText("")


    def cargarDatos(self, modo):
        if modo == 1:
            texto = self.ui.txt_buscar.text()
            if texto != "":
                self.ui.tbl_regiones.clearSelection()
                listaRegiones = self.dtu.buscarRegion(texto)
            else:
                QMessageBox.warning(self, "Advertencia", "Ingrese un texto para buscar")
                return
        else:
            listaRegiones = self.dtu.listaRegiones()
        i = len(listaRegiones)
        self.ui.tbl_regiones.setRowCount(i)
        tablerow = 0
        for row in listaRegiones:
            self.ui.tbl_regiones.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row._region_id)))
            self.ui.tbl_regiones.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row._region_name))
            tablerow = tablerow + 1

    def validarVacios(self):
        if self.ui.txt_nombre_region.text() == "":
            return False
        return True

    def seleccionarElemento(self):
        try:
            fila = self.ui.tbl_regiones.selectedIndexes()[0].row()
            regiones  = self.dtu.buscarRegion(self.ui.txt_buscar.text())
            region = regiones[fila]
            self.ui.txt_codigo.setText(str(region._region_id))
            self.ui.txt_nombre_region.setText(region._region_name)

        except Exception as e:
            print(e)
        except IndexError as e:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Seleccione un elemento de la tabla")

    def agregarRegion(self):
        if self.validarVacios():
            nombre_region = self.ui.txt_nombre_region.text()
            region = regions(region_name=nombre_region)
            try:
                self.ngr.agregarRegion(region)
                self.cargarDatos(0)
                self.limpiarCampos()
            except Exception as e:
                print(f"Error al agregar region: {e}")
        else:
            print("Campos vacios")

    def modificarRegion(self):
        if self.validarVacios():
            codigo = self.ui.txt_codigo.text()
            nombre_region = self.ui.txt_nombre_region.text()
            region = regions(region_id=codigo, region_name=nombre_region)
            try:
                self.ngr.modificarRegion(region, codigo)
                self.cargarDatos(0)
                self.limpiarCampos()
            except Exception as e:
                print(f"Error al modificar region: {e}")
        else:
            print("Campos vacios")

    def eliminarRegion(self):
        if self.validarVacios():
            codigo = self.ui.txt_codigo.text()
            try:
                self.dtu.eliminarRegion(codigo)
                self.cargarDatos(0)
                self.limpiarCampos()
            except Exception as e:
                print(f"Error al eliminar region: {e}")
        else:
            print("Campos vacios")
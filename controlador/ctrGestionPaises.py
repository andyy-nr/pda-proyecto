from vistas.frmPaises import Ui_frmPaises
from datos.countries import Dt_countries
from PyQt5 import QtWidgets

class CtrlGestionPaises(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmPaises()
        self.ui.setupUi(self)
        self.initControlGui()
        self.cargarDatos()
    dtu = Dt_countries()

    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.agregarPais)
        self.cargarCombobox()
        self.cargarDatos()
        self.limpiarCampos()

    def limpiarCampos(self):
        self.ui.txt_nombre.clear()
        self.ui.txt_codigo.clear()

    def cargarDatos(self):
        listaPaises = self.dtu.listaPaises()
        i = len(listaPaises)
        self.ui.tbl_paises.setRowCount(i)
        tablerow = 0
        for row in listaPaises:
            self.ui.tbl_paises.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row._country_id))
            self.ui.tbl_paises.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row._region_name))
            self.ui.tbl_paises.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row._country_name))
            tablerow = tablerow + 1

    def cargarCombobox(self):
        try:
            listaRegiones = self.dtu.listaRegiones()
            for region in listaRegiones:
                self.ui.cbox_cod_region.addItem(str(region._region_name), str(region._region_id))
        except Exception as e:
            print(e)

    def validarVacios(self):
        if self.ui.txt_nombre.text() == "":
            return False
        if self.ui.txt_codigo.text() == "":
            return False
        return True

    def agregarPais(self):
        if self.validarVacios():
            codigo_pais = self.ui.txt_codigo.text()[:2].upper()
            nombre = self.ui.txt_nombre.text()
            region = self.ui.cbox_cod_region.currentData()
            self.dtu.agregarPais(codigo_pais, nombre, region)
            self.cargarDatos()
            self.limpiarCampos()
        else:
            print("Campos vacios")

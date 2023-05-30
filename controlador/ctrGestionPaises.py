from vistas.frmPaises import Ui_frmPaises
from datos.countries import Dt_countries
from entidades.Countries import countries
from PyQt5 import QtWidgets

class CtrlGestionPaises(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmPaises()
        self.ui.setupUi(self)
        self.initControlGui()
        self.cargarDatos(0)
        self.ui.tbl_paises.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
    dtu = Dt_countries()

    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.agregarPais)
        self.ui.btn_limpiar.clicked.connect(self.limpiarCampos)
        self.ui.btn_buscar.clicked.connect(lambda: self.cargarDatos(1))
        self.ui.tbl_paises.clicked.connect(self.seleccionarElementos)
        self.ui.txt_buscar.textChanged.connect(self.buscarVacio)
        self.cargarCombobox()
        self.cargarDatos(0)
        self.limpiarCampos()

    def buscarVacio(self):
        if self.ui.txt_buscar.text() == "":
            self.cargarDatos(0)

    def limpiarCampos(self):
        self.ui.txt_nombre.setText("")
        self.ui.txt_codigo.setText("")
        self.ui.cbox_cod_region.setCurrentIndex(0)
        self.ui.txt_buscar.setText("")
        self.cargarDatos(0)
        self.ui.tbl_paises.clearSelection()

    def cargarDatos(self, modo):
        if modo == 1: # Buscar
            texto = self.ui.txt_buscar.text()
            if texto != "":
                self.ui.tbl_paises.clearSelection()
                listaPaises = self.dtu.buscarPais(texto)
            else:
                QtWidgets.QMessageBox.warning(self, "Advertencia", "Ingrese un texto para buscar")
                return
        else: # Cargar todos los datos
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
            self.ui.cbox_cod_region.addItem("Region*")
            for region in listaRegiones:
                self.ui.cbox_cod_region.addItem(str(region._region_name), str(region._region_id))
        except Exception as e:
            print(e)

    def validarVacios(self):
        if self.ui.txt_nombre.text() == "":
            return False
        if self.ui.txt_codigo.text() == "":
            return False
        if self.ui.cbox_cod_region.currentData() is None:
            return False
        return True

    def seleccionarElementos(self):
        try:
            nombre = self.ui.txt_buscar.text()
            fila = self.ui.tbl_paises.selectedIndexes()[0].row()
            pais = self.dtu.buscarPais(nombre)
            pais_seleccionado = pais[fila]
            self.ui.txt_codigo.setText(pais_seleccionado._country_id)
            self.ui.cbox_cod_region.setCurrentText(pais_seleccionado._region_name)
            self.ui.txt_nombre.setText(pais_seleccionado._country_name)

        except IndexError as e:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Seleccione un elemento de la tabla")
        except Exception as e:
            print(e)

    def agregarPais(self):
        if self.validarVacios():
            codigo_pais = self.ui.txt_codigo.text()[:2].upper()
            nombre = self.ui.txt_nombre.text()
            region_cod = self.ui.cbox_cod_region.currentData()
            pais = countries(codigo_pais, nombre, region_cod)
            self.dtu.agregarPais(pais)
            self.cargarDatos(0)
            self.limpiarCampos()
        else:
            print("Campos vacios")

from vistas.frmLocalidades import Ui_frmLocalidades
from datos.locations import Dt_locations
from PyQt5 import QtWidgets
class CtrlGestionLocalidades(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmLocalidades()
        self.ui.setupUi(self)
        self.initControlGui()
    dtl = Dt_locations()

    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.agregarLocalidad)
        self.ui.btn_limpiar.clicked.connect(self.limpiarCampos)
        self.ui.btn_buscar.clicked.connect(lambda: self.cargarDatos(1))
        self.cargarDatos(0)
        self.cargarCombobox()

    def limpiarCampos(self):
        self.ui.txt_direccion.setText("")
        self.ui.txt_codigo.setText("")
        self.ui.txt_ciudad.setText("")
        self.ui.txt_provincia.setText("")
        self.ui.txt_cod_postal.setText("")
        self.ui.txt_buscar.setText("")
        self.ui.cbox_pais.setCurrentIndex(0)
        self.cargarDatos(0)

    def cargarDatos(self, modo):
        if modo == 1:
            texto = self.ui.txt_buscar.text()
            if texto != "":
                listaLocalidades = self.dtl.buscarLocalidad(texto)
            else:
                QtWidgets.QMessageBox.warning(self, "Advertencia", "Ingrese un texto para buscar")
                return
        else:
            listaLocalidades = self.dtl.listaLocalidades()
        i = len(listaLocalidades)
        self.ui.tbl_localidades.setRowCount(i)
        tablerow = 0
        for row in listaLocalidades:
            self.ui.tbl_localidades.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row._location_id)))
            self.ui.tbl_localidades.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row._country_id))
            self.ui.tbl_localidades.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row._postal_code))
            self.ui.tbl_localidades.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row._city))
            self.ui.tbl_localidades.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row._state_province))
            self.ui.tbl_localidades.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row._street_address))
            tablerow = tablerow + 1

    def cargarCombobox(self):
        try:
            listaCiudades = self.dtl.listaCiudades()
            self.ui.cbox_pais.addItem("Pais*")
            for ciudad in listaCiudades:
                self.ui.cbox_pais.addItem(ciudad._country_name, ciudad._country_id)
        except Exception as e:
            print(e)

    def validarVacios(self):
        if self.ui.txt_direccion.text() == "":
            return False
        if self.ui.txt_cod_postal.text() == "":
            return False
        if self.ui.txt_provincia.text() == "":
            return False
        if self.ui.txt_ciudad.text() == "":
            return False
        if self.ui.cbox_pais.currentData() is None:
            return False
        return True

    def agregarLocalidad(self):
        if self.validarVacios():
            direccion = self.ui.txt_direccion.text()
            cod_postal = self.ui.txt_cod_postal.text()
            provincia = self.ui.txt_provincia.text()
            ciudad = self.ui.txt_ciudad.text()
            pais = self.ui.cbox_pais.currentData()
            self.dtl.agregarLocalidad(direccion, cod_postal, provincia, pais, ciudad)
            self.cargarDatos()
            self.limpiarCampos()
        else:
            print("Hay campos vacios")

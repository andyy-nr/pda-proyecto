from PyQt5.QtWidgets import QTableView, QMessageBox

from vistas.frmLocalidades import Ui_frmLocalidades
from datos.locations import Dt_locations
from negocio.ngLocalidades import ngLocalidades
from PyQt5 import QtWidgets
from entidades.Locations import locations

class CtrlGestionLocalidades(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmLocalidades()
        self.ui.setupUi(self)
        self.initControlGui()
        self.ui.tbl_localidades.setSelectionBehavior(QTableView.SelectRows)
    dtl = Dt_locations()
    ngl = ngLocalidades()

    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.agregarLocalidad)
        self.ui.btn_limpiar.clicked.connect(self.limpiarCampos)
        self.ui.btn_editar.clicked.connect(self.modificarLocalidad)
        self.ui.btn_eliminar.clicked.connect(self.eliminarLocalidad)
        self.ui.btn_buscar.clicked.connect(lambda: self.cargarDatos(1))
        self.ui.tbl_localidades.clicked.connect(self.seleccionarElemento)
        self.ui.txt_buscar.textChanged.connect(self.buscarVacio)
        self.cargarDatos(0)
        self.cargarCombobox()

    def buscarVacio(self):
        if self.ui.txt_buscar.text() == "":
            self.cargarDatos(0)

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
                self.ui.tbl_localidades.clearSelection()
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
            self.ui.tbl_localidades.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row._country_name))
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
        if self.ui.txt_ciudad.text() == "":
            return False
        if self.ui.cbox_pais.currentData() is None:
            return False
        return True

    def seleccionarElemento(self):
        try:
            fila = self.ui.tbl_localidades.selectedIndexes()[0].row()
            localidades = self.dtl.listaLocalidades()
            localidad = localidades[fila]
            self.ui.txt_codigo.setText(str(localidad._location_id))
            self.ui.txt_direccion.setText(localidad._street_address)
            self.ui.txt_cod_postal.setText(localidad._postal_code)
            self.ui.txt_provincia.setText(localidad._state_province)
            self.ui.txt_ciudad.setText(localidad._city)
            self.ui.cbox_pais.setCurrentText(str(localidad._country_name))
            return localidad
        except IndexError as e:
            QMessageBox.warning(self, "Advertencia", "Seleccione un elemento de la tabla")
        except Exception as e:
            print(e)

    def agregarLocalidad(self):
        if self.validarVacios():
            direccion = self.ui.txt_direccion.text()
            cod_postal = self.ui.txt_cod_postal.text()
            provincia = self.ui.txt_provincia.text()
            ciudad = self.ui.txt_ciudad.text()
            pais = self.ui.cbox_pais.currentData()
            localidad = locations(street_address=direccion, postal_code=cod_postal, state_province=provincia,
                                  city=ciudad, country_id=pais)
            self.ngl.agregarLocalidad(localidad)
            self.cargarDatos(0)
            self.limpiarCampos()
        else:
            print("Hay campos vacios")

    def modificarLocalidad(self):
        if self.validarVacios():
            direccion = self.ui.txt_direccion.text()
            cod_postal = self.ui.txt_cod_postal.text()
            provincia = self.ui.txt_provincia.text()
            ciudad = self.ui.txt_ciudad.text()
            pais = self.ui.cbox_pais.currentData()
            codigo = self.ui.txt_codigo.text()
            localidad = locations(location_id=codigo, street_address=direccion, postal_code=cod_postal,
                                  state_province=provincia, city=ciudad, country_id=pais)
            self.ngl.modificarLocalidad(localidad, localidad.location_id)
            self.cargarDatos(0)
            self.limpiarCampos()
            self.ui.tbl_localidades.clearSelection()


    def eliminarLocalidad(self):
        localidad = self.seleccionarElemento()
        if localidad is not None:
            self.dtl.eliminarLocalidad(localidad)
            self.cargarDatos(0)
            self.limpiarCampos()
            self.ui.tbl_localidades.clearSelection()
        else:
            QMessageBox.warning(self, "Advertencia", "Seleccione un elemento de la tabla")


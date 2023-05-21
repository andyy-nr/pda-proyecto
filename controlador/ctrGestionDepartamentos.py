from vistas.frmDepartamentos import Ui_frmDepartamentos
from datos.departments import Dt_departments
from PyQt5 import QtWidgets

class CtrlGestionDepartaments(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmDepartamentos()
        self.ui.setupUi(self)
        self.initControlGui()
    dtd = Dt_departments()

    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.agregarDepartamento)
        self.cargarDatos()
        self.cargarCombobox()

    def limpiarCampos(self):
        self.ui.txt_nombre.setText("")
        self.ui.cbox_cod_localidad.placeholderText("Localidad")

    def cargarDatos(self):
        listaDepartamentos = self.dtd.listaDepartamentos()
        i = len(listaDepartamentos)
        self.ui.tbl_departamentos.setRowCount(i)
        tablerow = 0
        for row in listaDepartamentos:
            self.ui.tbl_departamentos.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row._department_id)))
            self.ui.tbl_departamentos.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row._location_name))
            self.ui.tbl_departamentos.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row._department_name))
            tablerow = tablerow + 1

    def cargarCombobox(self):
        try:
            listaLocalidades = self.dtd.listaLocalidades()
            for localidad in listaLocalidades:
                self.ui.cbox_cod_localidad.addItem(str(localidad._location_name), int(localidad._location_id))
        except Exception as e:
            print(e)

    def validarVacios(self):
        if self.ui.txt_nombre.text() == "":
            return False
        return True

    def agregarDepartamento(self):
        if self.validarVacios():
            nombre = self.ui.txt_nombre.text()
            localidad = self.ui.cbox_cod_localidad.currentData()
            print(localidad)
            self.dtd.agregarDepartamento(nombre, localidad)
            self.limpiarCampos()
            self.cargarDatos()
        else:
            print("Campos vacios")
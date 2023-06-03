from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMessageBox, QTableView

from vistas.frmDepartamentos import Ui_frmDepartamentos
from datos.departments import Dt_departments
from entidades.Departments import departments
from negocio.ngDepartamentos import ngDepartamentos
from PyQt5 import QtWidgets

class CtrlGestionDepartaments(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmDepartamentos()
        self.ui.setupUi(self)
        self.initControlGui()
        self.ui.tbl_departamentos.setSelectionBehavior(QTableView.SelectRows)
    dtd = Dt_departments()
    ngd = ngDepartamentos()
    actualizar_info = pyqtSignal()

    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.agregarDepartamento)
        self.ui.btn_limpiar.clicked.connect(self.limpiarCampos)
        self.ui.btn_buscar.clicked.connect(lambda : self.cargarDatos(1))
        self.ui.btn_editar.clicked.connect(self.modificarDepartamento)
        self.ui.btn_eliminar.clicked.connect(self.eliminarDepartamento)
        self.ui.tbl_departamentos.clicked.connect(self.seleccionarElemento)
        self.ui.txt_buscar.textChanged.connect(self.buscarVacio)
        self.cargarDatos(0)
        self.cargarCombobox()

    def buscarVacio(self):
        if self.ui.txt_buscar.text() == "":
            self.cargarDatos(0)

    def limpiarCampos(self):
        self.ui.txt_codigo.setText("")
        self.ui.txt_nombre.setText("")
        self.ui.cbox_cod_localidad.setCurrentIndex(0)
        self.ui.txt_buscar.setText("")
        self.cargarDatos(0)

    def cargarDatos(self, modo):
        if modo == 1:
            texto = self.ui.txt_buscar.text()
            if texto != "":
                self.ui.tbl_departamentos.clearSelection()
                listaDepartamentos = self.dtd.buscarDepartamento(texto)
            else:
                QMessageBox.warning(self, "Advertencia", "Ingrese un texto para buscar")
                return
        else:
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
            self.ui.cbox_cod_localidad.addItem("Localidad")
            for localidad in listaLocalidades:
                self.ui.cbox_cod_localidad.addItem(str(localidad._location_name), int(localidad._location_id))
        except Exception as e:
            print(e)

    def validarVacios(self):
        if self.ui.txt_nombre.text() == "":
            return False
        if self.ui.cbox_cod_localidad.currentData() == None:
            return False
        return True

    def seleccionarElemento(self):
        try:
            fila = self.ui.tbl_departamentos.selectedIndexes()[0].row()
            departamento = self.dtd.buscarDepartamento(self.ui.txt_buscar.text())
            dep_seleccionado = departamento[fila]
            self.ui.txt_codigo.setText(str(dep_seleccionado._department_id))
            self.ui.txt_nombre.setText(dep_seleccionado._department_name)
            self.ui.cbox_cod_localidad.setCurrentText(dep_seleccionado._location_name)
        except Exception as e:
            print(e)
        except IndexError as e:
            QMessageBox.warning(self, "Advertencia", "Seleccione un elemento de la tabla")


    def agregarDepartamento(self):
        if self.validarVacios():
            nombre = self.ui.txt_nombre.text()
            localidad = self.ui.cbox_cod_localidad.currentData()
            departamento = departments(department_name=nombre, location_id=localidad)
            self.ngd.agregarDepartamento(departamento)
            self.limpiarCampos()
            self.cargarDatos(0)
            self.actualizar_info.emit()

    def modificarDepartamento(self):
        if self.validarVacios():
            id = self.ui.txt_codigo.text()
            nombre = self.ui.txt_nombre.text()
            localidad = self.ui.cbox_cod_localidad.currentData()
            departamento = departments(department_id=id, department_name=nombre, location_id=localidad)
            self.ngd.modificarDepartamento(departamento)
            self.limpiarCampos()
            self.cargarDatos(0)
            self.ui.tbl_departamentos.clearSelection()

    def eliminarDepartamento(self):
        try:
            fila = self.ui.tbl_departamentos.selectedIndexes()[0].row()
            departamento = self.dtd.buscarDepartamento(self.ui.txt_buscar.text())
            dep_seleccionado = departamento[fila]
            self.dtd.eliminarDepartamento(dep_seleccionado)
            self.limpiarCampos()
            self.cargarDatos(0)
            self.ui.tbl_departamentos.clearSelection()
        except Exception as e:
            print(e)
        except IndexError as e:
            QMessageBox.warning(self, "Advertencia", "Seleccione un elemento de la tabla")

from vistas.frmDependientes import Ui_frmDependientes
from datos.dependents import Dt_dependents
from PyQt5 import QtWidgets

class CtrlGestionDependientes( QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmDependientes()
        self.ui.setupUi(self)
        self.initControlGUi()


    dd = Dt_dependents()

    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.agregarOpcion)
        self.cargarDatos()

    def limpiarCampos(self):
        self.ui.txt_codigo.setText("")
        self.ui.txt_nombres.setText("")
        self.ui.txt_apellidos.setText("")
        self.ui.txt_relacion.setText("")
        self.ui.txt_empleados.setText("")

    def cargarDatos(self):
        listaDependientes = self.dd.listaDependents()
        i = len(listaDependientes)
        self.ui.tbl_dependientes.setRowCount(i)
        tablerow = 0

        for row in listaDependientes:
            self.ui.tbl_dependientes.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row._dependent_id)))
            self.ui.tbl_dependientes.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row._first_name))
            self.ui.tbl_dependientes.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row._last_name))
            self.ui.tbl_dependientes.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row._relationship))
            self.ui.tbl_dependientes.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row._employee))
            tablerow = tablerow + 1

    def validarVacio(self):
        if self.ui.txt_nombres.text() == "":
            return False
        if self.ui.txt_relacion.text() == "":
            return False
        if self.ui.txt_apellidos.text() == "":
            return False 
        if self.ui.txt_empleados.text() == "":
            return False

        return True

    def agregarDependiente(self):
        if self.validarVacio():
            nombres = self.ui.txt_nombres.text()
            apellidos = self.ui.txt_apellidos.text()
            relacion = self.ui.txt_relacion.text()
            empleado = self.ui.txt_empleados.text()

            try:
                self.dd.agregarDependientes(nombres, apellidos, relacion, empleado)
                self.cargarDatos()
                self.limpiarCampos()
            except Exception as e:
                print(f"Error al agregar dependiente: {e}")
        else:
            print("Campos vacios")
from vistas.frmEmpleados import Ui_frmEmpleados
from datos.employees import Dt_employees
from PyQt5 import QtWidgets


class CtrlGestionEmpleados(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmEmpleados()
        self.ui.setupUi(self)
        self.initControlGui()
    dtu = Dt_employees()

    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.limpiarCampos)
        self.cargarDatos()

    def limpiarCampos(self):
        self.ui.txt_telefono.setText("")
        self.ui.txt_correo.setText("")
        self.ui.txt_salario.setText("")
        self.ui.txt_nombres.setText("")
        self.ui.txt_apellidos.setText("")


    def cargarDatos(self):
        listaEmpleados = self.dtu.listaEmpleados()
        i = len(listaEmpleados)
        self.ui.tbl_employees.setRowCount(i)
        tablerow = 0
        for row in listaEmpleados:
            self.ui.tbl_employees.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row._first_name))
            self.ui.tbl_employees.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row._last_name))
            self.ui.tbl_employees.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row._email))
            self.ui.tbl_employees.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row._phone))
            self.ui.tbl_employees.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row._hire_date)))
            self.ui.tbl_employees.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row._job_id)))
            self.ui.tbl_employees.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row._salary)))
            self.ui.tbl_employees.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row._manager_id)))
            self.ui.tbl_employees.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(row._department_id)))
            tablerow = tablerow + 1
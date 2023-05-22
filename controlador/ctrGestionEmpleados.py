from vistas.frmEmpleados import Ui_frmEmpleados
from datos.employees import Dt_employees
import datetime
from PyQt5 import QtWidgets


class CtrlGestionEmpleados(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmEmpleados()
        self.ui.setupUi(self)
        self.initControlGui()
    dtu = Dt_employees()

    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.agregarEmpleado)
        self.ui.btn_limpiar.clicked.connect(self.limpiarCampos)
        self.cargarDatos()
        self.cargarCombobox()

    def limpiarCampos(self):
        self.ui.txt_telefono.setText("")
        self.ui.txt_correo.setText("")
        self.ui.txt_salario.setText("")
        self.ui.txt_nombres.setText("")
        self.ui.txt_apellidos.setText("")
        self.ui.cbox_trabajo.setCurrentIndex(0)
        self.ui.cbox_departamento.setCurrentIndex(0)
        self.ui.cbox_gerente.setCurrentIndex(0)


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
            self.ui.tbl_employees.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row._job_title)))
            self.ui.tbl_employees.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row._salary)))
            self.ui.tbl_employees.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row._manager)))
            self.ui.tbl_employees.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(row._department_name)))
            tablerow = tablerow + 1

    def cargarCombobox(self):
        try:
            listaManagers = self.dtu.listaManagers()
            self.ui.cbox_gerente.addItem("Gerente*")
            for manager in listaManagers:
                self.ui.cbox_gerente.addItem(str(manager._manager), int(manager._employee_id))

            listaDepartamentos = self.dtu.listaDepartamentos()
            self.ui.cbox_departamento.addItem("Departamento*")
            for departamento in listaDepartamentos:
                self.ui.cbox_departamento.addItem(str(departamento._department_name), int(departamento._department_id))

            listaTrabajos = self.dtu.listaTrabajos()
            self.ui.cbox_trabajo.addItem("Trabajo*")
            for trabajo in listaTrabajos:
                self.ui.cbox_trabajo.addItem(str(trabajo._job_title), int(trabajo._job_id))
        except Exception as e:
            print(e)

    def validarVacios(self):
        if self.ui.txt_nombres.text() == "":
            return False
        if self.ui.txt_apellidos.text() == "":
            return False
        if self.ui.txt_salario.text() == "":
            return False
        if self.ui.txt_correo.text() == "":
            return False
        if self.ui.txt_telefono.text() == "":
            return False
        if self.ui.cbox_gerente.currentData() is None:
            return False
        if self.ui.cbox_departamento.currentData() is None:
            return False
        if self.ui.cbox_trabajo.currentData() is None:
            return False
        return True

    def agregarEmpleado(self):
        if self.validarVacios():
            nombre = self.ui.txt_nombres.text()
            apellido = self.ui.txt_apellidos.text()
            salario = self.ui.txt_salario.text()
            correo = self.ui.txt_correo.text()
            telefono = self.ui.txt_telefono.text()
            fecha = self.ui.date_fecha_contratacion.date().toPyDate()
            gerente = self.ui.cbox_gerente.currentData()
            departamento = self.ui.cbox_departamento.currentData()
            trabajo = self.ui.cbox_trabajo.currentData()
            self.dtu.agregarEmpleado(nombre, apellido, correo, telefono, fecha, trabajo, salario, gerente, departamento)
            self.cargarDatos()
            self.limpiarCampos()
        else:
            print("Campos vacios")

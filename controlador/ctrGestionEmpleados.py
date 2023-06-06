from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QMessageBox, QTableView

from vistas.frmEmpleados import Ui_frmEmpleados
from datos.employees import Dt_employees
import datetime
from PyQt5 import QtWidgets, QtCore
from entidades.Employees import employee
from negocio.ngEmpleados import ngEmpleados


class CtrlGestionEmpleados(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmEmpleados()
        self.ui.setupUi(self)
        self.initControlGui()
        self.ui.tbl_employees.setSelectionBehavior(QTableView.SelectRows)
    dtu = Dt_employees()
    nge = ngEmpleados()
    actualizar_info = pyqtSignal()

    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.agregarEmpleado)
        self.ui.btn_limpiar.clicked.connect(self.limpiarCampos)
        self.ui.tbl_employees.clicked.connect(self.seleccionarElemento)
        self.ui.btn_eliminar.clicked.connect(self.eliminarEmpleado)
        self.ui.btn_editar.clicked.connect(self.editarEmpleado)
        self.ui.btn_buscar.clicked.connect(lambda: self.cargarDatos(1))
        self.ui.txt_buscar.textChanged.connect(self.buscarVacio)
        self.cargarDatos(0)
        self.cargarCombobox()

    def buscarVacio(self):
        if self.ui.txt_buscar.text() == "":
            self.cargarDatos(0)

    def limpiarCampos(self):
        self.ui.txt_telefono.setText("")
        self.ui.txt_correo.setText("")
        self.ui.txt_salario.setText("")
        self.ui.txt_nombres.setText("")
        self.ui.txt_apellidos.setText("")
        self.ui.cbox_trabajo.setCurrentIndex(0)
        self.ui.cbox_departamento.setCurrentIndex(0)
        self.ui.cbox_gerente.setCurrentIndex(0)
        self.ui.date_fecha_contratacion.setDate(datetime.datetime.now())
        self.ui.tbl_employees.clearSelection()
        self.ui.txt_buscar.setText("")
        self.cargarDatos(0)


    def cargarDatos(self, modo):
        if modo == 1:
            texto = self.ui.txt_buscar.text()
            if texto != "":
                self.ui.tbl_employees.clearSelection()
                listaEmpleados = self.dtu.buscarEmpleado(texto)
            else:
                QtWidgets.QMessageBox.warning(self, "Advertencia", "Ingrese un texto para buscar")
                return
        else:
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
                self.ui.cbox_gerente.addItem(str(manager._manager), int(manager.manager_id))

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
            fecha = self.ui.date_fecha_contratacion.date()
            gerente = self.ui.cbox_gerente.currentData()
            departamento = self.ui.cbox_departamento.currentData()
            trabajo = self.ui.cbox_trabajo.currentData()
            empleado = employee(nombre, apellido, correo, telefono, fecha, job_id=trabajo, salary=salario,
                                manager_id=gerente, department_id=departamento)
            self.nge.agregarEmpleado(empleado)
            self.cargarDatos(0)
            self.limpiarCampos()
            self.actualizar_info.emit()

        else:
            print("Campos vacios")

    def seleccionarElemento(self):
        try:
            fila = self.ui.tbl_employees.currentRow()
            empleados = self.dtu.buscarEmpleado(self.ui.txt_buscar.text())
            emp_seleccionado = empleados[fila]
            self.ui.txt_nombres.setText(emp_seleccionado._first_name)
            self.ui.txt_apellidos.setText(emp_seleccionado._last_name)
            self.ui.txt_correo.setText(emp_seleccionado._email)
            self.ui.txt_telefono.setText(emp_seleccionado._phone)
            self.ui.txt_salario.setText(str(emp_seleccionado._salary))
            self.ui.date_fecha_contratacion.setDate(emp_seleccionado._hire_date)
            self.ui.cbox_trabajo.setCurrentText(emp_seleccionado._job_title)
            self.ui.cbox_departamento.setCurrentText(emp_seleccionado._department_name)
            self.ui.cbox_gerente.setCurrentText(emp_seleccionado._manager)
            return emp_seleccionado
        except IndexError as e:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Seleccione un elemento de la tabla")
            return None

    def eliminarEmpleado(self):
        empleado = self.seleccionarElemento()
        if empleado is not None:
            self.dtu.eliminarEmpleado(empleado)
            self.cargarDatos(0)
            self.limpiarCampos()

    def editarEmpleado(self):
       try:
            fila = self.ui.tbl_employees.selectedIndexes()[0].row()
            empleados = self.dtu.listaEmpleados()
            emp_id= empleados[fila]._employee_id
            nombre = self.ui.txt_nombres.text()
            apellido = self.ui.txt_apellidos.text()
            salario = self.ui.txt_salario.text()
            correo = self.ui.txt_correo.text()
            telefono = self.ui.txt_telefono.text()
            fecha = self.ui.date_fecha_contratacion.date().toPyDate()
            gerente = self.ui.cbox_gerente.currentData()
            departamento = self.ui.cbox_departamento.currentData()
            trabajo = self.ui.cbox_trabajo.currentData()
            emp_nuevo = employee(first_name=nombre, last_name=apellido, email=correo, phone=telefono, hire_date=fecha,
                                 job_id=trabajo, salary=salario, manager_id=gerente, department_id=departamento)
            self.nge.modificarEmpleado(emp_nuevo, emp_id)
            self.cargarDatos(0)
            self.limpiarCampos()
       except Exception as e:
           print(f"Error al editar empleado: {e}")

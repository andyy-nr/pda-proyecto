from PyQt5.QtWidgets import QWidget, QMessageBox

from datos.employees import Dt_employees
from entidades.Employees import employee

class ngEmpleados:
    def __init__(self):
        self.empleado = employee()
    de = Dt_employees()

    def validarRepetido(self, empleado, emp_id=None):
        empleados = self.de.listaEmpleados()
        if emp_id == None:
            for emp in empleados:
                if emp._employee_id == empleado._employee_id:
                    return False
                if emp._first_name == empleado._first_name:
                    return False
                if emp._last_name == empleado._last_name:
                    return False
                if emp._email == empleado._email:
                    return False
                if emp._phone_number == empleado._phone_number:
                    return False
        else:
            for emp in empleados:
                if emp._employee_id != empleado._employee_id:
                    if emp._first_name == empleado._first_name:
                        return False
                    if emp._last_name == empleado._last_name:
                        return False
                    if emp._email == empleado._email:
                        return False
                    if emp._phone_number == empleado._phone_number:
                        return False
        return True

    def validarSalario(self, empleado):
        salarios = self.de.salarioMinYMax(empleado)
        widget = QWidget()
        if salarios._min_salary > empleado._salary:
            QMessageBox.warning(widget, "Error", "El salario no puede ser menor al salario mínimo del puesto")
            return False
        if salarios._max_salary < empleado._salary:
            QMessageBox.warning(widget, "Error", "El salario no puede ser mayor al salario máximo del puesto")
            return False
        return True

    def agregarEmpleado(self, empleado):
        if not self.validarRepetido(empleado):
            return False
        if not self.validarSalario(empleado):
            return False
        self.de.agregarEmpleado(empleado)

    def modificarEmpleado(self, empleado, emp_id):
        if not self.validarRepetido(empleado, emp_id):
            return False
        if not self.validarSalario(empleado):
            return False
        self.de.editarEmpleado(empleado, emp_id)

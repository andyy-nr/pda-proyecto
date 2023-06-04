from datos.employees import Dt_employees
from entidades.Employees import employee

class ngEmpleados:
    def __init__(self):
        self.empleado = employee()

    de = Dt_employees()

    def validarRepetido(self, empleado):
        empleados = self.de.listaEmpleados()
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
        return True

    def agregarEmpleado(self, empleado):
        if not self.validarRepetido(empleado):
            return False
        self.de.agregarEmpleado(empleado)

    def modificarEmpleado(self, empleado):
        if not self.validarRepetido(empleado):
            return False
        self.de.editarEmpleado(empleado)

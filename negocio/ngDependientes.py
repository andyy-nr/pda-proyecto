# nombre y empleado repetido
from datos.dependents import Dt_dependents
from entidades.Dependents import dependents

class ngDependientes:
    def __init__(self):
        self.dependiente = dependents()
    dd = Dt_dependents()

    def validarRepetido(self, dependiente):
        dependientes = self.dd.listaDependientes()
        for dep in dependientes:
            if dep._first_name == dependiente._first_name:
                return False
            if dep._last_name == dependiente._last_name:
                return False
            if dep._relationship == dependiente._relationship:
                return False
            if dep._employee_id == dependiente._employee_id:
                return False
            return True

    def agregarDependientes(self, dependiente):
        if not self.validarRepetido(dependiente):
            return False
        self.dd.agregarDependientes(dependiente)

    def modificarDependiente(self, dependiente):
        if not self.validarRepetido(dependiente):
            return False
        self.dd.modificarDependientes(dependiente)

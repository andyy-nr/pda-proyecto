# nombre y empleado repetido
from datos.dependents import Dt_dependents
from entidades.Dependents import dependents

class ngDependientes:
    def __init__(self):
        self.dependiente = dependents()
    dd = Dt_dependents()

    def validarRepetido(self, dependiente, dep_id=None):
        dependientes = self.dd.listaDependents()
        if dep_id is None:
            for dep in dependientes:
                if (dep._first_name == dependiente._first_name and
                        dep._last_name == dependiente._last_name and
                        dep._relationship == dependiente._relationship and
                        dep._employee_id == dependiente._employee_id):
                    return False
        else:
            for dep in dependientes:
                if dep_id != dep._dependent_id:
                    if  (dep._first_name == dependiente._first_name and
                            dep._last_name == dependiente._last_name and
                            dep._relationship == dependiente._relationship and
                            dep._employee_id == dependiente._employee_id):
                        return False
        return True

    def agregarDependientes(self, dependiente):
        if not self.validarRepetido(dependiente):
            return False
        self.dd.agregarDependientes(dependiente)

    def modificarDependiente(self, dependiente, dep_id):
        if not self.validarRepetido(dependiente, dep_id):
            return False
        self.dd.modificarDependientes(dependiente, dep_id)

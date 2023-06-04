from datos.departments import Dt_departments
from entidades.Departments import departments

class ngDepartamentos:
    def __init__(self):
        self.departamento = departments()
    dd = Dt_departments()

    def validarNombre(self, departamento, dep_id = None):
        departamentos = self.dd.listaDepartamentos()
        if dep_id is None:
            for dep in departamentos:
                if dep.department_name == departamento._department_name:
                    return False
        else:
            for dep in departamentos:
                if not dep_id == departamento._department_id:
                    if dep.department_name == departamento._department_name:
                        return False
        return True

    def agregarDepartamento(self, departamento):
        if not self.validarNombre(departamento):
            return False
        self.dd.agregarDepartamento(departamento)

    def modificarDepartamento(self, departamento):
        if not self.validarNombre(departamento):
            return False
        self.dd.modificarDepartamento(departamento)




from PyQt5.QtWidgets import QMessageBox, QWidget

from entidades.Jobs import jobs
from datos.jobs import Dt_jobs

class ngTrabajo:
    def __init__(self):
        self.trabajo = jobs()
    dj = Dt_jobs()

    def validarSalario(self, trabajo):
        widget = QWidget()
        if trabajo._min_salary > trabajo._max_salary:
            QMessageBox.warning(widget, "Error", "El salario mínimo no puede ser mayor al salario máximo")
            return False
        return True

    def validarNombre(self, trabajo, job_id=None):
        trabajos = self.dj.listaTrabajos()
        if job_id is None:
            for tj in trabajos:
                if tj.job_title == trabajo._job_title:
                    return False
        else:
            for tj in trabajos:
                if job_id == tj._job_id and tj.job_title == trabajo._job_title:
                        return False
        return True

    def agregarTrabajo(self, trabajo):
        if not self.validarNombre(trabajo):
            return False
        if not self.validarSalario(trabajo):
            return False
        self.dj.agregarTrabajo(trabajo)

    def modificarTrabajo(self, trabajo, job_id):
        if not self.validarNombre(trabajo, job_id):
            return False
        if not self.validarSalario(trabajo):
            return False
        self.dj.modificarTrabajo(trabajo)

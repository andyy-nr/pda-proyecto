from entidades.Jobs import jobs
from datos.jobs import Dt_jobs

class ngTrabajo:
    def __init__(self):
        self.trabajo = jobs()
    dj = Dt_jobs()

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
        self.dj.agregarTrabajo(trabajo)

    def modificarTrabajo(self, trabajo, job_id):
        if not self.validarNombre(trabajo, job_id):
            return False
        self.dj.modificarTrabajo(trabajo)

# salario min no mayor q sal max
# nombre repetido
from datos.jobs import Dt_jobs
from entidades.Jobs import jobs

class ngJobs:
    def __init__(self):
        self.job = jobs()
    dtj = Dt_jobs()

    def validarNombreRepetido(self, job, job_id=None):
        jobs = self.dtj.listaTrabajos()
        if job_id is None:
            for jb in jobs:
                if jb._job_title == job._job_title:
                    return False
        else:
            for jb in jobs:
                if jb._job_id != job_id:
                    if jb._job_title == job._job_title:
                        return False
        return True

    def salarioMinMenorSalarioMax(self, job):
        if job._min_salary > job._max_salary:
            return False
        return True

    def agregarJob(self, job):
        if not self.validarNombreRepetido(job):
            return False
        if self.salarioMinMenorSalarioMax(job):
            return False
        self.dtj.agregarTrabajo(job)


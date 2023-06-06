from datos.Conexion import Conexion
from entidades.Jobs import jobs
from PyQt5.QtWidgets import QMessageBox
import decimal

class Dt_jobs:
    def __init__(self):
        self._con = None
        self._cursor = None
        self._sql = ""

    def renovarConexion(self):
        self._con = Conexion.getConnection()
        self._cursor = Conexion.getCursor()

    def listaTrabajos(self):
        self.renovarConexion()
        self._sql = "SELECT * FROM Seguridad.jobs where estado <> 3;"
        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            listaTrabajos = []

            for tj in registros:
                tjs = jobs(tj['job_id'], tj['job_title'], tj['min_salary'], tj['max_salary'])
                listaTrabajos.append(tjs)
            return listaTrabajos
        except Exception as e:
            print("Datos: Error listaTrabajos()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def buscarTrabajo(self, trabajo):
        self.renovarConexion()
        self._sql = "SELECT * FROM Seguridad.jobs WHERE job_title like '%{}%';".format(trabajo)
        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            listaTrabajos = []

            for tj in registros:
                tjs = jobs(tj['job_id'], tj['job_title'], tj['min_salary'], tj['max_salary'])
                listaTrabajos.append(tjs)
            return listaTrabajos
        except Exception as e:
            print("Datos: Error buscarTrabajo()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def agregarTrabajo(self, trabajo):
        self.renovarConexion()
        self._sql = f"INSERT INTO Seguridad.jobs (job_title, min_salary, max_salary) " \
                    "VALUES ('{}', '{}', '{}');".format(trabajo.job_title, trabajo.min_salary, trabajo.max_salary)
        try:
            self._cursor.execute(self._sql)
            self._con.commit()
        except Exception as e:
            print("Datos: Error agregarTrabajo()", e)
            QMessageBox.warning(self, "Agregar Trabajo", f"Error al agregar Trabajo, {e}", QMessageBox.Abort)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def modificarTrabajo(self, trabajo):
        self.renovarConexion()
        self._sql = "UPDATE Seguridad.jobs SET job_title = '{}', min_salary = '{}', max_salary = '{}' WHERE job_id = '{}';".format(trabajo.job_title, trabajo.min_salary, trabajo.max_salary, trabajo.job_id)
        try:
            self._cursor.execute(self._sql)
            self._con.commit()
        except Exception as e:
            print("Datos: Error modificarTrabajo()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def eliminarTrabajo(self, trabajo):
        self.renovarConexion()
        self._sql = f"UPDATE Seguridad.jobs SET estado = 3 WHERE job_id = '{trabajo.job_id}';"
        try:
            self._cursor.execute(self._sql)
            self._con.commit()
        except Exception as e:
            print("Datos: Error eliminarTrabajo()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

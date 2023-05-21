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
        self._sql = "SELECT * FROM Seguridad.jobs;"
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

    def agregarTrabajo(self, id_trabajo, nombre_trabajo, salario_maximo, salario_minimo):
        self.renovarConexion()
        trabajo = [id_trabajo, nombre_trabajo, salario_maximo, salario_minimo]
        self._sql = f"INSERT INTO Seguridad.jobs (job_id, job_title, min_salary, max_salary) " \
                    "VALUES (%s, %s, %s, %s);"
        try:
            self._cursor.execute(self._sql, trabajo)
            self._con.commit()
            QMessageBox.information(None, "Agregar Trabajo", "Trabajo agregado correctamente")
        except Exception as e:
            print("Datos: Error agregarTrabajo()", e)
            QMessageBox.warning(None, "Agregar Trabajo", f"Error al agregar Trabajo, {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
import pymysql

from datos.Conexion import Conexion
from entidades.Employees import employee


class Dt_employees:
    def __init__(self):
        self._con = None
        self._cursor = None
        self._sql = ""

    def renovarConexion(self):
        self._con = Conexion.getConnection()
        self._cursor = Conexion.getCursor()

    def listaEmpleados(self):
        self.renovarConexion()
        self._sql = "SELECT * FROM Seguridad.employees;"
        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            print("Numero total de registros: ", self._cursor.rowcount)
            listaEmpleados = []

            for tu in registros:
                tus = employee(tu['employee_id'], tu['first_name'], tu['last_name'], tu['email'],
                            tu['phone_number'], tu['hire_date'], tu['job_id'],
                            tu['salary'], tu['manager_id'], tu['department_id'])
                listaEmpleados.append(tus)
            print('listaEmpleados[]', listaEmpleados)
            return listaEmpleados

        except Exception as e:
            print("Datos: Error listaEmpleados()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
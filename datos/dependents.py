import pymysql
from datos.Conexion import Conexion
from entidades.Dependents import dependents

class Dt_dependents:
    def __init__(self):
        self._con = None
        self._cursor = None
        self._sql = ""

    def renovarConexion(self):
        self._con = Conexion.getConnection()
        self._cursor = Conexion.getCursor()

    def totalDependents(self):
        self.renovarConexion()
        self._sql = "SELECT * FROM Seguridad.dependents;"
        try:
            self._cursor.execute(self._sql)
            return(str(self._cursor.rowcount))
        except Exception as e:
            print("Datos: Error totalDependents()", e)

    def listaDependents(self):
        self.renovarConexion()
        self._sql = "select * from Seguridad.dependents;"

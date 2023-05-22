from entidades.Regions import regions
from datos.Conexion import Conexion

class Dt_Regions:
    def __init__(self):
        self._con = None
        self._cursor = None
        self._sql = ""

    def renovarConexion(self):
        self._con = Conexion.getConnection()
        self._cursor = Conexion.getCursor()

    def listaRegiones(self):
        self.renovarConexion()
        self._sql = "SELECT * FROM Seguridad.regions;"
        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            listaRegiones = []

            for tu in registros:
                tus = regions(tu['region_id'], tu['region_name'])
                listaRegiones.append(tus)
            return listaRegiones

        except Exception as e:
            print("Datos: Error listaEmpleados()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def agregarRegion(self, nombre_region):
        self.renovarConexion()
        self._sql = "INSERT INTO Seguridad.regions(region_name) VALUES (%s);"
        try:
            self._cursor.execute(self._sql, nombre_region)
            self._con.commit()
        except Exception as e:
            print("Datos: Error agregarRegion()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

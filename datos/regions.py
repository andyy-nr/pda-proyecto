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

    def buscarRegion(self, texto):
        self.renovarConexion()
        self._sql = "SELECT * FROM Seguridad.regions WHERE region_name LIKE '%{}%';".format(texto)
        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            listaRegiones = []

            for tu in registros:
                tus = regions(tu['region_id'], tu['region_name'])
                listaRegiones.append(tus)
            return listaRegiones
        except Exception as e:
            print("Datos: Error buscarRegion()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()


    def agregarRegion(self, region):
        self.renovarConexion()
        self._sql = "INSERT INTO Seguridad.regions(region_name) VALUES ({});".format(region._region_name)
        try:
            self._cursor.execute(self._sql)
            self._con.commit()
        except Exception as e:
            print("Datos: Error agregarRegion()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def modificarRegion(self, region, reg_id):
        self.renovarConexion()
        self._sql = "UPDATE Seguridad.regions SET region_name = '{}' WHERE region_id = {};".format(region._region_name, reg_id)
        try:
            self._cursor.execute(self._sql)
            self._con.commit()
        except Exception as e:
            print("Datos: Error modificarRegion()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def eliminarRegion(self, reg_id):
        self.renovarConexion()
        self._sql = "UPDATE FROM Seguridad.regions SET estado = '3' WHERE region_id = {};".format(reg_id)
        try:
            self._cursor.execute(self._sql)
            self._con.commit()
        except Exception as e:
            print("Datos: Error eliminarRegion()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

import pymysql
from datos.Conexion import Conexion
from entidades.Tbl_rol import Tbl_rol

class Dt_tbl_rol:
    def __init__(self):
        self._con = None
        self._cursor = None
        self._sql = ""

    def renovarConexion(self):
        self._con = Conexion.getConnection()
        self._cursor = Conexion.getCursor()

    def listaRoles(self):
        self.renovarConexion()
        self._sql = "Select * from Seguridad.tbl_rol;"
        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            listaRoles =  []
            for tr in registros:
                trs = Tbl_rol(tr['id_rol'], tr['rol'], tr['estado'])
                listaRoles.append(trs)
            return listaRoles
        except Exception as e:
            print("Datos: Error listaRoles()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def agregarRol(self, rol, estado):
        self.renovarConexion()
        rol = [rol, estado]
        self._sql = "INSERT INTO Seguridad.tbl_rol (rol, estado) " \
                    "values (%s, %s);"
        try:
            self._cursor.execute(self._sql, rol)
            self._con.commit()
            print(f"Rol ingresado correctamente")
        except Exception as e:
            print(f"Error al insertar rol {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

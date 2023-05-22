import pymysql
from datos.Conexion import Conexion
from entidades.Tbl_rolOpcion import Tbl_rolOpcion

class Dt_tbl_rolOpcion:
    def __init__(self):
        self._con = None
        self._cursor = None
        self._sql = ""

    def renovarConexion(self):
        self._con = Conexion.getConnection()
        self._cursor = Conexion.getCursor()

    def listaRolOpcion(self):
        self.renovarConexion()
        self._sql = "SELECT rp.id_rolOpcion, rol.id_rol, rol.rol, opcion.id_opcion, opcion.opcion " \
                    "FROM Seguridad.tbl_rolOpcion rp " \
                    "INNER JOIN Seguridad.tbl_opcion opcion ON rp.id_opcion = opcion.id_opcion " \
                    "INNER JOIN Seguridad.tbl_rol rol ON rp.id_rol = rol.id_rol;"
        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            listaRolOpcion = []
            for tro in registros:
                tros = Tbl_rolOpcion(tro['id_rolOpcion'], tro['id_rol'], tro['rol'], tro['id_opcion'], tro['opcion'])
                listaRolOpcion.append(tros)
            return listaRolOpcion
        except Exception as e:
            print("Datos: Error listaRolOpcion()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def agregarRolOpcion(self, id_rol, id_opcion):
        self.renovarConexion()
        rolOpcion = [id_rol, id_opcion]
        self._sql = "INSERT INTO Seguridad.tbl_rolOpcion (id_rol, id_opcion) values (%s, %s);"
        try:
            self._cursor.execute(self._sql, rolOpcion)
            self._con.commit()
            print(f"RolOpcion ingresado correctamente")
        except Exception as e:
            print(f"Error al insertar rolOpcion {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()



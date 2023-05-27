import pymysql
from datos.Conexion import Conexion
from entidades.Tbl_UserRol import Tbl_UserRol

class Dt_tbl_UserRol:
    def __init__(self):
        self._con = None
        self._cursor = None
        self._sql = ""

    def renovarConexion(self):
        self._con = Conexion.getConnection()
        self._cursor = Conexion.getCursor()

    def listaUserRol(self):
        self.renovarConexion()
        self._sql = "SELECT ur.id_UserRol, u.id_user, u.user, r.id_rol, r.rol " \
                    "FROM Seguridad.tbl_UserRol ur " \
                    "INNER JOIN Seguridad.tbl_user u ON ur.id_user = u.id_user " \
                    "INNER JOIN Seguridad.tbl_rol r ON ur.id_rol = r.id_rol;"
        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            listaUserRol = []
            for tur in registros:
                turs = Tbl_UserRol(tur['id_UserRol'], tur['id_user'], tur['user'], tur['id_rol'], tur['rol'])
                listaUserRol.append(turs)
            return listaUserRol
        except Exception as e:
            print("Datos: Error listaUserRol()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def buscarUserRol(self,texto):
        self.renovarConexion()
        self._sql = "SELECT ur.id_UserRol, u.id_user, u.user, r.id_rol, r.rol " \
                    "FROM Seguridad.tbl_UserRol ur " \
                    "INNER JOIN Seguridad.tbl_user u ON ur.id_user = u.id_user " \
                    "INNER JOIN Seguridad.tbl_rol r ON ur.id_rol = r.id_rol " \
                    "WHERE u.user LIKE '%{}%' OR r.rol LIKE '%{}%';".format(texto, texto)
        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            listaUserRol = []
            for tur in registros:
                turs = Tbl_UserRol(tur['id_UserRol'], tur['id_user'], tur['user'], tur['id_rol'], tur['rol'])
                listaUserRol.append(turs)
            return listaUserRol
        except Exception as e:
            print("Datos: Error buscarUserRol()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def agregarUserRol(self, id_user, id_rol):
        self.renovarConexion()
        userRol = [id_user, id_rol]
        self._sql = "INSERT INTO Seguridad.tbl_UserRol (id_user, id_rol) values (%s, %s);"
        try:
            self._cursor.execute(self._sql, userRol)
            self._con.commit()
            print(f"UserRol ingresado correctamente")
        except Exception as e:
            print(f"Error al insertar userRol {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()


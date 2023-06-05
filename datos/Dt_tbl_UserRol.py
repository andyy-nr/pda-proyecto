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
        self._sql = "Select * from Seguridad.vwUserRol;"
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


    def buscarUserRol(self, texto):
        self.renovarConexion()
        self._sql = "SELECT * from Seguridad.vwUserRol WHERE user LIKE '%{}%' OR rol LIKE '%{}%';".format(texto, texto)
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

    def obtenerRolXUser(self, user):
        self.renovarConexion()
        self._sql = "SELECT * from Seguridad.vwUserRol WHERE user = '{}';".format(user)
        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchone()
            return str(registros['rol'])
        except Exception as e:
            print("Datos: Error obtenerRolXUser()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def agregarUserRol(self, rolUsuario):
        self.renovarConexion()
        self._sql = "INSERT INTO Seguridad.tbl_UserRol (id_user, id_rol) values ('{}', '{}');".format(rolUsuario._id_user, rolUsuario._id_rol)
        try:
            self._cursor.execute(self._sql)
            self._con.commit()
            print(f"UserRol ingresado correctamente")
        except Exception as e:
            print(f"Error al insertar userRol {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def eliminarUserRol(self, idUserRol):
        self.renovarConexion()
        self._sql = "DELETE FROM Seguridad.tbl_UserRol WHERE id_UserRol = '{}';".format(idUserRol)
        try:
            self._cursor.execute(self._sql)
            self._con.commit()
        except Exception as e:
            print(f"Error al eliminar userRol {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def modificarUserRol(self, rolUsuario):
        self.renovarConexion()
        self._sql = "UPDATE Seguridad.tbl_UserRol SET id_user = '{}', id_rol = '{}' WHERE id_UserRol = '{}';".format(rolUsuario._id_user, rolUsuario._id_rol, rolUsuario._id_UserRol)
        try:
            self._cursor.execute(self._sql)
            self._con.commit()
        except Exception as e:
            print(f"Error al actualizar userRol {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

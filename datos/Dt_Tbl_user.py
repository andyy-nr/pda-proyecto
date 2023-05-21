import pymysql
from PyQt5.QtWidgets import QMessageBox

from datos.Conexion import Conexion
from entidades.Tbl_user import Tbl_user


class Dt_tbl_user:
    def __init__(self):
        self._con = None
        self._cursor = None
        self._sql = ""

    def renovarConexion(self):
        self._con = Conexion.getConnection()
        self._cursor = Conexion.getCursor()

    def totalUsuarios(self):
        self.renovarConexion()
        self._sql = "SELECT * FROM Seguridad.tbl_user;"
        try:
            self._cursor.execute(self._sql)
            return(str(self._cursor.rowcount))
        except Exception as e:
            print("Datos: Error totalUsuarios()", e)

    def listUsuarios(self):
        self.renovarConexion()
        self._sql = "SELECT * FROM Seguridad.tbl_user;"
        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            listaUsuario = []

            for tu in registros:
                tus = Tbl_user(tu['id_user'], tu['user'], tu['pwd'], tu['nombres'],
                            tu['apellidos'], tu['email'], tu['pwd_temp'], tu['estado'])
                listaUsuario.append(tus)
            return listaUsuario
        except Exception as e:
            print("Datos: Error listUsuarios()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def agregarUsuario(self, usuario, pwd, nombres, apellidos, email, pwd_temp, estado):
        self.renovarConexion()
        usuario = [usuario, pwd, nombres, apellidos, email, pwd_temp, estado]
        self._sql = "INSERT INTO Seguridad.tbl_user (user, pwd, nombres, apellidos, email, pwd_temp, estado) " \
                    "values (%s, %s, %s, %s, %s, %s, %s);"
        try:
            self._cursor.execute(self._sql, usuario)
            self._con.commit()
            print(f"Usuario ingresado correctamente")
        except Exception as e:
            print(f"Error al insertar usuario {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()





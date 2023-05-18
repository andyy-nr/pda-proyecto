import pymysql

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

    def listUsuarios(self):
        self.renovarConexion()
        self._sql = "SELECT * FROM Seguridad.tbl_user;"
        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            print("Numero total de registros: ", self._cursor.rowcount)
            listaUsuario = []

            for tu in registros:
                tus = Tbl_user(tu['id_user'], tu['user'], tu['pwd'], tu['nombres'],
                            tu['apellidos'], tu['email'], tu['pwd_temp'], tu['estado'])
                listaUsuario.append(tus)
            print('listaUsuario[]', listaUsuario)
            return listaUsuario

        except Exception as e:
            print("Datos: Error listUsuarios()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()



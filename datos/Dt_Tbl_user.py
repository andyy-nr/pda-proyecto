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
        self._sql = "select count(*) from Seguridad.vwUsuarios where estado <> 3;"
        try:
            self._cursor.execute(self._sql)
            resultado = self._cursor.fetchone()
            return str(resultado['count(*)'])
        except Exception as e:
            print("Datos: Error totalUsuarios()", e)

    def listUsuariosNoEliminados(self):
        self.renovarConexion()
        self._sql = "SELECT * FROM Seguridad.tbl_user where estado <> 3;"
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

    def listTodosUsuarios(self):
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

    def buscarUsuario(self, texto):
        self.renovarConexion()
        self._sql = "SELECT * FROM Seguridad.tbl_user WHERE user LIKE '%{}%' and estado <> 3;".format(texto)
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
            print("Datos: Error buscarUsuario()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def obtenerIdUsuario(self, usuario):
        self.renovarConexion()
        self._sql = "SELECT id_user from Seguridad.tbl_user WHERE user like '%{}%';".format(usuario)
        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchone()
            id = registros['id_user']
            return id
        except Exception as e:
            print("Error obtenerIDUsuario()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def agregarUsuario(self, usuario):
        self.renovarConexion()

        self._sql = "INSERT INTO Seguridad.tbl_user (user, pwd, nombres, apellidos, email, pwd_temp, estado) " \
                    "values ('{}', '{}', '{}', '{}', '{}', '{}', {});".format(usuario._user, usuario._pwd, usuario._nombres,
                                                                   usuario._apellidos, usuario._email, usuario._pwd_temp,
                                                                   usuario._estado)
        try:
            self._cursor.execute(self._sql)
            self._con.commit()
            return True
        except Exception as e:
            print(f"Error al insertar usuario {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def editarUsuario(self, usuario):
        self.renovarConexion()
        self._sql = "UPDATE Seguridad.tbl_user SET user = '{}', pwd = '{}', nombres = '{}', apellidos = '{}', " \
                    "email = '{}', pwd_temp = '{}', estado = '{}' " \
                    "WHERE id_user = '{}';".format(usuario._user, usuario._pwd, usuario._nombres, usuario._apellidos,
                                                   usuario._email, usuario._pwd_temp, usuario._estado, usuario._id_user)
        try:
            self._cursor.execute(self._sql)
            self._con.commit()
        except Exception as e:
            print(e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def eliminarUsuario(self, usuario):
        self.renovarConexion()
        self._sql = "UPDATE Seguridad.tbl_user SET estado = 3 WHERE id_user = '{}';".format(usuario._id_user)
        try:
            self._cursor.execute(self._sql)
            self._con.commit()
        except Exception as e:
            print(e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()


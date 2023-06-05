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
        self._sql = "SELECT * FROM Seguridad.vwRolOpcion WHERE estado <> 3;"
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

    def buscarRolOpcion(self, texto):
        self.renovarConexion()
        self._sql = "SELECT * FROM Seguridad.vwRolOpcion WHERE rol like '%{}%' or opcion like '%{}%';".format(texto, texto)
        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            listaRolOpcion = []
            for tro in registros:
                tros = Tbl_rolOpcion(id_rol=tro['id_rol'], rol=tro['rol'], id_opcion=tro['id_opcion'], opcion=tro['opcion'])
                listaRolOpcion.append(tros)
            return listaRolOpcion
        except Exception as e:
            print("Datos: Error buscarRolUsuario()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()


    def agregarRolOpcion(self, rolOpcion):
        self.renovarConexion()
        self._sql = "INSERT INTO Seguridad.tbl_rolOpcion (id_rol, id_opcion) values ('{}','{}');".format(rolOpcion._id_rol, rolOpcion._id_opcion)
        try:
            self._cursor.execute(self._sql)
            self._con.commit()
            print(f"RolOpcion ingresado correctamente")
        except Exception as e:
            print(f"Error al insertar rolOpcion {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def modificarRolOpcion(self, rolOpcion):
        self.renovarConexion()
        self._sql = "UPDATE Seguridad.tbl_rolOpcion SET id_rol='{}', id_opcion='{}', estado = '2' WHERE id_rolOpcion='{}';".format(rolOpcion._id_rol, rolOpcion._id_opcion, rolOpcion._id_rolOpcion)
        try:
            self._cursor.execute(self._sql)
            self._con.commit()
        except Exception as e:
            print(f"Error al modificar rolOpcion {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def eliminarRolOpcion(self, rolOpcion):
        self.renovarConexion()
        self._sql = "UPDATE FROM Seguridad.tbl_rolOpcion SET estado = '3' WHERE id_rolOpcion='{}';".format(
            rolOpcion._id_rol, rolOpcion._id_opcion, rolOpcion._id_rolOpcion)
        try:
            self._cursor.execute(self._sql)
            self._con.commit()
        except Exception as e:
            print(f"Error al modificar rolOpcion {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()



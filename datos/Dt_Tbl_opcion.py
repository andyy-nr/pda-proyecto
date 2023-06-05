import pymysql

from datos.Conexion import Conexion
from entidades.Tbl_opcion import Tbl_opcion

class Dt_tbl_opcion:
    def __init__(self):
        super().__init__()
    _con = Conexion.getConnection()
    _cursor = Conexion.getCursor()
    _cursor = _con.cursor()
    _sql = ""

    def renovarConexion(self):
        self._con = Conexion.getConnection()
        self._cursor = Conexion.getCursor()

    def listaOpciones(self):
        self.renovarConexion()
        self._sql = "SELECT * from Seguridad.tbl_opcion;"
        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            listaOpciones = []

            for tp in registros:
                tps = Tbl_opcion(tp['id_opcion'], tp['opcion'], tp['estado'])
                listaOpciones.append(tps)
            return listaOpciones

        except Exception as e:
            print("Datos: Error listaOpciones()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def buscarOpcion(self, texto):
        self.renovarConexion()
        self._sql = "select * from Seguridad.tbl_opcion where opcion like '%{}%' and estado <> 3;".format(texto)
        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            listaOpciones = []
            for to in registros:
                tos = Tbl_opcion(to['id_opcion'], to['opcion'], to['estado'])
                listaOpciones.append(tos)
            return listaOpciones
        except Exception as e:
            print("Datos: Error buscarOpcion()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()


    def agregarOpcion(self, opcion):
        self.renovarConexion()
        self._sql = "INSERT INTO Seguridad.tbl_opcion (opcion, estado) " \
                    "values ('{}', '{}');".format(opcion._opcion, opcion._estado)
        try:
            self._cursor.execute(self._sql)
            self._con.commit()
            print(f"Opcion ingresado correctamente")
        except Exception as e:
            print(f"Error al insertar opcion {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def modificarOpcion(self, opcion):
        self.renovarConexion()
        self._sql = "UPDATE Seguridad.tbl_opcion SET opcion = '{}', estado = '{}' " \
                    "WHERE id_opcion = '{}';".format(opcion._opcion, opcion._estado, opcion._id_opcion)
        try:
            self._cursor.execute(self._sql)
            self._con.commit()
        except Exception as e:
            print(f"Error al modificar opcion {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def eliminarOpcion(self, opcion):
        self.renovarConexion()
        self._sql = "UPDATE Seguridad.tbl_opcion SET estado = 3 WHERE id_opcion = '{}';".format(opcion._id_opcion)
        try:
            self._cursor.execute(self._sql)
            self._con.commit()
        except Exception as e:
            print(f"Error al eliminar opcion {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()


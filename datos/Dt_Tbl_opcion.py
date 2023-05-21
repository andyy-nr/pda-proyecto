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

    def agregarOpcion(self, nombre_opcion, estado):
        self.renovarConexion()
        opcion = [ nombre_opcion, estado]
        self._sql = "INSERT INTO Seguridad.tbl_opcion (opcion, estado) " \
                    "values (%s, %s);"
        try:
            self._cursor.execute(self._sql, opcion)
            self._con.commit()
            print(f"Opcion ingresado correctamente")
        except Exception as e:
            print(f"Error al insertar opcion {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()



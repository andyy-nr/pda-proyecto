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

    def listaOpciones(self):
        self._sql = "SELECT * FROM Seguridad.tbl_user;"
        try:
            # ejecutamos la consulta
            self._cursor.execute(self._sql)
            # Obtenemos todos los registros de la consulta
            registros = self._cursor.fetchall()
            print("Numero total de registros: ", self._cursor.rowcount)
            listaOpciones = []

            for tp in registros:
                tps = Tbl_opcion(tp['id_user'], tp['user'])
                listaOpciones.append(tps)
            print('listaOpciones[]', listaOpciones)
            return listaOpciones

        except Exception as e:
            print("Datos: Error listaOpciones()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()


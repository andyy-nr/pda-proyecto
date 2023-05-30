import pymysql
from datos.Conexion import Conexion
from entidades.Dependents import dependents

class Dt_dependents:
    def __init__(self):
        self._con = None
        self._cursor = None
        self._sql = ""

    def renovarConexion(self):
        self._con = Conexion.getConnection()
        self._cursor = Conexion.getCursor()

    def totalDependientes(self):
        self.renovarConexion()
        self._sql = "select count(*) from Seguridad.vwDependents;"
        try:
            self._cursor.execute(self._sql)
            resultado = self._cursor.fetchone()
            return str(resultado['count(*)'])
        except Exception as e:
            print("Datos: Error totalDependents()", e)

    def listaDependents(self):
        self.renovarConexion()
        self._sql = "Select * from Seguridad.vwDependents;"

        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            listaDependientes = []
            for td in registros:
                tds = dependents(td['dependent_id'], td['first_name'], td['last_name'], td['relationship'], td['employee_id'],
                                 td['employee'])
                listaDependientes.append(tds)
            return listaDependientes
        except Exception as e:
            print(f"Ocurrio un error en lista dependendientes {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def buscarDependiente(self, texto):
        self.renovarConexion()
        self._sql = "Select * from Seguridad.vwDependents where first_name like '%{}%' or last_name like '%{}%';".format(texto, texto)
        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            listaDependientes = []
            for td in registros:
                tds = dependents(td['dependent_id'], td['first_name'], td['last_name'], td['relationship'],
                                 td['employee_id'],
                                 td['employee'])
                listaDependientes.append(tds)
            return listaDependientes
        except Exception as e:
            print(f"Ocurrio un error en  buscar dependendientes {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def agregarDependientes(self, dependiente):
        self.renovarConexion()
        self._sql = "INSERT INTO Seguridad.dependents " \
                    "(first_name, last_name, relationship, employee_id) " \
                    "VALUES ('{}', '{}', '{}', '{}');".format(dependiente.first_name, dependiente.last_name,
                                                      dependiente.relationship, dependiente.employee_id)
        try:
            self._cursor.execute(self._sql)
            self._con.commit()
        except Exception as e:
            print(f"Ocurrio un error en agregar dependendientes {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()


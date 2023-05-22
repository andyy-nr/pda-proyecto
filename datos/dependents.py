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

    def totalDependents(self):
        self.renovarConexion()
        self._sql = "SELECT * FROM Seguridad.dependents;"
        try:
            self._cursor.execute(self._sql)
            return(str(self._cursor.rowcount))
        except Exception as e:
            print("Datos: Error totalDependents()", e)

    def listaDependents(self):
        self.renovarConexion()
        self._sql = "select dep.dependent_id, dep.first_name, dep.last_name, dep.relationship, emp.employee_id, " \
                    "CONCAT(emp.first_name, ' ', emp.last_name) as employee " \
                    "from Seguridad.dependents dep inner join Seguridad.employees emp on dep.employee_id = emp.employee_id;"

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

    def agregarDependientes(self, nombre, apellido, relacion, empleado):
        self.renovarConexion()
        dependientes = [nombre, apellido, relacion, empleado]
        self._sql = "INSERT INTO Seguridad.dependents " \
                    "(first_name, last_name, relationship, employee_id) " \
                    "VALUES (%s, %s, %s, %s);"
        try:
            self._cursor.execute(self._sql, dependientes)
            self._con.commit()
        except Exception as e:
            print(f"Ocurrio un error en agregar dependendientes {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()


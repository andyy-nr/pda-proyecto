from datos.Conexion import Conexion
from entidades.Departments import departments

class Dt_departments:
    def __init__(self):
        self._con = None
        self._cursor = None
        self._sql = ""

    def renovarConexion(self):
        self._con = Conexion.getConnection()
        self._cursor = Conexion.getCursor()

    def totalDepartamentos(self):
        self.renovarConexion()
        self._sql = "SELECT * FROM Seguridad.departments;"
        try:
            self._cursor.execute(self._sql)
            return(str(self._cursor.rowcount))
        except Exception as e:
            print("Datos: Error totalDepartamentos()", e)

    def listaDepartamentos(self):
        self.renovarConexion()
        self._sql = "SELECT department_id, department_name, street_address, Seguridad.departments.location_id " \
                    "FROM (Seguridad.departments inner join Seguridad.locations on Seguridad.departments.location_id = Seguridad.locations.location_id);"

        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            listaDepartamentos = []

            for td in registros:
                tds = departments(department_id=td['department_id'], department_name=td['department_name'], location_id=td['location_id'], location_name=td['street_address'])
                listaDepartamentos.append(tds)
            return listaDepartamentos
        except Exception as e:
            print("Datos: error listaDepartamentos()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def buscarDepartamento(self, texto):
        self.renovarConexion()
        self._sql = "SELECT department_id, department_name, street_address, Seguridad.departments.location_id " \
                    "FROM (Seguridad.departments inner join Seguridad.locations " \
                    "on Seguridad.departments.location_id = Seguridad.locations.location_id) " \
                    "WHERE department_name LIKE '%{}%';".format(texto)
        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            listaDepartamentos = []

            for td in registros:
                tds = departments(department_id=td['department_id'], department_name=td['department_name'], location_id=td['location_id'], location_name=td['street_address'])
                listaDepartamentos.append(tds)
            return listaDepartamentos
        except Exception as e:
            print("Datos: error buscarDepartamento()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def agregarDepartamento(self, department_name, location_id):
        self.renovarConexion()
        departamento = [department_name, location_id]
        self._sql = "INSERT INTO Seguridad.departments (department_name, location_id) " \
                    "VALUES (%s, %s);"
        try:
            self._cursor.execute(self._sql, departamento)
            self._con.commit()
            print("Registro agregado correctamente")
        except Exception as e:
            print(f"Error al agregar el registro: {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def listaLocalidades(self):
        self.renovarConexion()
        self._sql = "Select distinct street_address, Seguridad.departments.location_id " \
                    "from (Seguridad.departments inner join Seguridad.locations " \
                    "on Seguridad.departments.location_id = Seguridad.locations.location_id);"
        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            listaLocalidades = []
            for tl in registros:
                tls = departments(location_name=tl['street_address'], location_id=tl['location_id'])
                listaLocalidades.append(tls)
            return listaLocalidades
        except Exception as e:
            print("Datos: error listaLocalidades()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()


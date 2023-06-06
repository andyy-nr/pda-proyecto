from PyQt5.QtWidgets import QMessageBox, QWidget

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
        self._sql = "select count(*) from Seguridad.vwDepartments where loc_estado <> 3 and dep_estado <> 3;"
        try:
            self._cursor.execute(self._sql)
            resultado = self._cursor.fetchone()
            return str(resultado['count(*)'])
        except Exception as e:
            print("Datos: Error totalDepartamentos()", e)

    def listaDepartamentos(self):
        self.renovarConexion()
        self._sql = "Select * from Seguridad.vwDepartments where loc_estado <> 3 and dep_estado <> 3;"

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
        self._sql = "SELECT * FROM Seguridad.vwDepartments WHERE department_name LIKE '%{}%' and loc_estado <> 3 and dep_estado <> 3;".format(texto)
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

    def agregarDepartamento(self, departamento):
        self.renovarConexion()
        self._sql = "INSERT INTO Seguridad.departments (department_name, location_id) " \
                    "VALUES ('{}', '{}');".format(departamento._department_name, departamento._location_id)
        try:
            self._cursor.execute(self._sql)
            self._con.commit()
            print("Registro agregado correctamente")
        except Exception as e:
            print(f"Error al agregar el registro: {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def modificarDepartamento(self, departamento):
        self.renovarConexion()
        self._sql = "UPDATE Seguridad.departments SET department_name = '{}', location_id = '{}', estado = '2' " \
                    "WHERE department_id = '{}';".format(departamento._department_name, departamento._location_id, departamento._department_id)
        try:
            self._cursor.execute(self._sql)
            self._con.commit()
        except Exception as e:
            print("Error al editar el departamento: ", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def eliminarDepartamento(self, departamento):
        self.renovarConexion()
        self._sql = "UPDATE Seguridad.departments SET estado = '3' WHERE department_id = '{}';".format(departamento._department_id)
        try:
            self._cursor.execute(self._sql)
            self._con.commit()
        except Exception as e:
            print("Error al eliminar el departamento: ", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def listaLocalidades(self):
        self.renovarConexion()
        self._sql = "select distinct street_address, location_id from Seguridad.vwLocations where loc_estado <> 3 and country_estado <> 3;"
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


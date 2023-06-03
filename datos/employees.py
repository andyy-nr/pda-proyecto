import pymysql
from PyQt5.QtWidgets import QMessageBox, QWidget

from datos.Conexion import Conexion
from entidades.Employees import employee


class Dt_employees:
    def __init__(self):
        self._con = None
        self._cursor = None
        self._sql = ""

    def renovarConexion(self):
        self._con = Conexion.getConnection()
        self._cursor = Conexion.getCursor()

    def totalEmpleados(self):
        self.renovarConexion()
        self._sql = "select count(*) from Seguridad.vwEmployees;"
        try:
            self._cursor.execute(self._sql)
            resultado = self._cursor.fetchone()
            return str(resultado['count(*)'])
        except Exception as e:
            print("Datos: Error totalEmpleados()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def listaEmpleados(self):
        self.renovarConexion()
        self._sql = "Select * from Seguridad.vwEmployees;"
        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            listaEmpleados = []

            for te in registros:
                tes = employee(employee_id=te['employee_id'], first_name=te['first_name'], last_name=te['last_name'],
                               email=te['email'], phone=te['phone_number'], hire_date=te['hire_date'], job_id=te['job_id'],
                               job_title=te['job_title'], salary=te['salary'], manager_id=te['manager_id'],
                               manager=te['manager'], department_id=te['department_id'], department_name=te['department_name'])
                listaEmpleados.append(tes)
            return listaEmpleados
        except Exception as e:
            print("Datos: Error listaEmpleados()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def buscarEmpleado(self, texto):
        self.renovarConexion()
        self._sql = "Select * from Seguridad.vwEmployees WHERE first_name LIKE '%{}%' OR last_name LIKE '%{}%';".format(texto, texto)

        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            listaEmpleados = []
            for te in registros:
                tes = employee(employee_id=te['employee_id'], first_name=te['first_name'], last_name=te['last_name'],
                                email=te['email'], phone=te['phone_number'], hire_date=te['hire_date'], job_id=te['job_id'],
                                job_title=te['job_title'], salary=te['salary'], manager_id=te['manager_id'],
                                manager=te['manager'], department_id=te['department_id'], department_name=te['department_name'])
                listaEmpleados.append(tes)
            return listaEmpleados
        except Exception as e:
            print("Datos: Error buscarEmpleado()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def agregarEmpleado(self, empleado):
        self.renovarConexion()
        self._sql = "INSERT INTO Seguridad.employees (first_name, last_name, email, " \
                    "phone_number, hire_date, job_id, salary, manager_id, department_id) " \
                    "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');". format(empleado.first_name, empleado.last_name, empleado.email, empleado.phone,
                                                                          empleado.hire_date, empleado.job_id, empleado.salary, empleado.manager_id, empleado.department_id)
        try:
            self._cursor.execute(self._sql)
            self._con.commit()
        except Exception as e:
            print(f"error AgregarEmpleado: {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def eliminarEmpleado(self, empleado):
        self.renovarConexion()
        self._sql = "DELETE FROM Seguridad.employees WHERE employee_id = '{}';".format(empleado.employee_id)
        try:
            self._cursor.execute(self._sql)
            self._con.commit()
        except Exception as e:
            if e.args[0] == 1451:
                QMessageBox.warning(None, 'Error', "No puede eliminar este registro ya que de el dependen otros", QMessageBox.Ok)
            print(e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def editarEmpleado(self,empleado, emp_id):
        self.renovarConexion()
        self._sql = "UPDATE Seguridad.employees SET first_name = '{}', last_name = '{}', email = '{}', phone_number = '{}', " \
                    "hire_date = '{}', job_id = '{}', salary = '{}', manager_id = '{}', department_id = '{}'" \
                    " WHERE employee_id = {};".format(empleado.first_name, empleado.last_name, empleado.email,
                                                      empleado.phone, empleado.hire_date, empleado.job_id,
                                                      empleado.salary, empleado.manager_id, empleado.department_id, emp_id)
        try:
            self._cursor.execute(self._sql)
            self._con.commit()
        except Exception as e:
            print(e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def listaManagers(self):
        self.renovarConexion()
        self._sql = "Select distinct manager_id, manager from Seguridad.vwEmployees;"

        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            listaManagers = []

            for tm in registros:
                tms = employee(manager_id=tm['manager_id'], manager=tm['manager'])
                listaManagers.append(tms)
            return listaManagers
        except Exception as e:
            print("Datos: Error listaManagers()", e)
        except self._cursor.Error as e:
            if e.errno == 1451:
                QMessageBox.alert(self, 'Error', "No puede eliminar este registro ya que de el dependen otros", QMessageBox.Ok)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def listaDepartamentos(self):
        self.renovarConexion()
        self._sql = "select distinct department_name, department_id from Seguridad.vwDepartments;"

        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            listaDepartamentos = []

            for td in registros:
                tds = employee(department_name=td['department_name'], department_id=td['department_id'])
                listaDepartamentos.append(tds)
            return listaDepartamentos
        except Exception as e:
            print("Datos: Error listaDepartamentos()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def listaTrabajos(self):
        self.renovarConexion()
        self._sql = "Select distinct job_title,job_id from Seguridad.jobs;"
        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            listaTrabajos = []
            for tt in registros:
                tts = employee(job_title=tt['job_title'], job_id=tt['job_id'])
                listaTrabajos.append(tts)
            return listaTrabajos
        except Exception as e:
            print("Datos: Error listaTrabajos()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()


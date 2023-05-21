import pymysql
from PyQt5.QtWidgets import QMessageBox

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
        self._sql = "SELECT * FROM Seguridad.employees;"
        try:
            self._cursor.execute(self._sql)
            return(str(self._cursor.rowcount))
        except Exception as e:
            print("Datos: Error totalEmpleados()", e)

    def listaEmpleados(self):
        self.renovarConexion()
        self._sql = "SELECT emp.employee_id, emp.first_name, emp.last_name, emp.email, emp.phone_number, emp.hire_date, " \
                    "jobs.job_title, emp.manager_id, emp.salary, departments.department_name, " \
                    "CONCAT(manager.first_name, ' ', manager.last_name) AS manager FROM Seguridad.employees emp " \
                    "INNER JOIN Seguridad.jobs ON emp.job_id = jobs.job_id " \
                    "INNER JOIN Seguridad.departments ON emp.department_id = departments.department_id " \
                    "INNER JOIN Seguridad.employees manager ON manager.employee_id = emp.manager_id;"
        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            listaEmpleados = []

            for te in registros:
                tes = employee(employee_id=te['employee_id'], first_name=te['first_name'], last_name=te['last_name'],
                               email=te['email'], phone=te['phone_number'], hire_date=te['hire_date'],
                               job_title=te['job_title'], salary=te['salary'], manager_id=te['manager_id'],
                               department_name=te['department_name'], manager=te['manager'])
                listaEmpleados.append(tes)
            return listaEmpleados
        except Exception as e:
            print("Datos: Error listaEmpleados()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def agregarEmpleado(self, first_name, last_name, email, phone_number, hire_date, job_id, salary, manager_id, department_id):
        self.renovarConexion()
        empleado = [first_name, last_name, email, phone_number,
                     hire_date, job_id, salary,
                     manager_id, department_id]
        self._sql = "INSERT INTO Seguridad.employees (first_name, last_name, email, phone_number, hire_date, job_id, salary, manager_id, department_id) " \
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
        try:
            self._cursor.execute(self._sql, empleado)
            self._con.commit()
        except Exception as e:
            print(e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def listaManagers(self):
        self.renovarConexion()
        self._sql = "SELECT DISTINCT concat(manager.first_name, ' ', manager.last_name) AS manager, manager.employee_id " \
                    "FROM Seguridad.employees emp " \
                    "INNER JOIN Seguridad.employees manager on manager.employee_id = emp.manager_id;"

        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            listaManagers = []

            for tm in registros:
                tms = employee(employee_id=tm['employee_id'], manager=tm['manager'])
                listaManagers.append(tms)
            return listaManagers
        except Exception as e:
            print("Datos: Error listaManagers()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def listaDepartamentos(self):
        self.renovarConexion()
        self._sql = "select distinct department_name, Seguridad.employees.department_id from Seguridad.employees " \
                    "inner join Seguridad.departments " \
                    "on Seguridad.employees.department_id = Seguridad.departments.department_id;"

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
        self._sql = "Select distinct job_title, Seguridad.employees.job_id from Seguridad.employees " \
                    "inner join Seguridad.jobs on Seguridad.employees.job_id = Seguridad.jobs.job_id;"
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
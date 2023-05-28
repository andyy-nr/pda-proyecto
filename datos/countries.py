from PyQt5.QtWidgets import QMessageBox
from datos.Conexion import Conexion
from entidades.Countries import countries
from entidades.Regions import regions

class Dt_countries:
    def __init__(self):
        self._con = None
        self._cursor = None
        self._sql = ""

    def renovarConexion(self):
        self._con = Conexion.getConnection()
        self._cursor = Conexion.getCursor()

    def listaPaises(self):
        self.renovarConexion()
        self._sql = "Select * from Seguridad.vwCountries;"

        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            listaPaises = []

            for tp in registros:
                tps = countries(country_id=tp['country_id'], country_name=tp['country_name'], region_name=tp['region_name'])
                listaPaises.append(tps)
            return listaPaises
        except Exception as e:
            print("Datos: Error listaPaises()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def buscarPais(self, texto):
        self.renovarConexion()
        self._sql = "Select * from Seguridad.vwCountries where country_name like '%{}%';".format(texto)
        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            listaPaises = []

            for tp in registros:
                tps = countries(country_id=tp['country_id'], country_name=tp['country_name'], region_name=tp['region_name'])
                listaPaises.append(tps)
            return listaPaises
        except Exception as e:
            print("Datos: Error buscarPais()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def agregarPais(self, cod_pais, country_name, region_id):
        self.renovarConexion()
        pais = [cod_pais, country_name, region_id]
        self._sql = "INSERT INTO Seguridad.countries (country_id, country_name, region_id) VALUES (%s, %s, %s);"
        try:
            self._cursor.execute(self._sql, pais)
            self._con.commit()
            QMessageBox.information(self, "Registro agregado", "Registro agregado correctamente")
        except Exception as e:
            print("Datos: Error agregarPais()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def listaRegiones(self):
        self.renovarConexion()
        self._sql = "SELECT * FROM Seguridad.regions;"
        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            listaRegiones = []

            for tr in registros:
                trs = regions(region_id=tr['region_id'], region_name=tr['region_name'])
                listaRegiones.append(trs)
            return listaRegiones
        except Exception as e:
            print("Datos: Error listaRegiones()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

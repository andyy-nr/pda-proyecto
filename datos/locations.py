from datos.Conexion import Conexion
from entidades.Locations import locations

class Dt_locations:
    def __init__(self):
        self._con = None
        self._cursor = None
        self._sql = ""

    def renovarConexion(self):
        self._con = Conexion.getConnection()
        self._cursor = Conexion.getCursor()

    def listaLocalidades(self):
        self.renovarConexion()
        self._sql = "Select * from Seguridad.locations;"
        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            listaLocalidades = []

            for tl in registros:
                tls = locations(location_id=tl['location_id'], street_address=tl['street_address'],
                                postal_code=tl['postal_code'], state_province=tl['state_province'],
                                country_id=tl['country_id'], city=tl['city'])
                listaLocalidades.append(tls)
            return listaLocalidades
        except Exception as e:
            print("Datos: error listaLocalidades()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def agregarLocalidad(self, street_address, postal_code, state_province, country_id, ciudad):
        self.renovarConexion()
        localidad = [street_address, postal_code, ciudad, state_province, country_id]
        self._sql = "INSERT INTO Seguridad.locations (street_address, postal_code, city, state_province, country_id) " \
                    "VALUES (%s, %s, %s, %s, %s);"
        try:
            self._cursor.execute(self._sql, localidad)
            self._con.commit()
            print("Registro agregado correctamente")
        except Exception as e:
            print(f"Error al agregar el registro: {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def listaCiudades(self):
        self.renovarConexion()
        self._sql = "Select distinct Seguridad.locations.country_id, country_name " \
                    "from Seguridad.locations " \
                    "inner join Seguridad.countries on Seguridad.locations.country_id = Seguridad.countries.country_id;"
        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            listaCiudades = []

            for tc in registros:
                tcs = locations(country_id=tc['country_id'], country_name=tc['country_name'])
                listaCiudades.append(tcs)
            return listaCiudades
        except Exception as e:
            print("Datos: error listaCiudades()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()


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
        self._sql = "Select * from Seguridad.vwLocations where loc_estado <> 3 and country_estado <> 3;"
        try:
            self._cursor.execute(self._sql)
            registros = self._cursor.fetchall()
            listaLocalidades = []

            for tl in registros:
                tls = locations(location_id=tl['location_id'], street_address=tl['street_address'],
                                postal_code=tl['postal_code'], state_province=tl['state_province'],
                                country_id=tl['country_id'], city=tl['city'], country_name=tl['country_name'])
                listaLocalidades.append(tls)
            return listaLocalidades
        except Exception as e:
            print("Datos: error listaLocalidades()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def listaCiudades(self):
        self.renovarConexion()
        self._sql = "Select distinct country_name, country_id from Seguridad.countries where estado <> 3;"
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

    def buscarLocalidad(self, texto):
        self.renovarConexion()
        self._sql = "select * from Seguridad.vwLocations where street_address like '%{}%' and loc_estado <> 3 " \
                    "and country_estado <> 3;".format(texto)
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
            print("Datos: error buscarLocalidad()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()


    def agregarLocalidad(self, localidad):
        self.renovarConexion()
        self._sql = "INSERT INTO Seguridad.locations (street_address, postal_code, city, state_province, country_id) " \
                    "VALUES ('{}', '{}', '{}', '{}', '{}');".format(localidad._street_address, localidad._postal_code,
                                                          localidad._city, localidad._state_province, localidad._country_id)
        try:
            self._cursor.execute(self._sql)
            self._con.commit()
        except Exception as e:
            print(f"Error al agregar el registro: {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def modificarLocalidad(self, localidad):
        self.renovarConexion()
        self._sql = "UPDATE Seguridad.locations SET street_address = '{}', postal_code = '{}', city = '{}', " \
                    "state_province = '{}', country_id = '{}' WHERE location_id = '{}';".format(localidad._street_address, localidad._postal_code,  localidad._city,
                                                                                                localidad._state_province, localidad._country_id, localidad._location_id)
        try:
            self._cursor.execute(self._sql)
            self._con.commit()
        except Exception as e:
            print(f"Error al modificar el registro: {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def eliminarLocalidad(self, localidad):
        self.renovarConexion()
        self._sql = "UPDATE Seguridad.locations SET loc_estado = 3 WHERE location_id = '{}';".format(localidad._location_id)
        try:
            self._cursor.execute(self._sql)
            self._con.commit()
        except Exception as e:
            print(f"Error al eliminar el registro: {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

# nombre repetido
from datos.locations import Dt_locations
from entidades.Locations import locations

class ngLocalidades:
    def __init__(self):
        self.localidad = locations()
    dl = Dt_locations()

    def validarRepetido(self, localidad, loc_id = None):
        localidades = self.dl.listaLocalidades()
        if loc_id is None:
            for loc in localidades:
                if loc.street_address == localidad._street_address:
                    return False
        else:
            for loc in localidades:
                if not loc_id == loc._location_id:
                    if loc.street_address == localidad._street_address:
                        return False
        return True

    def agregarLocalidad(self, localidad):
        if not self.validarRepetido(localidad):
            return False
        self.dl.agregarLocalidad(localidad)

    def modificarLocalidad(self, localidad, loc_id):
        if not self.validarRepetido(localidad, loc_id):
            return False
        self.dl.modificarLocalidad(localidad)


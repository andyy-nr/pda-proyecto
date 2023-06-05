# nombre repetido
from datos.regions import Dt_Regions
from entidades.Jobs import jobs

class ngRegiones:
    def __init__(self):
        self.region = Dt_Regions()
    dr = Dt_Regions()

    def validarNombre(self, region, region_id=None):
        regiones = self.dr.listaRegiones()
        if region_id is None:
            for re in regiones:
                if re._region_name == region._region_name:
                    return False
        else:
            for re in regiones:
                if re._region_id != region_id:
                    if re._region_name == region._region_name:
                        return False
        return True

    def agregarRegion(self, region):
        if not self.validarNombre(region):
            return False
        self.dr.agregarRegion(region)

    def modificarRegion(self, region, reg_id):
        if not self.validarNombre(region, reg_id):
            return False
        self.dr.modificarRegion(region, reg_id)



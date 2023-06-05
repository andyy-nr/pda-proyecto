from datos.countries import Dt_countries
from entidades.Countries import countries

class ngPaises:
    def __init__(self):
        self.pais = countries()
    dd = Dt_countries()

    def validarRepetido(self, pais, pais_id=None):
        paises = self.dd.listaPaises()
        if pais_id is None:
            for pa in paises:
                if pa._country_name == pais._country_name:
                    return False
                if pa._country_id == pais._country_id:
                    return False
        else:
            for pa in paises:
                if pa._country_id != pais_id:
                    if pa._country_name == pais._country_name:
                        return False
                    if pa._country_id == pais._country_id:
                        return False
        return True

    def agregarPais(self, pais):
        if not self.validarRepetido(pais):
            return False
        self.dd.agregarPais(pais)

    def modificarPais(self, pais):
        if not self.validarRepetido(pais):
            return False
        self.dd.modificarPais(pais)


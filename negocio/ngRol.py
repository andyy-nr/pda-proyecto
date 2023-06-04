# nombre repetido

from datos.Dt_Tbl_rol import Dt_tbl_rol
from entidades.Tbl_rol import Tbl_rol

class ngTbl_rol:
    def __init__(self):
        self.rol = Tbl_rol()
    dr = Dt_tbl_rol()

    def validarNombre(self, rol):
        roles = self.dr.listaRoles()
        for ro in roles:
            if ro.rol == rol.rol:
                return False
        return True

    def agregarRol(self, rol):
        if not self.validarNombre(rol):
            return False
        self.dr.agregarRol(rol)

    def modificarRol(self, rol):
        if not self.validarNombre(rol):
            return False
        self.dr.modificarRol(rol)


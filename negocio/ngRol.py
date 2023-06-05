# nombre repetido

from datos.Dt_Tbl_rol import Dt_tbl_rol
from entidades.Tbl_rol import Tbl_rol

class ngTbl_rol:
    def __init__(self):
        self.rol = Tbl_rol()
    dr = Dt_tbl_rol()

    def validarNombre(self, rol, rol_id=None):
        roles = self.dr.listaRoles()
        if rol_id is None:
            for ro in roles:
                if ro.rol == rol.rol:
                    return False
            return True
        else:
            for ro in roles:
                if ro.id_rol != rol_id:
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


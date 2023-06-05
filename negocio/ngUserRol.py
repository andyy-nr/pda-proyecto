# un usuario puede tener un rol dos veces
from datos.Dt_tbl_UserRol import Dt_tbl_UserRol
from entidades.Tbl_UserRol import Tbl_UserRol

class ngUserRol:
    def __init__(self):
        self.tbl_userRol = Tbl_UserRol()
    dtur = Dt_tbl_UserRol()

    def validarRepetido(self, tbl_userRol, id_userRol=None):
        rolOpciones = self.dtur.listaUserRol()
        if id_userRol is None:
            for rol in rolOpciones:
                if rol._id_user == tbl_userRol._id_user and rol._id_rol == tbl_userRol._id_rol:
                    return False
        else:
            for rol in rolOpciones:
                if rol._id_userRol != id_userRol:
                    if rol._id_user == tbl_userRol._id_user and rol._id_rol == tbl_userRol._id_rol:
                        return False
        return True

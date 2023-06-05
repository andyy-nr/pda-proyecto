# un usuario puede tener un rol dos veces
from datos.Dt_tbl_rolOpcion import Dt_tbl_rolOpcion
from entidades.Tbl_rolOpcion import Tbl_rolOpcion

class ngRolOpcion:
    def __init__(self):
        self.rolOpcion = Tbl_rolOpcion()
    dtro = Dt_tbl_rolOpcion()

    def validarRepetido(self, rol, rol_id=None):
        rolOpciones = self.dtro.listaRolOpcion()
        if rol_id is None:
            for rolOpcion in rolOpciones:
                if rolOpcion._id_rol == rol._id_rol and rolOpcion._id_opcion == rol._id_opcion:
                    return False
        else:
            for rolOpcion in rolOpciones:
                if rolOpcion._id_rol == rol._id_rol and rolOpcion._id_opcion == rol._id_opcion:
                    return False
        return True

    def agregarRolOpcion(self, rol):
        if not self.validarRepetido(rol):
            return False
        self.dtro.agregarRolOpcion(rol)
        return True

    def modificarRolOpcion(self, rol):
        if not self.validarRepetido(rol, rol._id_rol):
            return False
        self.dtro.modificarRolOpcion(rol)
        return True

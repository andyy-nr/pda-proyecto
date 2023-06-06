# un usuario puede tener un rol dos veces
from datos.Dt_tbl_rolOpcion import Dt_tbl_rolOpcion
from entidades.Tbl_rolOpcion import Tbl_rolOpcion

class ngRolOpcion:
    def __init__(self):
        self.rolOpcion = Tbl_rolOpcion()
    dtro = Dt_tbl_rolOpcion()

    def validarRepetido(self, rol):
        rolOpciones = self.dtro.listaRolOpcionTodos()
        for rolOpcion in rolOpciones:
            if rolOpcion._id_rol == rol._id_rol and rolOpcion._id_opcion == rol._id_opcion:
                print(f"{rolOpcion._id_rol} - {rolOpcion._rol} - {rolOpcion._id_opcion} - {rolOpcion._opcion}")
                return False
        return True

    def agregarRolOpcion(self, rol):
        if not self.validarRepetido(rol):
            return False
        self.dtro.agregarRolOpcion(rol)


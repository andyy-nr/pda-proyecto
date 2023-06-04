from datos.Dt_Tbl_opcion import Dt_tbl_opcion
from entidades.Tbl_opcion import Tbl_opcion

class ngOpciones:
    def __init__(self):
        self.opcion = Tbl_opcion()
    do = Dt_tbl_opcion()

    def validarNombre(self, opcion):
        opciones = self.do.listaOpciones()
        for op in opciones:
            if op.opcion == self.opcion.opcion:
                return False
        return True

    def agregarOpcion(self, opcion):
        if not self.validarNombre(opcion):
            return False
        self.do.agregarOpcion(opcion)

    def modificarOpcion(self, opcion):
        if not self.validarNombre(opcion):
            return False
        self.do.modificarOpcion(opcion)


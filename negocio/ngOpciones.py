from datos.Dt_Tbl_opcion import Dt_tbl_opcion
from entidades.Tbl_opcion import Tbl_opcion

class ngOpciones:
    def __init__(self):
        self.opcion = Tbl_opcion()
    do = Dt_tbl_opcion()

    def validarNombre(self, opc, opc_id=None):
        opciones = self.do.listaOpciones()
        if opc_id is None:
            for op in opciones:
                if op.opcion == opc.opcion:
                    return False
        else:
            for op in opciones:
                if op.id_opcion == opc_id and op.opcion == opc.opcion:
                    return False
        return True

    def agregarOpcion(self, opcion):
        if not self.validarNombre(opcion):
            return False
        self.do.agregarOpcion(opcion)

    def modificarOpcion(self, opcion, codigo):
        if not self.validarNombre(opcion, codigo):
            return False
        self.do.modificarOpcion(opcion)


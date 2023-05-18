import copy


class Tbl_opcion:
    def __init__(self, _id_opcion=None, rol=None, estado=None):
        self._id_opcion= _id_opcion
        self._opcion = rol
        self._estado = estado

    def __str__(self):
        return f'''
        id_opcion=: {self._id_opcion},
        rol: {self._opcion},
        estado: {self._estado}
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u._id_opcion = u._id_opcion
        u._opcion = u._opcion
        u.estado = u._estado
        return u

    @property
    def id_opcion(self):
        return self._id_opcion

    @id_opcion.setter
    def id_opcion(self, id_opcion):
        self._id_opcion = id_opcion

    @property
    def opcion(self):
        return self._opcion

    @opcion.setter
    def opcion(self, opcion):
        self._opcion = opcion

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado

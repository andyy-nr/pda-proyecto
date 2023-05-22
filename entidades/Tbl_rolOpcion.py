import copy


class Tbl_rolOpcion:
    def __init__(self, id_rolOpcion=None, id_rol=None, rol=None, id_opcion=None, opcion=None):
        self._id_rolOpcion = id_rolOpcion
        self._id_rol = id_rol
        self._rol = rol
        self._id_opcion = id_opcion
        self._opcion = opcion


    def __str__(self):
        return f'''
        id_rolOpcion: {self._id_rolOpcion},
        rol: {self._rol},
        opcion: {self._opcion}
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u._id_rolOpcion = u._id_rolOpcion
        u.rol = u._rol
        u._opcion = u._opcion
        return u

    @property
    def id_rolOpcion(self):
        return self._id_rolOpcion

    @id_rolOpcion.setter
    def id_rolOpcion(self, id_rolOpcion):
        self._id_rolOpcion = id_rolOpcion

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, rol):
        self._rol = rol

    @property
    def opcion(self):
        return self._opcion

    @opcion.setter
    def opcion(self, opcion):
        self._opcion = opcion


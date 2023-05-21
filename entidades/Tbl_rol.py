import copy


class Tbl_rol:
    def __init__(self, id_rol=None, rol=None, estado=None):
        self._id_rol = id_rol
        self._rol = rol
        self._estado = estado

    def __str__(self):
        return f'''
        id_rol: {self._id_rol},
        rol: {self._rol},
        estado: {self._estado}
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u.id_rol = u._id_rol
        u.rol = u._rol
        u.estado = u._estado
        return u

    @property
    def id_rol(self):
        return self._id_rol

    @id_rol.setter
    def id_rol(self, id_rol):
        self._id_rol = id_rol

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, rol):
        self._rol = rol

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado

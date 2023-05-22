import copy


class Tbl_UserRol:
    def __init__(self, id_UserRol=None, id_user=None, user=None, id_rol=None, rol=None):
        self._id_UserRol = id_UserRol
        self._id_user = id_user
        self._user = user
        self._id_rol = id_rol
        self._rol = rol

    def __str__(self):
        return f'''
        id_UserRol: {self._id_UserRol},
        id_user: {self._id_user},
        id_rol: {self._id_rol}
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u.id_UserRol = u._id_UserRol
        u.id_user = u._id_user
        u.id_rol = u._id_rol
        return u

    # GET & SET
    @property
    def id_UserRol(self):
        return self._id_UserRol

    @id_UserRol.setter
    def id_userRol(self, id_UserRol):
        self._id_UserRol = id_UserRol

    @property
    def id_user(self):
        return self._id_user

    @id_user.setter
    def id_user(self, id_user):
        self._id_user = id_user

    @property
    def id_rol(self):
        return self._id_rol

    @id_rol.setter
    def id_rol(self, id_rol):
        self._id_rol = id_rol

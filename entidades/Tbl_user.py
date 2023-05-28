import copy


class Tbl_user:
    def __init__(self, id_user=None, user=None, pwd=None,
                 nombres=None, apellidos=None, email=None,
                 pwd_temp=None, estado=None, id_rol=None, rol=None):
        self._id_user = id_user
        self._user = user
        self._pwd = pwd
        self._nombres = nombres
        self._apellidos = apellidos
        self._email = email
        self._pwd_temp = pwd_temp
        self._estado = estado
        self._id_rol = rol
        self._rol = rol

    def __str__(self):
        return f'''
        id_user: {self._id_user},
        user: {self._user},
        pwd: {self._pwd},
        nombres: {self._nombres},
        apellidos: {self._apellidos},
        email: {self._email},
        pwd_temp: {self._pwd_temp},
        estado: {self._estado}
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u.id_user = u._id_user
        u.user = u._user
        u.pwd = u._pwd
        u.nombres = u._nombres
        u.apellidos = u._apellidos
        u.email = u._email
        u.pwd_temp = u._pwd_temp
        u.estado = u._estado
        return u

        # GET
        @property
        def id_user(self):
            return self._id_user

        # SET
        @id_user.setter
        def id_user(self, id_user):
            self._id_user = id_user

        @property
        def nombres(self):
            return self._nombres

        @nombres.setter
        def nombre(self, nombres):
            self._nombres = nombres

        @property
        def apellidos(self):
            return self._apellidos

        @apellidos.setter
        def apellidos(self, apellidos):
            self._apellidos = apellidos

        @property
        def user(self):
            return self._user

        @user.setter
        def user(self, user):
            self._user = user

        @property
        def pwd(self):
            return self._pwd

        @clave.setter
        def pwd(self, pwd):
            self._pwd = pwd

        @property
        def pwd_temp(self):
            return self._pwd_temp

        @pwd_temp.setter
        def pwd(self, pwd_temp):
            self._pwd_temp = pwd_temp

        @property
        def estado(self):
            return self._estado

        @estado.setter
        def estado(self, estado):
            self._estado = estado

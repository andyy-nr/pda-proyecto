import copy


class departments:
    def __init__(self, department_id=None, department_name=None, location_id=None):
        self._department_id = department_id
        self._department_name = department_name
        self._location_id = location_id

    def __str__(self):
        return f'''
        department_id: {self._department_id},
        department_name: {self._department_name},
        location_id: {self._location_id}
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u.department_id = u._department_id
        u.department_name = u._department_name
        u.location_id = u._location_id
        return u

    # GET & SET
    @property
    def department_id(self):
        return self._department_id

    @department_id.setter
    def department_id(self, department_id):
        self._department_id = department_id

    @property
    def department_name(self):
        return self._department_name

    @department_name.setter
    def department_name(self, department_name):
        self._department_name = department_name

    @property
    def location_id(self):
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        self._location_id = location_id
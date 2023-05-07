import copy

class countries:
    def __init__(self, country_id=None, country_name=None, region_id=None):
        self._country_id = country_id
        self._country_name = country_name
        self._region_id = region_id

    def __str__(self):
        return f'''
        country_id: {self._country_id},
        country_name: {self._country_name},
        region_id: {self._region_id}
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u.country_id = u._country_id
        u.country_name = u._country_name
        u.region_id = u._region_id
        return u

# GET & SET
    @property
    def country_id(self):
        return self._country_id

    @country_id.setter
    def country_id(self, country_id):
        self._country_id = country_id

    @property
    def country_name(self):
        return self._country_name

    @country_name.setter
    def country_name(self, country_name):
        self._country_name = country_name

    @property
    def region_id(self):
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        self._region_id = region_id
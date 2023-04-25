import copy

class regions:
    def __init__(self, region_id=None, region_name=None):
        self._region_id = region_id
        self._region_name = region_name

    def __str__(self):
        return f'''
        region_id = {self._region_id},
        region_name = {self._region_name}
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u.region_id = u._region_id
        u.region_name = u._region_name
        return u

# GET & SET
    @property
    def region_id(self):
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        self._region_id = region_id

    @property
    def region_name(self):
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        self._region_name = region_name


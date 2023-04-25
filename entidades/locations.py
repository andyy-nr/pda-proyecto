import copy

class locations:
    def __init__(self, location_id=None, street_address=None, postal_code=None, state_province=None, country_id=None):
        self._location_id = location_id
        self._street_address = street_address
        self._postal_code = postal_code
        self._state_province = state_province
        self._country_id = country_id

    def __str__(self):
        return f'''
        location_id = {self._location_id},
        street_address = {self._street_address},
        postal_code = {self._postal_code},
        tate_province = {self._state_province},
        country_id = {self._country_id}
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u.location_id = u._location_id
        u.street_address = u._street_address
        u.postal_code = u._postal_code
        u.state_province = u._state_province
        u.country_id = u._country_id
        return u

        # GET & SET

    @property
    def location_id(self):
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        self._location_id = location_id

    @property
    def street_address(self):
        return self._street_address

    @street_address.setter
    def street_address(self, street_address):
        self._street_address = street_address

    @property
    def postal_code(self):
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        self._postal_code = postal_code

    @property
    def state_province(self):
        return self.state_province

    @state_province.setter
    def state_province(self, state_province):
        self._state_province = state_province

    @property
    def country_id(self):
        return self._country_id

    @country_id.setter
    def country_id(self, country_id):
        self._country_id = country_id


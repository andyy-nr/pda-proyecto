import copy


class jobs:
    def __init__(self, job_id=None, job_title=None, min_salary=None, max_salary=None):
        self._job_id = job_id
        self._job_title = job_title
        self._min_salary = min_salary
        self._max_salary = max_salary

    def __str__(self):
        return f'''
        job_id = {self._job_id},
        job_title = {self._job_title},
        min_salary = {self._min_salary},
        max_salary = {self._max_salary}
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u.job_id = u._job_id
        u.job_title = u._job_title
        u.min_salary = u._min_salary
        u.max_salary = u._max_salary
        return u

    # GET & SET
    @property
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        self._job_id = job_id

    @property
    def job_title(self):
        return self._job_title

    @job_title.setter
    def job_title(self, job_title):
        self._job_title = job_title

    @property
    def min_salary(self):
        return self._min_salary

    @min_salary.setter
    def _min_salary(self, min_salary):
        self._min_salary = min_salary

    def max_salary(self):
        return self._max_salary

    @max_salary.setter
    def max_salary(self, max_salary):
        self._max_salary = max_salary

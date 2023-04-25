import copy


class employee:
    def __init__(self, employee_id=None, first_name=None, last_name=None, email=None, phone=None, hire_date=None,
                 job_id=None, salary=None, manager_id=None, department_id=None):
        self._employee_id = employee_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._phone = phone
        self._hire_date = hire_date
        self._job_id = job_id
        self._salary = salary
        self._manager_id = manager_id
        self._department_id = department_id

    def __str__(self):
        return f'''
        employee_id = {self._employee_id}
        first_name = {self._first_name}
        last_name = {self._last_name}
        email = {self._email}
        phone = {self._phone}
        hire_date = {self._hire_date}
        job_id = {self._job_id}
        salary = {self._salary}
        manager_id = {self._manager_id}
        department_id = {self._department_id}
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u.employee_id = u._employee_id
        u.first_name = u._first_name
        u.ast_name = u._last_name
        u.email = u._email
        u.phone = u._phone
        u.hire_date = u._hire_date
        u.job_id = u._job_id
        u.salary = u._salary
        u.manager_id = u._manager_id
        u.department_id = u._department_id
        return u

    # GET & SET
    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id = employee_id

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def hire_date(self):
        return self._hire_date

    @hire_date.setter
    def hire_date(self, hire_date):
        self._hire_date = hire_date

    @property
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        self._job_id = job_id

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    @property
    def manager_id(self):
        return self._manager_id

    @manager_id.setter
    def manager_id(self, manager_id):
        self._manager_id = manager_id

    @property
    def department_id(self):
        return self._department_id

    @department_id.setter
    def department_id(self, department_id):
        self._department_id = department_id

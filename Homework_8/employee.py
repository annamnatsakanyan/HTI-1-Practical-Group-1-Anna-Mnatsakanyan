from datetime import datetime


class Employee:
    def __init__(self, first_name, last_name, gender, work_email, salary, join_date,
                 trial_passed=False, phone_number=None, leave_date=None):
        self.name = first_name
        self.surname = last_name
        self.gender = gender
        self.email = work_email
        self.salary = salary
        self.join = join_date
        self.leave = leave_date
        self.trial_passed = trial_passed
        self.phone = phone_number

    def full_name(self):
        return f'{self.name} {self.surname}'

    def work_term(self):
        if self.leave is None:
            _join_date = datetime.strptime(self.join, '%d-%m-%y %H:%M:%S')
            _work_term = datetime.now() - _join_date
            return _work_term
        else:
            _join_date = datetime.strptime(self.join, '%d-%m-%y %H:%M:%S')
            _leave_date = datetime.strptime(self.leave, '%d-%m-%y %H:%M:%S')
            _work_term = _leave_date - _join_date
            return _work_term


first_employee = Employee("Davit", "Tovmasyan", "M", "davit.tovmasyan@company.com", "600$", "22-02-10 01:00:00", True,
                          "098169333", '21-12-20 01:00:00')
second_employee = Employee("Tovmas", "Davtyan", "M", "tovmas.davtyan@company.com", "45000Դ", "09-12-09 02:20:00", True,
                           "077123456")

print(first_employee.name, first_employee.trial_passed, first_employee.work_term())
print(second_employee.phone, second_employee.trial_passed, second_employee.full_name(), second_employee.work_term())



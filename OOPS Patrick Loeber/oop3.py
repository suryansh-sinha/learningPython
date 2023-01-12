# Topics Covered -
# Encapsulation

class SoftwareEngineer:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None         # variable ke naam ke aage _ lagana is convention for a private variable.
        self._num_bugs_solved = 0   # there is no concept of private variable in python. we just use convention to denote it.

    # to change the value of private variables, we access it using getter and setter functions.

    # getter function
    def get_salary(self):
        return self._salary

    def code(self):
        self._num_bugs_solved += 1

    # setter function
    def set_salary(self, base_value):
        self._salary = self._calculate_salary(base_value)

    # this is a private function. we must not use this function anywhere outside the class.
    def _calculate_salary(self, base_value):
        if self._num_bugs_solved < 10:
            return base_value
        if self._num_bugs_solved < 100:
            return base_value * 2
        return base_value * 3

se = SoftwareEngineer('Max', 25)
print(se.age, se.name)

for i in range(70):
    se.code()

# Setting the salary for se with base as 6000.
se.set_salary(6000)
print(se.get_salary())
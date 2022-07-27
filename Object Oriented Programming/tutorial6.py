# Public and Private Classes

# In python, we don't have public or private classes.
# So, we have created a convention that denotes classes as private.
# Class names that start with _ denote that the class is private.

class _Private:
    def __init__(self, name):
        self.name = name

class NotPrivate:
    def __init__(self, name):
        self.name = name
        self.priv = _Private(name)

    # This is a private method because it starts with an underscore.
    # This still can be used as a normal function because it's just convention but starting it with _ means
    # You're saying this is a private function.
    def _display(self):
        print("Hello")

    def display(self):
        print('Hi')

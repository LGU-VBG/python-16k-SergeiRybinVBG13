class User:
    def __init__(self, name, age):
        self.find_error_name(name)
        self.find_error_age(age)
        self._name = name
        self._age = age

    def find_error_name(self, name):
        if not isinstance(name, str) or not name.isalpha():
            raise ValueError('Некорректное имя')

    def find_error_age(self, age):
        if not isinstance(age, int) or age < 0 or age > 110:
            raise ValueError('Некорректный возраст')

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter
    def set_name(self, new_name):
        self.find_error(new_name)
        self._name = new_name

    @age.setter
    def set_age(self, new_age):
        self.find_error_age(new_age)
        self._age = new_age


user = User('67', 12)
print(user.name)
print(user.age)

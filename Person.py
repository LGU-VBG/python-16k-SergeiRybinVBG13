class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return self.name + ' ' + self.surname

    @fullname.setter
    def fullname(self, value):
        self.name, self.surname = value.split(' ', 1)


person = Person('Том', 'Йорк')
print(person.name)
print(person.surname)
print(person.fullname)

person = Person('Меган', 'Фокс')
person.name = 'Стефани'
print(person.fullname)

person = Person('Алан', 'Тьюринг')
person.surname = 'Вирт'
print(person.fullname)

person = Person('Джон', 'Маккарти')
person.fullname = 'Алан Тьюринг'
print(person.name)
print(person.surname)
print(person.fullname)

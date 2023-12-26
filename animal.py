class Animal:
    def __init__(self, color: str, name: str):
        self.color = color
        self.name = name

    paw: int = 4

    def speak(self):
        pass


class DictMixin:

    def __init__(self, color, name):
        self.name = color
        self.color = name

    def info(self, color, name):
        self.color = color
        self.name = name
        return [self.color, self.name]


class Cat(Animal, DictMixin):

    def speak(self):
        return "Miu"


cat = Cat("white", "Vaska")

print(cat.speak())
print(cat.paw)


class Dog(Animal, DictMixin):

    def speak(self):
        return "Haf"


dog = Dog("black", "Rex")

# print(dog.speak(), dog.paw)

print(dog.info(dog.color, dog.name))


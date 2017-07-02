class Person(object):

    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking")


p = Person("Addu")

p.name

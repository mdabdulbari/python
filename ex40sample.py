class Person(object):

    def __init__(self, age):
        self.age = age

    def walk(self):
        print("I am walking")

person1 = person(21)
person1.walk()
print (f"Your age is: {person1.age}")

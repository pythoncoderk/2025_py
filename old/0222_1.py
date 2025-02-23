class Person(object):
    def __init__(self, name):
        self.name = name

    def run(self, num):
        print("run" * num)
    def say_something(self):
        print("I am {}. hello".format(self.name))
        self.run(10)


person = Person("Maik")
person.say_something()
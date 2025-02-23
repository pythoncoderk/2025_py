class Car():
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print("run")

class Toyota(Car):
    def run(self):
        print("fast")

class TeslaCar(Car):
    def run(self):
        print("super fast")
    def auto_run(self):
        print("auto run")

        
car = Car()
car.run()

toyota = Toyota()
toyota.run()
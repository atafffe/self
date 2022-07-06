from operator import mod


class Car(object):

    def __init__(self, model, color, company, speed_limit):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model
    def start(self):
        print("Started")
    def stop(self):
        print("Stopped")
    def accelerate(self):
        print("Accelerating")
    def changeGear(self, gear_type):
        print("Gear Changed")

audi = Car("A6", "White", "Audi", 80)
print(audi.color)
jeep = Car("Wrangler", "Black", "Jeep", 90)
print(jeep.model, jeep.color)

class Car:
    def move(self):
        return "This vehicle moves in a unique way."

class Car(Car):
    def move(self):
        return "Driving on roads 🚗."

class Plane(Car):
    def move(self):
        return "Flying in the sky ✈️."

class Boat(Car):
    def move(self):
        return "Sailing on water 🚢."

# Creating car objects
cars = [Car(), Plane(), Boat()]

for car in cars:
    print(car.move())

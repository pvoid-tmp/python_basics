# Lesson 6 task 4
# проверки типов данных отсуствуют

class Car:

    def __init__(self, color, name):
        self.speed = 0.0
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        if self.speed < 160.0:
            self.speed += 20.0
        print("Go")

    def stop(self):
        self.speed = 0.0
        print("Stop")

    def turn(self, direction):
        if direction == "left":
            print("go left")
        elif direction == "right":
            print("go right")
        else:
            self.stop()
            print("steering issue")

    def show_speed(self):
        print(self.speed)


class TownCar(Car):

    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 60.0:
            print("Over speed detected")


class SportCar(Car):

    def go(self):
        if self.speed < 250:
            self.speed += 40
        print("Go!")


class WorkCar(Car):

    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 40.0:
            print("Over speed detected")


class PoliceCar(Car):

    def __init__(self):
        Car.__init__(self, "official striped", "Ford Crown Victoria")
        self.is_police = True


# main

c = TownCar("white", "Chevrolet Impala")
print('\n'+c.name, c.color, "Police" if c.is_police else "Civil", sep=", ")
for _ in range(4):
    c.go()
    c.show_speed()
c.turn("left")
c.turn("right")
c.turn("up")

c = SportCar("red", "Porsche 911")
print('\n'+c.name, c.color, "Police" if c.is_police else "Civil", sep=", ")
for _ in range(6):
    c.go()
c.show_speed()

c = WorkCar("yellow", "TomCat")
print('\n'+c.name, c.color, "Police" if c.is_police else "Civil", sep=", ")
for _ in range(3):
    c.go()
c.show_speed()

c = PoliceCar()
print('\n'+c.name, c.color, "Police" if c.is_police else "Civil", sep=", ")
c.go()
c.stop()

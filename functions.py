from _datetime import datetime


# datetime function
def my_function():
    now = datetime.now()
    print(now)


my_function()


# add function
def add(a, b):
    return a + b


print(add(1, 2))


# subtract function
def sub(a, b):
    return a - b


print(sub(2, 1))


# multiply
def mul(a, b):
    return a * b


mult1 = mul(2, 3)
mult2 = mul(3, 4)
print(mult1)
print(mult2)


# division function
def div(a, b):
    return a / b


try:
    division1 = div(2, 0)
    print("Result is: ", division1)
except ZeroDivisionError as e:
    print("Division by zero is not possible: ", e)
division2 = div(2, 1)
print(division2)


#classes
class Car:
    def __init__(self, make, year, horsepower):
        self.make = make
        self.year = year
        self.horsepower = horsepower

    def describe(self):
        print("Make: ", self.make)
        print("Year: ", self.year)
        print("Horsepower: ", self.horsepower)

car1 = Car("Ford", 2020, 590)
print("Car one properties: ", car1.describe())
car2 = Car("Ferrari", 2023, 700)
print("Car two properties: ", car2.describe())
car3 = Car("Volvo", 2024, 550)
print("Car three properties: ", car3.describe())


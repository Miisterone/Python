class Concession:
    def __init__(self):
        self.all_cars = []


class Car:
    def __init__(self, marque, model, colour, price):
        self.marque = marque
        self.model = model
        self.colour = colour
        self.price = price



if __name__ == '__main__':
    newCar = Car("Audi", "A3", "grey", 17000)
class Concession:
    def __init__(self):
        self.all_cars = []

    def add_car(self, car):
        self.all_cars.append(car)

    def display_cars(self):
        print("------------ OUR CARS -----------")
        for cars in self.all_cars:
            print(cars.marque, cars.model, cars.colour, ":", cars.price)

    def search_car(self, marque, model, colour, price):
        sold = None
        for search in self.all_cars:
            if marque == search.marque:
                if model == search.model:
                    if colour == search.colour:
                        if price >= search.price:
                            sold = search
                        else:
                            return "Pas assez d'oseille...", None
        if sold is not None:
            self.all_cars.remove(sold)
            return "Nous avons trouvé une voiture qui correspond a vos critères :", sold

        return "Nous n'avons pas de voiture qui corresponde a vos critères...", None


class Car:
    def __init__(self, marque, model, colour, price):
        self.marque = marque
        self.model = model
        self.colour = colour
        self.price = price

    def __str__(self):
        return self.marque + " " + self.model + " " + self.colour + " " + ":" + " " + str(self.price)


if __name__ == '__main__':
    newCar = Car("Audi", "A3", "grey", 17000)
    myConcession = Concession()
    myConcession.add_car(newCar)
    myConcession.display_cars()
    sentence, founded_car = myConcession.search_car("Audi", "A3", "grey", 23000)
    print(sentence)
    if founded_car is not None:
        print(founded_car)

    myConcession.display_cars()
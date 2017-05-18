#print "hello world"
"""
class car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = empty
        self.mileage = mileage
        self.tax = 0
    def showinfo(self):
        print self.price
        print self.speed
        print self. fuel
        print self.mileage
        print self.tax
    def sale_price(self):
        if self.price >= 10000
        self.tax = "15%"
    else:
        self.tax = "10%"
    def fuel_amount(self):
"""
class car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed =speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
    def displayinfo(self):
        print "price: ", self.price
        print "speed: ", self.speed, "mph"
        print "fuel: ", self.fuel
        print "mileage: ", self.mileage, "mpg"
        print "tax: ", self.tax
car1 = car(2000, 35, "Full", 15)
car1.displayinfo()

car2 = car(10001, 5, "Not Full", 105)
car2.displayinfo()

car3 = car(2000, 15, "Kind of Full", 95)
car3.displayinfo()

car4 = car(1300, 45, "Empty", 25)
car4.displayinfo()

car5 = car(2000000, 35, "Empty", 15)
car5.displayinfo()

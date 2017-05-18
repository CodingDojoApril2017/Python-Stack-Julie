class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayinfo(self):
        print self.price
        print self.max_speed
        print self.miles
        return self
    def ride(self):
        print "riding"
        self.miles += 10
        return self
    def reverse(self):
        print "reverse"
        self.miles -=5
        return self
biker1 = Bike(50,20,20)
biker1.reverse().ride().ride().ride().displayinfo()

#biker2 = Bike(130,25)
#biker2.reverse().ride().ride().ride().displayinfo()

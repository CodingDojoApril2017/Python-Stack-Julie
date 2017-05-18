"""
class Animal(object):
    def __init__(self, health, name, walk):
        self.health = health
        self.name = name
        self.walk = self.health-5
        #for self.health - 5 = self.walk
        #for self.health -10 = self.run
    def displayinfo(self):
        print "Display Health: ", self.health
        print "Name: ", self.name
animal1 = Animal(100, "george", 5)
animal1.displayinfo()
"""
"""
class Animal(object):
    def __init__(self, name, health, walk, run):
        self.name = name
        self.health = health
        self.walk = self.health-5
        self.run = self.health-10
    def displyhealth(self):
        print "Display Health: ", self.health
#class Animals(object):
    #def __inti__(self, name, health)
class Animals(object):
    def __init__(self, name="animal",health =100):
        self.name=name
        self.health=health
        self.displayhealth()
    #def walk(self):
#        if self.health -= 1
#        print "walking"
#    else:
#        print "Dead"
animal = Animals("animal")
animal.health()
"""

#class Animal(object):
#    def __init__(self, name, health, walk, run)



class Animal(object):
	def __init__(self, name="animal", health = 100):
		self.name = name
		self.health = health
		self.displayHealth()
	def walk(self):
		if self.health > 1:
			self.health -= 1
			print "Walking"
		else:
			self.health = 0
			print "Dead"
		return self
	def run(self):
		if self.health > 5:
			self.health -=5
			print "Running"
		else:
			self.health = 0
			print "Dead"
		return self
	def displayHealth(self):
		print self.name+"'s health is:", self.health
#i would need to make a separate folder file for the new class so i could call it form there? is that what they want?
class Dog(Animal):
	def __init__(self,name):
		health = 150
		super(Dog, self).__init__(name, health)
	def pet(self):
		self.health += 5
		print "Petting"
		return self

class Dragon(Animal):
	def __init__(self,name):
		health = 170
		super(Dragon,self).__init__(name,health)
	def fly(self):
		print "Flying"
		self.health -= 10
		return self
	def displayHealth(self):
		super(Dragon,self).displayHealth()


animal = Animal("Animal")
animal.walk().walk().walk().run().run().displayHealth()


dog = Dog("Joshua")
dog.walk().walk().walk().run().run().pet().displayHealth()

dragon = Dragon("Jorge")
dragon.walk().walk().walk().run().run().fly().fly().displayHealth()

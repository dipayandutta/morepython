class Animal:
    def eat(self):
        print("Eat Method")
    def sleep(self):
        print("Sleep Method")

class Dog(Animal):
    def bark(self):
        print("Bark function")

class Goat(Animal):
    def voice(self):
        print("baaa")

labrador = Dog()
labrador.eat()
labrador.sleep()
labrador.bark()

goat = Goat()
goat.eat()
goat.sleep()
goat.voice()
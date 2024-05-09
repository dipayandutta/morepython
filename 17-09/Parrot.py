class Car:

    #class attributes 
    model = ""
    age   = 0

    def carWash(self):
        print("hello")

# Create Maruti Object 
maruti = Car()
maruti.model="XYZ"
maruti.age = 2
maruti.carWash()

# Create Honda Object 
honda = Car()
honda.model="Honda"
honda.age  = 5

# print attributes
print(f"Model => {maruti.model} is {maruti.age} years old")
print(f"model {honda.model} is {honda.age} years old")
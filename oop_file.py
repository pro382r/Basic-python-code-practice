class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

my_dog = Dog("Buddy", "Golden Retriever")
print("Dog's name:", my_dog.name)
my_dog.bark()

class Car:
  def __init__(self, model, color):
    self.model = model
    self.color = color

  def start(self):
    print("The car is starting.")

my_car = Car("Tesla", "Red")
print(my_car.model)
my_car.start()

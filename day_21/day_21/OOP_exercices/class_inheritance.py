class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("Inhile, Exhile")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print("Doing this under the water")

    def swim(self):
        print("Moving in the water")

mimo = Fish()

mimo.breath()
mimo.swim()
print(mimo.num_eyes)
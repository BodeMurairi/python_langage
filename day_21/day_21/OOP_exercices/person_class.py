class Person():
    def __init__(self):
        self.name = input("What is your name")
        self.country = input("Which country are you from?")
        self.birth_date = int(input("Which year where you born?:"))
        self.current_year = int(input("which year are we?"))

    def age(self):
        age = self.current_year - self.birth_date
        print(f"Mr/Ms. {self.name}, you are {age} years old")

sandra = Person()
sandra.age()
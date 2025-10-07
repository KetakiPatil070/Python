
class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def display_info(self):
        print(f"Cat Name: {self.name}")
        print(f"Breed: {self.breed}")

my_cat = Cat("Whiskers", "Persian")
my_cat.display_info()

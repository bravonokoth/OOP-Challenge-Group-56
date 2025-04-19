class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Start with moderate hunger
        self.energy = 5  # Start with moderate energy
        self.happiness = 5  # Start with moderate happiness
        self.tricks = []  # List to store learned tricks

    def eat(self):
        self.hunger = max(0, self.hunger - 3)  # Reduce hunger, not below 0
        self.happiness = min(10, self.happiness + 1)  # Increase happiness, not above 10
        print(f"{self.name} ate some food! Hunger decreased, happiness increased.")

    def sleep(self):
        self.energy = min(10, self.energy + 5)  # Increase energy, not above 10
        print(f"{self.name} took a nap! Energy increased.")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2  # Decrease energy
            self.happiness = min(10, self.happiness + 2)  # Increase happiness
            self.hunger = min(10, self.hunger + 1)  # Increase hunger
            print(f"{self.name} had fun playing! Happiness increased, but got hungrier and a bit tired.")
        else:
            print(f"{self.name} is too tired to play!")

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 1)  # Small happiness boost for learning
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name}'s tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} doesn't know any tricks yet!")

    def get_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
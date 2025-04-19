from pet import Pet

# Create a new pet
my_pet = Pet("Buddy")

# Test the pet's functionality
print("Welcome to your digital pet!")
my_pet.get_status()

# Interact with the pet
my_pet.eat()
my_pet.get_status()

my_pet.play()
my_pet.get_status()

my_pet.sleep()
my_pet.get_status()

# Teach and show tricks
my_pet.train("Sit")
my_pet.train("Roll Over")
my_pet.train("Sit")  # Try teaching the same trick again
my_pet.show_tricks()
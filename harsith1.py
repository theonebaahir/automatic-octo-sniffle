class Dog:
    # Class variable (shared by all dogs)
    species = "Canis familiaris"

    def __init__(self, name, breed):
        # Instance variables (unique to each object)
        self.name = name
        self.breed = breed

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Species: {Dog.species}")
        print("------------------------")

# Create two Dog objects with different breeds
dog1 = Dog("Bruno", "Labrador Retriever")
dog2 = Dog("Lucy", "German Shepherd")

# Display their details
dog1.display_info()
dog2.display_info()

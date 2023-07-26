"""
Assignment: Animal Sounds

Create a simple program that represents different animals and their sounds. Follow the steps below to complete 
the assignment:
Step 1: Create a base class Animal with a method make_sound(). This method should print a generic animal sound.
Step 2: Create two subclasses Dog and Cat, each inheriting from the Animal class.
Step 3: Override the make_sound() method in the Dog and Cat classes with their respective sounds (bark and meow).
Step 4: Implement a function called animal_sound_in_zoo() that takes an animal object as a parameter and calls its 
        make_sound() method.
Step 5: Create instances of Dog and Cat classes and call the animal_sound_in_zoo() function with these instances 
        as arguments to observe their unique sounds.    Hints:

You can use the print() function to display the output.

Remember to use the super() function inside the make_sound() method of the derived classes to call the base class's 
make_sound() method.
"""

# Step 1: Create a base class Animal with a method make_sound()
class Animal:
    def make_sound(self):
        print("Generic animal sound")

# Step 2: Create two subclasses Dog and Cat, each inheriting from the Animal class.
class Dog(Animal):
    # Step 3: Override the make_sound() method in the Dog class with the sound "bark"
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    # Step 3: Override the make_sound() method in the Cat class with the sound "meow"
    def make_sound(self):
        print("Meow")

# Step 4: Implement the animal_sound_in_zoo() function
def animal_sound_in_zoo(animal):
    # Step 5: Call the make_sound() method of the animal object
    animal.make_sound()

# Create instances of Dog and Cat classes
dog_instance = Dog()
cat_instance = Cat()

# Call the animal_sound_in_zoo() function with these instances as arguments
print("Sound of dog in the zoo:")
animal_sound_in_zoo(dog_instance)

print("\nSound of cat in the zoo:")
animal_sound_in_zoo(cat_instance)

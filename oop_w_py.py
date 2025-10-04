"""A simple demonstration of object-oriented programming with Python classes."""


class Dog:
    """A Dog class"""

    legs: int = 4
    ears: int = 2
    type: str = "random"

    def eat(self):
        """just prints eating"""
        print(f"The dog is eating. {self.ears}")


dog = Dog()
dog.eat()
print(dog.ears, dog.legs)

class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __str__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    @classmethod
    def remove_dead(cls):
        cls.alive = [animal for animal in cls.alive if animal.health > 0]

class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden

class Carnivore(Animal):
    def bite(self, other):
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            Animal.remove_dead()

# Example usage
lion = Carnivore("Simba")
rabbit = Herbivore("Susan")
print(Animal.alive)  # Initial state
lion.bite(rabbit)  # Lion bites Susan
print(Animal.alive)  # Check state after bite
rabbit.hide()  # Susan hides
lion.bite(rabbit)  # Attempt to bite hidden Susan
print(Animal.alive)  # Final state

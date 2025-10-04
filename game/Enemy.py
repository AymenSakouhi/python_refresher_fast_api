"""a Class of Enemy that I am going to use for my game"""


class Enemy:
    """my class of enemy"""

    type_of_enemy: str
    health_points: int = 10
    attack_damage: int = 1

    def talk(self):
        """Talking"""
        print(f"I am an enemy of type {self.type_of_enemy}")

    def walk_forward(self):
        """walking towards you"""
        print(f"{self.type_of_enemy} is moving closer to you")

    def attack(self):
        """attacking with self.attack_damage"""
        print(f"{self.type_of_enemy} is attacking with {self.attack_damage}")

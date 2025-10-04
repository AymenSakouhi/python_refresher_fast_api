"""a Class of Enemy that I am going to use for my game"""


class Enemy:
    """my class of enemy"""

    def __init__(
        self, type_of_enemy: str = "", health_points: int = 10, attack_damage: int = 1
    ) -> None:
        self.type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def talk(self):
        """Talking"""
        print(f"I am an enemy of type {self.type_of_enemy} and ready to fight")

    def walk_forward(self):
        """walking towards you"""
        print(f"{self.type_of_enemy} is moving closer to you")

    def attack(self):
        """attacking with self.attack_damage"""
        print(f"{self.type_of_enemy} attacks for {self.attack_damage}")

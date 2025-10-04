"""a Class of Enemy that I am going to use for my game"""


class Enemy:
    """my class of enemy"""

    def __init__(
        self, type_of_enemy: str = "", health_points: int = 10, attack_damage: int = 1
    ) -> None:
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def get_type_of_enemy(self):
        """a getter for a private attribute"""
        return self.__type_of_enemy

    def talk(self):
        """Talking"""
        print(f"I am an enemy of type {self.__type_of_enemy} and ready to fight")

    def walk_forward(self):
        """walking towards you"""
        print(f"{self.__type_of_enemy} is moving closer to you")

    def attack(self):
        """attacking with self.attack_damage"""
        print(f"{self.__type_of_enemy} attacks for {self.attack_damage}")

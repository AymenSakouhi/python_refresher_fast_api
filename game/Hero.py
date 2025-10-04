"""Hero class"""

from Weapon import *


class Hero:
    """Hero class to equip weappon and battle asa well"""

    def __init__(self, health_points, attack_damage):
        """
        Purpose: these values as like enemy but this is the Hero class
        """
        self.health_points = health_points
        self.attack_damage = attack_damage
        self.is_weapon_equiped: bool = False
        self.weapon: Weapon = None

    def talk(self):
        """talking"""
        print("Hero: here I came to finish you monster")

    def equip_weapon(self):
        """equip weapon"""
        if not self.is_weapon_equiped and self.weapon is not None:
            self.attack_damage += self.weapon.attack_increase
            self.is_weapon_equiped = True

    def attack(self):
        """attacking"""
        print(f"Hero attacks for {self.attack_damage}")

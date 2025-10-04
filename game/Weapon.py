"""a weapon class to be equiped by a hero"""


class Weapon:
    """A weapon class that can be equipped by a hero to increase attack power."""

    def __init__(self, weapon_type, attack_increase):
        """
        Purpose: a calss of a weapon
        """
        self.weapon = weapon_type
        self.attack_increase = attack_increase

    # end alternate constructor

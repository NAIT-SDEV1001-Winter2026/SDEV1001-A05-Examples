class Monster:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def introduce(self):
        print(f"I am {self.name} and I am {self.color}.")

    def make_sound(self):
        print(f"{self.name} makes a mysterious monster sound!")

    def special_move(self):
        print(f"{self.name} does something Monster like!")


class Dragon(Monster):
    def __init__(self, name, color, fire_power):
        super().__init__(name, color)
        self.fire_power = fire_power

    def make_sound(self):
        print(f"{self.name} roars: RAAAAWR!")

    def special_move(self):
        print(f"{self.name} breathes fire with power level {self.fire_power}! 🔥")


class Ghost(Monster):
    def __init__(self, name, color, transparency):
        super().__init__(name, color)
        self.transparency = transparency

    def make_sound(self):
        print(f"{self.name} whispers: Woooooooo...")

    def special_move(self):
        print(f"{self.name} floats through a wall at {self.transparency}% transparency! 👻")


class Slime(Monster):
    def __init__(self, name, color, goo_level):
        super().__init__(name, color)
        self.goo_level = goo_level

    def make_sound(self):
        print(f"{self.name} squishes: splorp splorp!")

    def special_move(self):
        print(f"{self.name} oozes across the floor with goo level {self.goo_level}! 🟢")


class Werewolf(Monster):
    def __init__(self, name, color, fluffiness):
        super().__init__(name, color)
        self.fluffiness = fluffiness

    def make_sound(self):
        print(f"{self.name} howls: Awooooo!")

    def special_move(self):
        print(f"{self.name} does a dramatic moon howl with fluffiness {self.fluffiness}! 🌕")


monsters = [
    Dragon("Blaze", "red", 95),
    Ghost("Misty", "white", 80),
    Slime("Goober", "green", 100),
    Werewolf("Fang", "brown", 87)
]

for monster in monsters:
    monster.introduce()
    monster.make_sound()
    monster.special_move()
    print()
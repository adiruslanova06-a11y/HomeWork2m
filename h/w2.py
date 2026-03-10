from lesson1 import user


class Hero:
    def __init__(self, name,lv,hp,strength):
        self.name = name
        self.lv = lv
        self.hp = hp
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}")

    def attack(self):
        print(f"{self.name} герой наносит удар!")

    def rest(self):
        print(f"{self.name} отдыхает...")


    def show_info(self):
        print(f"Герой: {self.name},уровень: {self.lv}")


class Warrior(Hero):
    def __init__(self, name, lv,hp,strength, stamina):
        super().__init__(name, lv, hp, strength)
        self.stamina = stamina

    def attack(self):
        print(f"{self.name} (воин) атакует мечом")

class Mage(Hero):
    def __init__(self, name, lv,hp,strength, mana):
        super().__init__(name, lv, hp, strength)
        self.mana = mana

    def attack(self):
        print(f"{self.name}(маг),колдует заклинанием!")

class Assassin(Hero):
    def __init__(self, name, lv,hp,strength,stealth):
        super().__init__(name,lv, hp, strength)
        self.stealth = stealth

    def attack(self):
        print(f"{self.name}(ассасин),атакует из-под тишка !")


Warrior = Warrior("Artur", 15, 16, 23, 45)
Mage = Mage("Merlin", 7, 8, 70)
Assassin = Assassin("Ночной Коготь", 7, 50, 90)




import random
class Warrior:
    name = "Warrior"
    beats = "Assasin"

class Mage:
    name = "Mage"
    beats = "Warrior"

class Assasin:
    name = "Assassin"
    beats = "Mage"


warrior_obj = Warrior()
mage_obj = Mage()
assassin_obj = Assassin()

heroes = [warrior_obj, mage_obj, assassin_obj]

bot=random.choice(heroes)
print(f"Ваш выбор: {bot.name}")
print(f"Ваш противник: {bot.name}"



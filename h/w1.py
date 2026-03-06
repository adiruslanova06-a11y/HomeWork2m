class Hero:
    def __init__(self, name,level,health,strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет,{self.name},{self.level}")

    def attack(self):
        print(f"{self.name} атакует врага!")
        self.strength -= 1

    def rest(self):
        print(f"{self.name} отдыхает...")
        self.health += 1

hero1=Hero("Hero1",1,10,5)
hero2=Hero("Hero2",2,10,5)
hero1.greet()
hero1.attack()
hero1.rest()

hero2.greet()
hero2.attack()
hero2.rest()

print(f"\nResult {hero1.name}: Strength={hero1.strength}, Health={hero1.health}")
print(f"Result {hero2.name}: Strength={hero2.strength}, Health={hero2.health} ")




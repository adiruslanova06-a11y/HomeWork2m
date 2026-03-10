class Hero:
    def __init__(self, name, level,hp):
        self.name = name
        self.level = level
        self.hp = hp

    def action(self):
        print(f"{self.name},готов к бою!")

class MageHero(Hero):
    def __init__(self, name, level,hp,mp):
        super().__init__()
        self.name = name
        self.level = level
        self.hp = hp
        self.mp = mp
    def action(self):
        print(f"Маг {self.name} кастует заклинание! MP: {self.mp}")


class Warrior(MageHero):
    def __init__(self, name, level,hp,mp):
        super().__init__()
        self.name = name
        self.level = level
        self.hp = hp
        self.mp = mp
    def action(self):
        print(f"Воин {self.name} рубит мечом! MP: {self.mp}")


class BankAccount:
    bank_name = "International Bank"

    def __init__(self, name, hero,balance,password):
        self.hero = hero
        self._balance = balance
        self.__password = password

    def login(self, password):
        return self.__password == password

    @property
    def full_info(self):
        return f"Hero: {self.hero.name}, Balance: {self._balance}"

    @classmethod
    def get_bank_name(cls):
        return cls.bank_name

    def bonus_for_level(self):
        level = getattr(self.hero, 'lvl', 1)
        return level

    class Hero:
        def __init__(self, name, hero_class, level, balance):
            self.name = name
            self.hero_class = hero_class
            self.level = level
            self.balance = balance

        def __str__(self):
            return f"{self.name} | Баланс: {self.balance} SOM"

        def __add__(self, other):
            if self.hero_class == other.hero_class:
                return self.balance + other.balance
            raise ValueError(f"Нельзя складывать баланс разных классов: {self.hero_class} и {other.hero_class}")

        def __eq__(self, other):
            if not isinstance(other, Hero):
                return False
            return self.name == other.name and self.level == other.level

from abc import ABC, abstractmethod
class SmsService(ABC):
    @abstractmethod
    def send_opt(self,phone):
        pass

class KGSms(SmsService):
    def send_opt(self,phone):
        return f"<text>Код: 1234</text><phone>{phone}</phone>"

 class RUSms(SmsService):
    def send_otp(self, phone):
        return {"text": "Код: 1234", "phone": phone}

class BankAccount:
    def __init__(self, hero, balance, pin, bank_name):
        self.hero = hero
        self.balance = balance
        self.pin = pin
        self.__bank_name = bank_name

    def __str__(self):
        return f"{self.hero.name} | Баланс: {self.balance} SOM"

    def __add__(self, other):
        if type(self.hero) == type(other.hero):
            return self.balance + other.balance
        return "Ошибка: Нельзя сложить счета героев разных классов!"

    def __eq__(self, other):
        return (self.hero.name == other.hero.name and
                self.hero.level == other.hero.level)

    def get_bank_name(self):
        return self.__bank_name
    def bonus_for_level(self):
        return self.hero.level




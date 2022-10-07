"""
1)Выбрать предметную область
2)Создать класс
3)Описать свойства
4) Описать методы
Свойств min 5, методов min 2
5)Реализовать наследование
6)полиморфизм
7)инкапсуляцию
"""
"""
Предметная область: RPG игра. 
Свойства объекта: 
1. Имя персонажа
2. Количество хп
3. уровень
4. урон
5. защита

Методы объекта:
1. Атаковать
2. Использовать умение
3. Принять атаку

Наследование через разные классы (Воин, Маг)
Полиморфизм через интерфейс У каждого класса будет своё умение
Инкапсуляция приватными свойствами
"""


class ICharacterMeta(type):
    def __instancecheck__(self, instance):
        return self.__subclasscheck__(type(instance))

    def __subclasscheck__(self, subclass):
        return (hasattr(subclass, 'name')
                and hasattr(subclass, 'health_point')
                and hasattr(subclass, 'level')
                and hasattr(subclass, 'damage')
                and hasattr(subclass, 'defense')
                and callable(subclass.attack)
                and callable(subclass.use_skill)
                and callable(subclass.take_attack))


class SuperCharacter(metaclass=ICharacterMeta):
    def __init__(self, name, damage, defense):
        self.__name = name
        self.__damage = damage
        self.__defense = defense
        self.__health_point = 100
        self.__level = 1

    @property
    def name(self):
        return self.__name

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, damage_value):
        self.__damage = damage_value
    @property
    def defense(self):
        return self.__defense

    @defense.setter
    def defense(self, defenseValue):
        if defenseValue <= 25:
            self.__defense += defenseValue
        else:
            print('Invalid value')
    @property
    def health_point(self):
        return self.__health_point

    @property
    def level(self):
        return self.__level

    def take_attack(self, attack_damage):
        self.__health_point -= attack_damage

    def attack(self, target):
        target.take_attack(self.__damage)

    def use_skill(self):
        self.__health_point += 10
        self.__damage += 5


class Warrior(SuperCharacter):
    def use_skill(self):
        print('Warrior skill:')
        print(f'Old defense: {self.defense}, Old damage: {self.damage}')
        self.defense = 18
        self.damage = 74
        print(f'New defense: {self.defense}, New damage: {self.damage}')

class Wizzard(SuperCharacter):
    def use_skill(self):
        print('Wizzard skill:\nUSING SHADOW ROOTS!!!')


warrior = Warrior('Moguzo', 8, 50)
wizzard = Wizzard('Shihoru', 2, 20)

warrior.use_skill()
wizzard.use_skill()

warrior.attack(wizzard)
print(f'{wizzard.name} health after {warrior.name} attack: {wizzard.health_point}')
wizzard.health_point = 100
print(wizzard.health_point)




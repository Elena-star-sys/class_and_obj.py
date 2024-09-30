# nums = [7,8,9,3,1,2,]
#
# def bubble_sort(ls):
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(len(ls) - 1):
#             if ls[i]  > ls[i + 1]:
#                 ls[i], ls[i + 1] = ls[i + 1], ls[i]
#                 swapped = True
# #
# # bubble_sort(nums)
# # print(nums)
#
# def selection_sort(ls):
#     for i in range(len(ls)):
#         lowest = i
#         for j in range(i + 1, len(ls)):
#             if ls[j] < ls[lowest]:
#                 lowest = j
#         ls[i], ls[lowest] = ls[lowest], ls[i]
#
# selection_sort(nums)
# print(nums)
# from math import floor


class Hero:

    def __init__(self, health=100, level=1, attack_damage=10):
        self.health = health
        self.level = level
        self.attack_damage = attack_damage
        self.inventory = []

    def find_item(item):
        message = f'Вы нашли {item}'
        self_inventory.append(item)
        print(message)

    def attack(self):
        mob.health -= self.attack_damage
        print(f'Вы напали на {mob.name} и нанесли {self.attack_damage} урона. У {mob.name} осталось {mob.health} зоровья.')

    def show_status(self):
        health_status = f'Здоровье героя: {self.health}'
        inventory_status = f'Инвентарь героя: {', '.join(self.inventory) if self.inventory else 'пусто'}'
        level_status = f'Уровень героя: {self.level}'
        attack_status = f'Урон героя: {self.attack_damage}'
        print(health_status)
        print(inventory_status)
        print(level_status)
        print(attack_status)


class Mob:

    def __init__(self, name, health, attack_damage):
        self.name = name
        self.health = health
        self.attack_damage = attack_damage

    def attack(self):
        hero.health -= self.attack_damage
        print(f'На вас напал {self.name} и нанёс {self.attack_damage} урона. У вас осталось {hero.health} зоровья.')


    def main():
        hero = Hero()
        orc = Mob("Орк", 50, 15)
        hero.show_status()

        while hero.health > 0 and orc.health > 0:
            hero.attack(orc)
            if orc.health > 0:
                orc.attack(hero)
            print()

        if hero.health > 0:
            print(f"Вы победили {orc.name}!")
        else:
            print(f"Вас победил {orc.name}.....")

if __name__ == '__main__':
    main()












# def main():
#     find_item("меч")
#     find_item("щит")
#     show_status()
#     fight_monster('Гоблин', 30)
#     show_status()
#     fight_monster("Дракон", 80)
#     show_status()



# class Car:
#     def __init__(self, model, colour):
#         self.model = model
#         self.colour = colour
#
#     def start(self):
#         print(f'{self.model} {self.colour} на старте')
#
# my_car = Car('BMV', 'red')
# my_car.start()


# class House:
#     def __init__(self, floor, door):
#         self.floor = floor
#         self.door = door
#
#     def start(self):
#         print(f'Я нахожусь на {self.floor} этаже, квартира номер {self.door} ')
#
# my_house = House(5, 54)
# my_house.start()


# class House:
#     def __init__(self, name, floors):
#         self.name = name
#         self.number_floors = floors
#
#     def go_to(self,new_floor):
#         if 1 <= new_floor <= self.number_floors:
#             for floor in range(1, new_floor + 1):
#                 print(floor)
#         else:
#             print(f'Такого этажа не существует')
#
#     def __del__(self):
#         print(f'{self.name} снесён, но он останется в истории"')




# h1 = House('ЖК Горский', 18)
# h2 = House('Домик в деревне', 2)
# del (h2)
# h1.go_to(5)
# # h2.go_to(10)


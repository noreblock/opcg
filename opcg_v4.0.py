import random
from dataclasses import dataclass


#Helping methods
def sequence_printer(seq: list):
    seq = list(set(seq))
    res = ''
    repeat_count = len(seq) - 1
    for i in range(repeat_count):
        res += str(seq[i]) + ', '
    res += str(seq[len(seq) - 1])
    return res

def x_in_int_bounds(x: int, bounds: list):
    if x in range(bounds[0], bounds[1] + 1): return True
    else:
        print('Argument is out of range!')
        return False

class Separator:
    def __init__(self, sub=False, lenght=100, symbol='='):
        self.sub = sub
        self.lenght = lenght
        self.symbol = symbol
        self.counter = 1

    def split(self, count: bool = False, title: str = None):
        if title is None:
            if count:
                print(self.symbol * int((self.lenght - 3) / 2) + f'[{self.counter}]' +
                      (self.symbol * int((self.lenght - 3) / 2 + 1)))
                self.counter += 1
            else:
                print(self.symbol * self.lenght)
        else:
            if count:
                print(self.symbol * int((self.lenght - len(title) - 5) / 2) + f'[{title}({self.counter})]' +
                      (self.symbol * int((self.lenght - len(title) - 4) / 2)))
                self.counter += 1
            else:
                print(self.symbol * int((self.lenght - len(title) - 1) / 2) + f'[{title}]' +
                      (self.symbol * int((self.lenght - len(title) - 1) / 2)))



#Character generation methods
@dataclass
class Data:
    fruit_range = [1, 150]
    fraction_range = [0, 2]
    sea_range = [0, 5]
    haki_range = [0, 1, 2, 3, 4]
    race_range = [0, 1, 2, 3, 4]
    rokushiki_range = [0, 1, 2, 3, 4, 5, 6, 7]
    fishman_style_range = [0, 3]
    weapon_range = [False, True]
    battle_skills_mastery_range = [0, 1, 2, 3, 4]
    special_ability_mastery_range = [0, 1, 2, 3]


class Character:
    def __init__(self, fruit=None, fraction=None, sea=None, haki=None,
                 race=None, style=None, fighting_mastery=None, weapon=None,
                 sword_mastery=None, gun_mastery=None, fruit_mastery=None):
        if haki is None:
            haki = [0, 0, 0, 0]
        if weapon is None:
            weapon = [False, False]
        self.__fruit = fruit
        self.__fraction = fraction
        self.__sea = sea
        self.__haki = haki
        self.__race = race
        self.__style = style
        self.__fighting_mastery = fighting_mastery
        self.__weapon = weapon
        self.__sword_mastery = sword_mastery
        self.__gun_mastery = gun_mastery
        self.__fruit_mastery = fruit_mastery
    
    #Fruit
    def set_fruit(self, fruit: int):
        if x_in_int_bounds(fruit, Data.fruit_range): self.__fruit = fruit

    def get_fruit(self):
        return self.__fruit

    def set_random_fruit(self):
        self.__fruit = random.randint(*Data.fruit_range)


    #Fraction
    def set_fraction(self, fraction: int):
        if x_in_int_bounds(fraction, Data.fraction_range): self.__fraction = fraction

    def get_fraction(self):
        return self.__fraction

    def set_random_fraction(self):
        self.__fraction = random.randint(*Data.fraction_range)


    #Sea
    def set_sea(self, sea: int):
        if x_in_int_bounds(sea, Data.sea_range): self.__sea = sea

    def get_sea(self):
        return self.__sea

    def set_random_sea(self):
        self.__sea = random.randint(*Data.sea_range)


    #Haki
    def set_haki(self, haki: list):
        if x_in_int_bounds(haki[0], Data.haki_range)\
                and x_in_int_bounds(haki[1], Data.special_ability_mastery_range)\
                and x_in_int_bounds(haki[2], Data.special_ability_mastery_range)\
                and x_in_int_bounds(haki[3], Data.special_ability_mastery_range):
            self.__haki[0] = haki[0]
            self.__haki[1] = haki[1]
            self.__haki[2] = haki[2]
            self.__haki[3] = haki[3]

    def get_haki(self):
        return self.__haki

    def set_random_haki(self):
        self.__haki[0] = random.randint(0, int(*random.choices(Data.haki_range, weights=(3, 2, 2, 1, 1))))
        self.__haki[1] = int(*random.choices(Data.special_ability_mastery_range, weights=(3, 3, 2, 1)))
        self.__haki[2] = int(*random.choices(Data.special_ability_mastery_range, weights=(3, 3, 2, 1)))
        self.__haki[3] = int(*random.choices(Data.special_ability_mastery_range, weights=(3, 3, 2, 1)))


    #Race
    def set_race(self, race: int):
        if x_in_int_bounds(race, Data.race_range):
            self.__race = race

    def get_race(self):
        return self.__race

    def set_random_race(self):
        self.__race = int(*random.choices(Data.race_range, weights=(5, 3, 3, 2, 1)))


    #Style
    def set_style(self, style: int):
        if self.__race == 1:
            if x_in_int_bounds(style, Data.fishman_style_range):
                self.__style = style
        elif self.__race == 0:
            if x_in_int_bounds(style, Data.rokushiki_range):
                self.__style = style
        else: print('This race has no special fighting styles')

    def get_style(self):
        return self.__style

    def set_random_style(self):
        if self.__race == 1:
            self.__style = random.choice(Data.fishman_style_range)
        elif self.__race == 0:
            self.__style = int(*random.choices(Data.rokushiki_range, weights=(3, 4, 2, 2, 2, 2, 1, 1)))


    #Fighting mastery
    def set_fighting_mastery(self, fighting_mastery: int):
        if x_in_int_bounds(fighting_mastery, Data.battle_skills_mastery_range):
            self.__fighting_mastery = fighting_mastery

    def get_fighting_mastery(self):
        return self.__fighting_mastery

    def set_random_fighting_mastery(self):
        self.__fighting_mastery = int(*random.choices(Data.battle_skills_mastery_range, weights=(3, 4, 2, 2, 1)))

    #Weapon
    def set_weapon(self, weapon: list):
        if x_in_int_bounds(weapon[0], Data.weapon_range) and x_in_int_bounds(weapon[1], Data.weapon_range)\
                and len(weapon) == 2:
            self.__weapon[0] = weapon[0]
            self.__weapon[1] = weapon[1]

    def get_weapon(self):
        return self.__weapon

    def set_random_weapon(self):
        self.__weapon[0] = random.choice(Data.weapon_range)
        self.__weapon[1] = random.choice(Data.weapon_range)


    #Sword mastery
    def set_sword_mastery(self, sword_mastery: int):
        if x_in_int_bounds(sword_mastery, Data.battle_skills_mastery_range):
            self.__sword_mastery = sword_mastery

    def get_sword_mastery(self):
        return self.__sword_mastery

    def set_random_sword_mastery(self):
        self.__sword_mastery = int(*random.choices(Data.battle_skills_mastery_range, weights=(2, 3, 2, 2, 1)))


    #Gun mastery
    def set_gun_mastery(self, gun_mastery: int):
        if x_in_int_bounds(gun_mastery, Data.battle_skills_mastery_range):
            self.__gun_mastery = gun_mastery

    def get_gun_mastery(self):
        return self.__gun_mastery

    def set_random_gun_mastery(self):
        self.__gun_mastery = random.choice(Data.battle_skills_mastery_range)


    #Fruit mastery
    def set_fruit_mastery(self, fruit_mastery: int):
        if x_in_int_bounds(fruit_mastery, Data.special_ability_mastery_range):
            self.__fruit_mastery = fruit_mastery

    def get_fruit_mastery(self):
        return self.__fruit_mastery

    def set_random_fruit_mastery(self):
        self.__fruit_mastery = int(*random.choices(Data.special_ability_mastery_range, weights=(3, 3, 2, 1)))


    #All character generator
    def generate_character(self):
        self.set_random_fruit()
        self.set_random_fraction()
        self.set_random_sea()
        self.set_random_race()
        self.set_random_style()
        self.set_random_haki()
        self.set_random_weapon()
        self.set_random_sword_mastery()
        self.set_random_gun_mastery()
        self.set_random_fruit_mastery()

    def show_character_data(self):
        print(f'{self.get_fruit()}\n'
              f'{self.get_fraction()}\n'
              f'{self.get_sea()}\n'
              f'{self.get_race()}\n'
              f'{self.get_style()}\n'
              f'{self.get_haki()}\n'
              f'{self.get_weapon()}\n'
              f'{self.get_sword_mastery()}\n'
              f'{self.get_gun_mastery()}\n'
              f'{self.get_fruit_mastery()}')

    def show_character(self):
        races = ['Human', 'Fishman', 'Mink', 'Giant', 'Lunarian']
        fractions = ['Pirate', 'Bounty hunter', 'Navy']
        seas = ['East Blue', 'South Blue', 'West Blue', 'North Blue', 'Paradise', 'New World']
        hakis = ['Has no haki', 'Buso haki', 'Ken haki', 'Buso and ken haki', 'All hakis']
        haki_masteries = ['Beginner', 'Experienced', 'Improved', 'Mastered']
        weapons = ['Has no weapon', 'Sword', 'Gun', 'Sword and gun']
        masteries = ['Has no mastery', 'Beginner', 'Experienced', 'Improved', 'Mastered']
        fruit_masteries = ['Beginner', 'Experienced', 'Awakened', 'Mastered']
        rokushiki_tecniques = ['Knows no rokushiki tecniques', 'Shigan', 'Geppo', 'Tekkai',
                               'Rokukyaku', 'Soru', 'Paper Arts', 'All rokushiki techniques']


        print(f'Devil fruit: {self.get_fruit()}')
        print(f'Fraction: {fractions[self.get_fraction()]}')
        print(f'Sea: {seas[self.get_sea()]}')


        print(f'Race: {races[self.get_race()]}')
        #print(f'Style: {rokushiki_tecniques[self.get_style()]}')

        print(f'Haki: {hakis[self.get_haki()[0]]}')
        if self.get_haki()[0] == 1:
            print(f'Buso haki mastery: {haki_masteries[self.get_haki()[1]]}')
        elif self.get_haki()[0] == 2:
            print(f'Ken haki mastery: {haki_masteries[self.get_haki()[2]]}')
        if self.get_haki()[0] == 3:
            print(f'Buso haki mastery: {haki_masteries[self.get_haki()[1]]}')
            print(f'Ken haki mastery: {haki_masteries[self.get_haki()[2]]}')
        elif self.get_haki()[0] == 4:
            print(f'Buso haki mastery: {haki_masteries[self.get_haki()[1]]}')
            print(f'Ken haki mastery: {haki_masteries[self.get_haki()[2]]}')
            print(f'Hao haki mastery: {haki_masteries[self.get_haki()[3]]}')


        print('Weapon: ', end='')
        if self.get_weapon()[0] is True and self.get_weapon()[1] is True:
            print(weapons[3])
        elif self.get_weapon()[0] is False and self.get_weapon()[1] is True:
            print(weapons[2])
        elif self.get_weapon()[0] is True and self.get_weapon()[1] is False:
            print(weapons[1])
        else:
            print(weapons[0])

        print(f'Sword mastery: {masteries[self.get_sword_mastery()]}')
        print(f'Gun mastery: {masteries[self.get_gun_mastery()]}')


        print(f'Devil fruit mastery: {fruit_masteries[self.get_fruit_mastery()]}')


class Area:
    def __init__(self):
        self.biom = 'Plain'
        self.landscape: str = None

    def random_area(self):
        self.biom = random.choice(['Plain', 'Forest', 'Desert', 'Sea', 'Mountain', 'Snow'])
        if self.biom != 'Sea':
            self.landscape = random.choices(['There are no buildings around',
                                            'There are some high buildings and columns around',
                                            'There are some low buildings around'], weights=(2, 1, 1))
        else:
            self.landscape = random.choices(['There are no buildings around',
                                            'There are some high peaks and columns around',
                                            'There are some little islands around'], weights=(2, 1, 1))

    def show_area(self):
        print(f'Biom: {self.biom}')
        if self.landscape is not None:
            print('Landscape: ', end='')
            print(*self.landscape)

def main():
    char = Character()
    char.generate_character()
    char.show_character()

    area = Area()
    area.random_area()
    area.show_area()

    input()

if __name__ == '__main__':
    main()

                            # Задание 6. 
from pprint import pprint

class OscarFilm:       # """ Задание 8. Пробелы заменил на табуляцию"""     

#Задание 6.1 Описать классами данные 
    def __init__(self, namefilm, year, raitingIMDB, long_min, genre,
    budget, cost):
        self.namefilm = namefilm
        self.year = year
        self.raitingIMDB = raitingIMDB
        self.long_min = long_min
        self.genre = genre
        self.budget = budget
        self.cost = cost 
        self.key = (namefilm, year, budget)
                            # Задание 6.1 Конец
    def __repr__(self):
        return "OscarFilm('%s',%s,%s)" % (self.namefilm, self.year,
                                          self.budget)
    
                    #""" Задание 8. Длину строки сделал не более 79 симолов"""

                            # Задание 6.2 Реализовать поиск по полям    
    def filter_suspense(self):
        if 'история' in self.genre or 'фантастика' in self.genre:
            print("История или фантастика есть в фильме " +self.namefilm)
            
        else:
            print ("Истории или фантастики нет в " +self.namefilm)
                            # Задание 6.2 Конец
                            # Задание 6.3 Реализовать нечеткий поиск.
                            # Бюджет картины около 20
    def filter_budget(self):
        if 16 <= self.budget <= 24:
            print("20 +- 20% составляет бюджет фильма " +self.namefilm)
                            # Задание 6.3 Конец       

    # filtered_data = filter_suspense(b)
    
WaterForm = OscarFilm("Форма воды", 2017, 6.914, 123, ['фантастика', 'драма'],
                      19.4, 195.243464)
MoonLight = OscarFilm("Лунный свет", 2016, 6.151, 110, ['драма'],
                      1.5, 65.046687)
AttentionCentre = OscarFilm("В центре внимания", 2015, 7.489, 129, ['драма',
                            'криминал', 'история'], 20.0, 88.346473)
Birdman = OscarFilm("Бёрдмэн", 2014, 7.604, 119, ['драма', 'комедия'], 18.0,
                    103.215094)
TwentyYearsSlave = OscarFilm("12 лет рабства", 2013, 7.71, 133, ['драма',
                            'биография', 'история'], 20.0, 178.371993)

#""" Задание 8. Длину строки сделал не более 79 симолов,
                                                    #но выглядит это не оч"""

WaterForm.filter_suspense()
MoonLight.filter_suspense()
AttentionCentre.filter_suspense()
Birdman.filter_suspense()
TwentyYearsSlave.filter_suspense()

WaterForm.filter_budget()
MoonLight.filter_budget()
AttentionCentre.filter_budget()
Birdman.filter_budget()
TwentyYearsSlave.filter_budget()



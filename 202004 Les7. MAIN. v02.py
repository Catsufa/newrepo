from pprint import pprint
import numpy as np
# from utils import compare, int_val # не получилось utils подстановкой файла в папку с библиотеками добавить. Поэтому int_val и compare вставил в текст программы
from itertools import product

ADDRESS_WORDS = {'дом','улица','живет'}
NAME_WORDS    = {'имя','зовут','фамилия'}
AGE_WORDS     = {'возраст', 'старше', 'младше'}

def compare(s1, s2):
    s1, s2 = [ s.lower() for s in [s1,s2] ]
    ngrams = [ s1[i:i+3] for i in range(len(s1)-1) ]
    count = 0
    for ngram in ngrams:
        count += s2.count(ngram)
    return count / max(len(s1),len(s2))

def int_val(s):
    try:
        return int(s)
    except ValueError:
        return 0

class Person:
    def __init__(self, name, surname, age, street, home, appartments):
        self.name, self.surname, self.age, self.street, self.home, self.appartments = name, surname, age, street, home, appartments
        self.key = (name, surname, street, home, appartments)
    
    def __repr__(self):
        return "Person('%s',%s,'%s')" % (self.name, self.age, self.street)
    
    def __eq__(self, obj):
        if type(obj) == Person:
            return (self.name, self.age, self.street) == (obj.name, obj.age, obj.street)
        elif type(obj) == str:
            return self.__fuzzy_compare(obj)
        else:
            return self.__repr__() == obj.__repr__()
        
    def __fuzzy_compare(self, query):
        def by_street(Q):
            Q = Q - ADDRESS_WORDS
            W = set(self.street.replace(',','').split())
            rez = []
            for a, b in product(Q, W):
                rez += [(compare(a,b),a,b)]
            return max(rez)[0]

        
            
        
        def by_name(Q):
            Q = Q - NAME_WORDS
            W = set(self.name.split())
            rez = []
            for a, b in product(Q, W):
                rez += [(compare(a,b),a,b)]

            return max(rez)[0]
        
        def by_age(Q):
            query_age = max([ int_val(q) for q in Q ])
            if 'старше' in Q:
                return query_age < self.age 
            if 'младше' in Q:
                return query_age > self.age 
            return query_age + 5 >= self.age >= query_age - 5
        
        q_words = set(query.split())
        score = 0
        for m_words, method in zip([ADDRESS_WORDS, NAME_WORDS, AGE_WORDS],
                                   [by_street,    by_name,    by_age]):
            if m_words & q_words:
                score += method(q_words)
                
        return score > 0.49

    
#Задание 7.2 Входные данные в видео были размещены через TAB и попали
#таким образом в тело класса. Это ошибка
    
lena = Person("Лена", "Головач", 19, "Пушкина", 14, 115)
natan = Person("Натан", "Головач-Добрый", 29, "Пушкина", 14, 115)
leonid = Person("Леонид", "Рыжиков", 27, "Ростова",  16,  15)
oleg = Person("Олег", "Вещий", 34, "Ленскoго", 10,  11)
olga = Person("Ольга", "Премудрая",  28, "Онегина",  11,  12)
nata = Person("Наташа", "Рыжикова", 17, "Ростова",  16,  15)

queries = [
    'имя Ольга', 
    'возраст 30', 
    'старше 20', 
    'младше 20', 
    'живет на Пушкина', 
    'дом 11',
    'фамилия ростова', #Задание 7.1 в этой строчке указан пример неподходящего запроса
    'имя  ростова', #Задание 7.1 в этой строчке указан пример неподходящего запроса
    'дом розовый', #Задание 7.1 в этой строчке указан пример неподходящего запроса
    'зовут ната',
]

people = {
    lena.key: lena,
    natan.key: natan,
    leonid.key: leonid,
    oleg.key: oleg,
    olga.key: olga,
    nata.key: nata,
}


for query, person in product(queries, people.values()):
    if person == query:
        pprint((query, person))

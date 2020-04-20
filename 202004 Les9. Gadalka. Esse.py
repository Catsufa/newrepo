"""
    Гадалка
"""
#Даниил добрый день. Начал писать Гадалку. Потом посмотрел уроки 10 и 11. ПОказалось - что уровень - просто отличный. Копипастить сразу не решился... может быть зря
# попробую реализовать модули fuzzy и memory. Но когда это произойдет, пока сказать не могу
# Еще вопрос - почем коммиты в Pastebin а не GitHub? как Вы нас учите

from random import randint # импорт модуля
prompt = "Ваш вопрос?"
answers = ("да","нет")
question = ""
while question != "стоп": # выход из цикла
    print(prompt, end = '')
    question = input() 
    answer = answers[randint(0,len(answers) - 1)]
    print(answer)

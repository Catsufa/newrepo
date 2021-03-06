import numpy as np
b = np.array ([
    ['Форма воды', 2017, 6.914, 123, ['фантастика', 'драма'], 19.4, 195.243464],
    ['Лунный свет', 2016, 6.151, 110, ['драма'], 1.5, 65.046687],
    ['В центре внимания', 2015, 7.489, 129, ['драма', 'криминал', 'история'], 20.0, 88.346473],
    ['Бёрдмэн', 2014, 7.604, 119, ['драма', 'комедия'], 18.0, 103.215094],
    ['12 лет рабства', 2013, 7.71, 133, ['драма', 'биография', 'история'], 20.0, 178.371993],
])


def filter_suspense(data):
    result = []
    for row in data:
        genres = row[4]
        if 'история' in genres or 'фантастика' in genres:
            result.append(row)
    return result

filtered_data = filter_suspense(b)


print (filtered_data)



def count_unique_words(words):
    unique_words = list(set(words))  # Отделяем уникальные слова из списка
    dictionary = {}
    for name in unique_words:  # Цикл на счетчик, name - это отдельное уникальное слово
        counter = []
        for i in range(0, len(words)):  # Цикл сравнивающий каждое слово из списка уникальных с оригинальным списком
            if words[i] == name:  # Если есть совпадение то добавляет +1 к счетчику этого уникального слова
                counter.append(i)
                dictionary[name] = len(counter)  # Добавляет значения в словарик "ключ" : кол-во
    return(dictionary)  # Возвращает словарь


count_unique_words(["foo", "bar", "baz", "bar", "bar"])

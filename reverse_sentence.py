# Первый вариант по требованиям


def reverse_sentence(sentence):
    words = sentence.split(' ')[::-1]  # Делим предложение по пробелам в обратном порядке в список
    words = ' '.join(words)  # Соединяем список обратно в предложение
    return(words)  # Возвращаем значение


reverse_sentence("мама мыла раму")


# Второй вариант с вводом с клавиатуры


def reverse_sentence_input(sentence):
    words = sentence.split(' ')[::-1]
    words = ' '.join(words)
    return(words)


inpt = input('Введите предложение: ')
reverse_sentence_input(inpt)

# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе
# несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.
# Стихотворение Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке
# и “Пам парам”, если с ритмом все не в порядке

# пара-ра-рам рам-пам-папам па-ра-па-дам

def vowels_count(S):
    vowels = list('а е ё и о у ы э ю я'.split())
    vowels_count = list()
    for i in S:
        count = 0
        for ch in i:
            if ch in vowels:
                count += 1
        vowels_count.append(count)
    return vowels_count


S = list("пара-ра-рам рам-пам-папам па-ра-па-дам".split())
print("Парам пам-пам" if len(set(vowels_count(S))) == 1 else "Пам парам")

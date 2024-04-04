import random

def z1():
    a = list(random.sample(range(1,9), k=5))
    b = list(input("Введите число: "))
    if b in a:
        print("Поздравляю, Вы угадали числo!")
    else:
        print ("Нет такого числа!")
    print( "Были загаданы числа: ", a)

def z2():
    my_list = list(random.choices(range(1,9), k=5))
    print("Были загаданы числа: ", my_list)
    b = list()
    c = 0
    for i in my_list:
        if i in b:
            print("Повторяющийся элемент: ", i)
            c += 1
        else:
            b.append(i)
    if c == 0:
        print("Повторений нет")

def z3():
    dw = ('пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс')
    wd_input = input("Какие дни вы хотите выходными: ")
    wd = wd_input.split(' ')
    print(wd)
    wd_list = []
    w_list = []
    for i in dw:
        if i in wd:
            wd_list.append(i)
        else:
            w_list.append(i)
    print(wd_list)
    print("Ваши выходные дни: ", ', '.join(reversed(wd_list)), " - ", len(wd_list), "дня")
    print("Ваши рабочие дни: ", ', '.join(w_list), " - ", len(w_list), "дней")

def z4():
    g1 = ['Гилязова', 'Горбунов', 'Епифанова', 'Иванов', 'Калинин', 'Королева', 'Криштал', 'Крючкова', 'Мельников', 'Тугова']
    g2 = ['Зайцев', 'Белов', 'Григорьев', 'Тарасов', 'Орлов', 'Макаров', 'Андреев', 'Киселев', 'Максимов', 'Федоров']

    t1 = random.sample(g1, 5)
    t2 = random.sample(g2, 5)
    s = tuple(t1 + t2)
    sort = tuple(sorted(s))

    print("Группа 1: ", ', '.join(g1))
    print("Группа 2: ", ', '.join(g2))
    print("Спортивная команда: ", ', '.join(s))
    print("Длина кортежа:", len(s))
    print("Отсортированная команда: ", ', '.join(sort))

    ivanov = s.count('Иванов')
    if ivanov > 0:
        print("Студент Иванов входит в команду.")
        print("Количество раз, которое фамилия Иванов встречается в команде:", ivanov)
    else:
        print("Студент Иванов не входит в команду.")

z4()

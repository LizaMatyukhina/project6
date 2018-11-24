def finding_name(line):
    return line[5:len(line)]


def finding_height(lines):
    for i in range(0, len(lines)):
        line = lines[i]
        if line[0:4] == 'Рост':
            height = int(line[6:9])
    return height


def finding_weight(lines):
    for i in range(0, len(lines)):
        line = lines[i]
        if line[0:3] == 'Вес':
            weight = int(line[5:7])
    return weight


def finding_index(height=180, weight=85):
    index = round((weight / ((height / 100) ** 2)), 1)
    return index


def finding_calories(index):
    if index < 17.5:
        calories = 'потреблять очень большое количество каллорий из-за недостатка веса'
    elif 17.5 < index < 25.9:
        calories = 'потреблять 1800-2000 ккал в день'
    elif 26 < index < 30.9:
        calories = 'потреблять 1500-1800 ккал в день для снижения веса'
    else:
        calories = 'срочно обратиться за помощью к врачу'
    return calories


def finding_year(line):
    year = int(line[0:4])
    return year


def finding_ill(text):
    count = 0
    for i in range(1994, 2019):
        count1 = 0
        for k in range(6, len(text)):
            year1 = finding_year(text[k])
            if year1 == i:
                count1 += 1
        if count1 > count:
            count = count1
            year = i
    return year, count


def main():
    try:
        with open("card.txt") as f_in:
            text = f_in.readlines()
            name = finding_name(text[0])
            index = finding_index(finding_height(text), finding_weight(text))
            print('Индекс массы твоего тела равен {}.'.format(index))
            calories = finding_calories(index)
            print('Это значит, что тебе следует {}.'.format(calories))
            year = finding_ill(text)
            print('Больше всего раз в своей жизни ты болел в {} году.'.format(year[0]))
            print('Тогда ты заболел {} раза.'.format(year[1]))
    except FileNotFoundError:
        print('Твоя мед. карта не была найдена:(')


if __name__ == '__main__':
    main()

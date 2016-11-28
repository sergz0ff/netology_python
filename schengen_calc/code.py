RESIDENCE_LIMIT = 90
SCHENGEN_CONSTRAINT = 180

first_of_january = 1  # первое января текущего года

running_program = True

visits = []

# visits = [[1, 10], [21, 30], [45, 46], [251, 260], [300, 305]]

def clear_visits():
    global visits
    visits = []

def read_visits():
    with open('dates.txt') as doc:
        temp_list = []
        for line in doc:
            temp_list.append(int(line.strip()))
        for i in range(0, len(temp_list), 2):
            visits.append(temp_list[i:i + 2])

def write_visits(visits):
    with open('dates.txt', 'w') as doc:
        for i in range(len(visits)):
            for j in range(len(visits[i])):
                doc.write(str(visits[i][j]) + '\n')

def sort_visits():
    visits.sort(key=lambda i: i[1])

def check_new_visit(new_visit):
    if new_visit[0] > new_visit[1]:
        print('Ошибка в поездке')
        raise Exception('Ошибка даты поездки, выезд раньше въезда', new_visit)

def check_date_intersection():
    for visit in visits:
        for check_range_visit in visits:
            if visit == check_range_visit:
                continue
            elif visit[0] <= check_range_visit[1] and visit[1] >= check_range_visit[0]:
                raise Exception('Ошибка даты поездки, следующие даты пересекаются', visit, check_range_visit)

def print_visits():
        print('Список поездок: {} '.format(visits))

def add_visit():
    print_visits()
    arrival = input('Введите дату приезда:\n')
    departure = input('Введите дату отъезда:\n')
    if arrival.isdigit() and departure.isdigit():
        new_visit = [int(arrival), int(departure)]
        check_new_visit(new_visit)
        visits.append(new_visit)
        write_visits(visits)
        sort_visits()
        check_date_intersection()
        days_in_eu = []
        total_time_in_es = 0
        for visit in visits:
            past_days = 0
            for past_visit in visits:
                if visit[0] >= past_visit[0] > visit[0] - SCHENGEN_CONSTRAINT:
                    past_days += past_visit[1] - past_visit[0] + 1
            days_in_eu.append(past_days)
            total_time_in_es += visit[1] - visit[0] + 1

        for visit, days in zip(visits, days_in_eu):
            if days > RESIDENCE_LIMIT:
                print('В течение поездки', visit, 'вы пребывали в ЕС слишком долго:', days)

        if total_time_in_es > RESIDENCE_LIMIT:
            print('Вы не можете прибывать в ЕС так долго')

        print('Вы пробудете в ЕС дней:', total_time_in_es)
    else:
        print('Целое число, которое больше нуля!!!')
        add_visit()
    clear_visits()

def predict_visit():
    print_visits()
    future_date = int(input('Введите дату будущей поездки: \n'))
    days_in_eu_in_constraint = []
    if future_date <= visits[len(visits) - 1][1]:
        raise Exception(
            'Ошибка, дата очередной поездки должна быть позднее последней даты выезда. Последняя дата выезда:',
            visits[len(visits) - 1][1])
    temp_end_180 = visits[0][0] + 180 - 1
    while future_date > temp_end_180:
        temp_end_180 += 180
    for visit in visits:
        if visit[0] >= temp_end_180 - 180 and visit[1] in range(visit[0], temp_end_180 + 1):
            days_in_eu_in_constraint.append(visit)
    total_days_in_period = 0
    for day in days_in_eu_in_constraint:
        total_days_in_period += day[1] - day[0] + 1
    available_days = RESIDENCE_LIMIT - total_days_in_period
    print('У вас в запасе:', available_days, 'дней')
    clear_visits()

def remove_visit():
    print_visits()
    killing_date = input('Введите дату из поездки, которую нужно удалить:\n')
    if killing_date.isdigit():
        for visit in visits:
            killing_date = int(killing_date)
            if killing_date == visit[0] or killing_date == visit[1]:
                visits.remove(visit)
        write_visits(visits)
        print('Теперь список поездок выглядит так: {} '.format(visits))
    else:
        print('Целое число, которое больше нуля!!!')
        remove_visit()
    clear_visits()

def stop_program():
    print('Программа завершена.\nДо скорых встреч!')
    global running_program
    running_program = False

function_table = {
    'v': add_visit,
    'p': predict_visit,
    'r': remove_visit,
    'e': stop_program
}

while running_program:
    read_visits()
    print(
        'Шенгенский калькулятор \n Меню программы:\n v - ввести новый визит\n p - ввести дату будущего визита\n r - удалить визит\n e - выход')
    option = input('Введите команду:\n').lower()
    if option not in function_table.keys():
        print("Нет такой команды!")
        continue
    function_table[option]()

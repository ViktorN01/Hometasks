days = 1
start_km = int(input('Введите пройденное растояние: '))
finish = int(input('Введите цель дистанции: '))
if start_km <= 0 or finish <= 0:
    print('Расстояние должно быть больше нуля!')
else:
    while start_km < finish:
        start_km += start_km * 0.1
        days += 1
    print(f'Спортсмен преодолеет дистанцию за {days} дней')

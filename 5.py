hours, minute, seconds = int(input('Введите кол - во часов: ')), int(input('Введите кол - во минут: ')), int(input('Введите кол - во секунд: '))
time = hours * 60 * 60 + minute * 60 + seconds
print(f'Время в пути в секундах: {time} с')

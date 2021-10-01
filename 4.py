time = input('Введите время в пути в формате часы:минуты:секунды ')
s = [int(i) for i in time.split(':')]
time_second = s[0] * 60 * 60 + s[1] * 60 + s[2]
print(f'Время в пути в секундах: {time_second}с')

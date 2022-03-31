duration = int(input('введите целое число: '))
minute = 60
hour = 3600
day = 86400
if duration <= 60:
    print(duration, 'сек')
elif duration <= 3600:
    print(duration // minute, 'мин', duration % minute , 'сек')
elif duration <= 86400:
    print(duration // hour, 'час', (duration % hour) // minute, 'мин', (duration % hour) % minute, 'сек')
elif duration >86400:
    print(duration // day, 'дн', (duration % day) //hour, 'час', ((duration % day) % hour) // minute, 'мин', ((duration % day) % hour) % minute, 'сек')
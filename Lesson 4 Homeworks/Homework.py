name = input('Привет! Как тебя зовут?  ')
age = int(input('Сколько тебе лет? '))

message = ''

if not name:
    message += 'Ошибка! Пустое имя.\n'
elif len(name) < 3 and name.lower != 'ян':
    message += 'Ошибка! В имени меньше 3 символов.\n'

if age <= 0:
    message += 'Ошибка! Ваш возраст не может быть меньше или равен нулю.'
elif age < 14:
    message += 'Ошибка! Минимальный возраст 14 лет.'

if not message:
    message += f'Привет {name.title()}! Тебе {age} лет. '

    if age in (16, 17):
        message += 'Тебе нужно получить первый паспорт'
    elif age in (25, 26):
        message += 'Тебе нужно заменить паспорт'
    elif age in (45, 46):
        message += 'Тебе нужно заменить паспорт второй раз'

print(message)

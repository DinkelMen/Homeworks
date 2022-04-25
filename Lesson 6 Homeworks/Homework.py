def validate_name(name: str) -> str:
    """ В этой функции имя проверяется на то что оно пустое, слишком короткое
    и содержит внутри себя более 1 пробела. При отсуствии ошибок выводит пустую строку

    """

    if not name:
        return 'Ошибка: пустое имя. Введите имя.'
    if len(name) < 3 and name.lower() != 'ян':
        return 'Ошибка: Имя слишком короткое. Введите имя больше 2 букв.'
    if name.count(' ') > 1:
        return 'Ошибка: В имени допускается только 1 пробел.'
    else:
        return ''


def validate_age(age: int) -> str:
    """ В этой функции возраст проверяется на то что он пустой, меньше либо равен нулю и больше 13 лет"""

    if not age:
        return 'Ошибка: не указан возраст'
    if age <= 0:
        return 'Ошибка: возраст не может быть меньше или равен нулю.'
    if age < 14:
        return 'Ошибка: вам должно быть 14 и более лет.'
    else:
        return ''


def passport_advice(age: int) -> str:
    """ В этой функции проверяется возраст на предмет необходимости выполнения каких-либо действия с паспортом"""

    if age in (16, 17):
        return 'Тебе нужно получить первый паспорт'
    if age in (25, 26):
        return 'Тебе нужно заменить паспорт'
    if age in (45, 46):
        return 'Тебе нужно заменить паспорт второй раз'
    else:
        return ' '


def cleaning_func(name, age):

    """ В этой функции вводимые данные очищаются от лишних пробелов в начале и конце"""

    return [name.strip(), int(age.strip())]


def main_func():

    """ Эта функция осуществляет вызовы всех остальных функций, ввод данных и прочее"""

    message = ' '
    while message != '' '':
        name = input('Введите ваше имя: ')
        age = input('Введите ваш возраст: ')
        clean = cleaning_func(name, age)
        message = validate_name(clean[0]) + validate_age(clean[1])
        if message == '' '':
            print(f'Привет! Тебя зовут {clean[0]}. Тебе {clean[1]} лет. {passport_advice(clean[1])}')
        else:
            print(validate_name(clean[0]), validate_age(clean[1]))


main_func()

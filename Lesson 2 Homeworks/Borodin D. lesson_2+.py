# Пункт 1
list1 = ['123', 456, [], ()]
print('Пункт 1: ', list1)

# Пункт 2
list1[0] = int(list1[0])
print('Пункт 2: ', list1)

# Пункт 3
list1[1] = str(list1[1])
print('Пункт 3: ', list1)

# Пункт 4
list1[2].append(2**8)
print('Пункт 4: ', list1)

# Пункт 5
list1[3] = (2**10 % 2 == 0,)
print('Пункт 5: ', list1)

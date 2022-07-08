# 3 переменные с одинаковым данными и ID
item1 = '123'
item2 = '123'
item3 = '123'
print(id(item1) == id(item2) == id(item3))

# 2 переменные с одинаковыми данными с разным ID
item5 = [123]
item6 = [123]
print(id(item5) == id(item6))

# У первых трёх переменных разные идентификаторы, а у 2х последних одинаковые(При одинаковых данных)
item7 = [123]
item8 = [123]
item9 = [123]
print(id(item7) == id(item8))
print(id(item8) == id(item9))
print(id(item7) == id(item9))

item10 = 123
item11 = 123
print(id(item10) == id(item11))

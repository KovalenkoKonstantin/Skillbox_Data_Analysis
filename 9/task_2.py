# Существует мессенджер,
# в котором иногда возникают неполадки при передаче сообщений:
# в них попадает лишний символ — звёздочка.
# Пользователям это надоело,
# поэтому они стали уходить в другие сервисы.
# Но один из них заинтересовался,
# на каких позициях обычно появляется звёздочка.
# Чтобы выяснить это, пользователю необходимо подготовить строки,
# в которых символ «*» встречается ровно один раз.

# Что нужно сделать:

# Напишите программу, которая определяет порядковый номер звёздочки в строке.

# Пример:

# Введите текст: «Пр*ивет как дела».
# Символ «*» стоит на позиции 3.

# in_word = "Пр*ивет как дела"
## 1
# in_word = input('input prompt word: ')
# for index, symbol in enumerate(in_word,  1):
#     if symbol == '*':
#         print(f'The "*" symbol is at the position {index}.')

## 2
# in_word = input('input prompt word: ')
# index = in_word.find('*')
# print(f'The "*" symbol is at the position {index + 1}')

## 3
count = 0
in_word = input('input prompt word: ')
for symbol in in_word:
    count += 1
    if symbol == '*':
        break
print(f'The "*" symbol is at the position {count}')

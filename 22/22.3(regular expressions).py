print('\\\\par')

import re

# \d	Любая цифра
# \D	Любой символ, кроме цифры
# r, скажет питону «не рассматривай \ как экранирующий символ
match = re.search(r'\d\d\D\d\d', r'Телефон 123-12-12')
print(match[0] if match else 'Not found')
# -> 23-12
match = re.search(r'\d\d\D\d\d', r'Телефон 1231 212')
print(match[0] if match else 'Not found')
# -> 31 21

match = re.fullmatch(r'\d\d\D\d\d', r'12-12')
print('YES' if match else 'NO')
# -> YES
match = re.fullmatch(r'\d\d\D\d\d', r'Т. 12-12')
print('YES' if match else 'NO')
# -> NO

# \w	Любая буква (то, что может быть частью слова), а также цифры и _
# \W	Любая не-буква, не-цифра и не подчёркивание
# {m,n}	От m до n повторений включительно
# +	Одно или более, синоним {1,}
print(re.split(r'\W+', 'Where, say to me, is my glasses??!'))
# -> ['Where', 'say', 'to', 'me', 'is', 'my', 'glasses', '']

# {n}	Ровно n повторений
print(re.findall(r'\d{2}\.\d\d\.\d{4}',
                 r'This string write 19.01.2018, but can be 01.09.2017'))
# -> ['19.01.2018', '01.09.2017']

for m in re.finditer(r'\d\d\.\d\d\.\d{4}', r'This string is 19.01.2018, but it can be 01.09.2017'):
    print('Data', m[0], 'starts with position', m.start())
# -> Data 19.01.2018 starts with position 15
# -> Data 01.09.2017 starts with position 41

print(re.sub(r'\d\d\.\d\d\.\d{4}',
             r'DD.MM.YYYY',
             r'This string is 19.01.2018, but it can be 01.09.2017'))
# -> This string is DD.MM.YYYY, but it can be DD.MM.YYYY

# заменим каждый пятый символ предложения, начиная с 0-го, на *
text = "Это не те дроиды, которых вы ищете"
new_text = ""
for char in enumerate(text):
    if char[0] % 5 == 0:
        new_text += '*'
    else:
        new_text += char[1]
print(new_text)

for i in range(3):
    print(f"iteration # {i + 1}")

str = 'abcdef'
for i in str:
    print(i[0], end='')

print()

str = 'abcdef'
for i in range(len(str)):
    print(str[i], end='')

s = 'a1b2c3d4e5f6g7h8'
for i in range(0, len(s), 2):
    print(s[i], end='')

print()

s = 'a1b2c3d4e5f6g7h8'
for i in enumerate(s):
    print(i[1], end='')

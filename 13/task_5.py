# Известно, что амплитуда качающегося маятника с каждым разом затухает
# на 8,4% от амплитуды прошлого колебания.
# Если качнуть маятник,
# то, строго говоря, он не остановится никогда,
# просто амплитуда будет постоянно уменьшаться до тех пор,
# пока мы не сочтём такой маятник остановившимся.

# Напишите программу,
# определяющую, сколько раз качнётся маятник,
# прежде чем он, по нашему мнению, остановится.

# Программа получает на вход
# начальную амплитуду колебания в сантиметрах
# и конечную амплитуду его колебаний,
# которая считается остановкой маятника.

# Обеспечьте контроль ввода.

# Пример:

# Введите начальную амплитуду: 1
# Введите амплитуду остановки: 0.1

# Маятник считается остановившимся через 27 колебаний

def calculate_oscillation(initial_amplitude, stop_amplitude):
    if initial_amplitude <= stop_amplitude:
        return 'Конечная амплитуда должна быть меньше начальной.'

    oscillation = 0
    current_amplitude = initial_amplitude

    while current_amplitude > stop_amplitude:
        current_amplitude *= 0.916  # (100-8,4)/100
        oscillation += 1

    return oscillation


def main():
    while True:
        try:
            initial_amplitude = float(input('Введите начальную амплитуду: '))
            stop_amplitude = float(input('Введите амплитуду остановки: '))
            print()
            result = calculate_oscillation(initial_amplitude, stop_amplitude)
            print(f'Маятник считается остановившимся через  {result} колебаний')
            break
        except ValueError:
            print('Неправильное значение.')


main()

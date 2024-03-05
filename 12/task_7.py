# Вы пришли на работу в контору по разработке игр,
# целевая аудитория которых - дети и их родители.
#
# У прошлого программиста было задание
# сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
#
# Однако программист, на место которого вы пришл
# и, перед увольнением не успел сделать эту задачу
# и оставил только небольшой шаблон проекта.
#
# Используя этот шаблон,
# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
#
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
#
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
#
# Правила игры “Угадай число”:
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.
import random


def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    user_choice = int(input('Enter your choice (1. rock, 2. paper, 3. scissors): '))
    computer_choice = random.randint(1, 3)

    while user_choice == computer_choice:
        print('One more!')
        user_choice = int(input('Enter your choice (1. rock, 2. paper, 3. scissors): '))
        computer_choice = random.randint(1, 3)

    print(f'Your choice: {user_choice} - {choices[user_choice - 1]}')
    print(f"Computer's choice: {computer_choice} - {choices[computer_choice - 1]}")

    if (user_choice == 1 and computer_choice == 3) \
            or (user_choice == 3 and computer_choice == 2) \
            or (user_choice == 2 and computer_choice == 1):
        print('You win!')
        print()
    else:
        print('Computer wins!')
        print()


def guess_the_number():
    target_number = random.randint(1, 100)
    guess = None
    attempts = 0

    while guess != target_number:
        guess = int(input('Guess the number (1-100): '))
        attempts += 1

        if guess < target_number:
            print('Too low!')
        elif guess > target_number:
            print('Too high!')

    print(f'Congratulations! You guessed the number {target_number}')
    print(f'Number of attempts: {attempts}')
    print()


def main_menu():
    while True:
        print('1. Rock, Paper, Scissors')
        print('2. Guess the Number')
        print('3. Exit')
        print()
        try:
            choice = int(input('Enter your choice (1-3): '))

            if choice == 1:
                rock_paper_scissors()
            elif choice == 2:
                guess_the_number()
            elif choice == 3:
                break
            else:
                print('Invalid choice. Please try again.')
        except ValueError:
            print('Invalid choice. Please try again.')
            print()


main_menu()

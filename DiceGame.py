import time
from random import randint

# moves_and_wins = {
#     '2': '1',                      Not used
#     '3': '1' or '2',
#     '4': '1' or '2' or '3',
#     '5': '1' or '2' or '3' or '4',
#     '6': '1' or '2' or '3' or '4' or '5',
# }


again_last_ask = ['yes', 'да']
while again_last_ask != 'нет':
    name = input("What's your name? // Как вас зовут? ")
    Welcome = input(name + ', Are you ready to start // Вы готовы начать игру? ').lower()

    if Welcome == 'yes' or 'да':  # If user ready to start - code is start run.Если пользователь готов-код запускается
        print('Throwing the dice // Кидаем кости...')
    elif Welcome == 'no' or 'нет':
        print('All is good! Goodbye. // Хорошо! До встречи.')
        break

    for i in range(1, 6):  # The visual part. Output of progress execution // Отброс цифр, типа прогресс
        time.sleep(0.2)
        print(i)

    moves = ['1', '2', '3', '4', '5', '6']  # Choosing a random number for dice
    computer_move = randint(1, 6)
    print('Computer has rolled // Компьютеру выпало:', computer_move)
    player_move = randint(1, 6)
    print('You roll a // Вам выпало:', player_move)

    if player_move > computer_move:
        print('You win! // Вы победили!')

    elif player_move == computer_move:
        print("It's a tie // У вас ничья!")

    else:
        print('You lose :( // Вы проиграли :(')

    again = input('Сыграем еще? ').lower()

    if again not in again_last_ask:
        print('Спасибо за игру! До свидания! ')
        break

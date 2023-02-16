import random
import time
from random import randint

# moves_and_wins = {
#     '2': '1',                      Not used
#     '3': '1' or '2',
#     '4': '1' or '2' or '3',
#     '5': '1' or '2' or '3' or '4',
#     '6': '1' or '2' or '3' or '4' or '5',
# }


again = 'да'
Welcome_phrases = ['Нет']
while again != 'нет':
    name = input('Как вас зовут? ')
    Welcome = input(name + ', вы готовы начать игру? ').lower()
    if Welcome == 'нет':
        print('Хорошо! До встречи.')
        break
    if Welcome == 'Lf' or Welcome_phrases:
        print('Кидаем кости...')
    for i in range(1, 6):
        time.sleep(0.2)
        print(i)

    moves = ['1', '2', '3', '4', '5', '6']

    computer_move = randint(1, 6)
    print('Компьютеру выпало:', computer_move)
    player_move = randint(1, 6)
    print('Вам выпало:', player_move)

    if player_move > computer_move:
        print('Вы победили!')

    elif player_move == computer_move:
        print('у вас ничья!')

    else:
        print('Вы проиграли :(')

    again = input('Сыграем еще? ').lower()

if again == 'нет':
    print('Спасибо за игру! До свидания! ')

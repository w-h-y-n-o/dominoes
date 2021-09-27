import random

# Список всех домино
all = [[2, 5], [1, 2], [3, 6], [0, 0], [0, 2], [5, 6], [3, 5], [2, 4], [3, 4], [1, 5], [0, 4], [2, 6], [3, 3], [1, 1],
       [1, 4], [1, 3], [2, 3], [4, 5], [2, 2], [0, 3], [0, 6], [5, 5], [4, 4], [4, 6], [0, 1], [0, 5], [1, 6], [6, 6]]
random.shuffle(all)  # Перетасовка всего списка домино
# Запасные домино
stock = []
for el in all:
    stock.append(el)
    all.remove(el)
    if el == all[13]:
        break
el = 0
# Набор домино компьютера
computer = []
for el in all:
    computer.append(el)
    all.remove(el)
    if el == all[6]:
        break
el = 0
# Оставшиеся домино для игрока
player = []
for i in range(7):
    player.append(all[0])
    all.pop(0)
# Проверка на дубль у компьютера
# snake - начальная доминошка
max1 = 0
max2 = 0
i = 0
ii = 0
for el in computer:
    if el[0] == el[1]:
        if el[0] > max1:
            max1 = el[0]
            ii = i
    i += 1
i = 0
el = 0
# Проверка на дубль у игрока
j = 0
jj = 0
for el in player:
    if el[0] == el[1]:
        if el[0] > max2:
            max2 = el[0]
            jj = j
    j += 1
j = 0
el = 0
snake = []
if max1 > max2:
    snake.append(computer[ii])
    computer.remove(computer[ii])
else:
    snake.append(player[jj])
    player.remove(player[jj])
# Случай, когда дубль не нашёлся и нужно определить самую большую доминошку
smax1 = 0
smax2 = 0
i = 0
if not snake:
    for el in computer:
        s1 = el[0] + el[1]
        if s1 > smax1:
            smax1 = s1
            ii = i
        i += 1
    el = 0
    j = 0
    for el in player:
        s2 = el[0] + el[1]
        if s2 > smax2:
            smax2 = s2
            jj = j
        j += 1
    if smax1 > smax2:
        snake.append(computer[ii])
        computer.remove(computer[ii])
    else:
        snake.append(player[jj])
        player.remove(player[jj])


def desk(stock, computer, player, snake):
    print('======================================================================')
    print('Stock size:', len(stock))
    print('Computer pieces:', len(computer))
    if len(snake) > 6:
        print(snake[0], snake[1], snake[2], '...', snake[-3], snake[-2], snake[-1], sep='')
    else:
        print(*snake)
    print('Your pieces:')
    i = 1
    for el in player:
        print(f'{i}: {el}')
        i += 1
    # Определить, кто пойдёт первым
    if len(computer) > len(player):
        Status = 'computer'
    elif len(computer) < len(player):
        Status = 'player'
    else:
        Status = 0
    return Status


def put_p():
    while True:
        st_p = input()
        try:
            st_p = int(st_p)
            if -len(player) <= st_p <= len(player):
                break
            else:
                print('Invalid input. Please try again.')
        except ValueError:
            print('Invalid input. Please try again.')
    return st_p


def put_c(snake, computer):
    o_snake = []
    for el in range(len(snake)):
        o_snake.append(snake[el][0])
        o_snake.append(snake[el][1])
    o_computer = []
    for ell in range(len(computer)):
        o_computer.append(computer[ell][0])
        o_computer.append(computer[ell][1])

    # Рассчёт редкости каждого числа
    score = []
    for i in range(7):
        score.append(o_snake.count(i) + o_computer.count(i))

    # Рассчёт баллов для каждой доминошки
    ball = []
    for l in computer:
        ball.append(score[l[0]] + score[l[1]])

    # Отсртировнный список ball, где по убыванию стоят номера доминошек с самым высоким баллом
    ball_sort = []
    for n in range(len(computer)):
        ball_sort.append(ball.index(max(ball)) + 1)
        ball[ball.index(max(ball))] = -1
    return ball_sort


status = desk(stock, computer, player, snake)


def step(status, stock, computer, player, snake):
    if status == 'computer':
        print('Status: Computer is about to make a move. Press Enter to continue...')
        a = input()
        ball = put_c(snake, computer)
        for i in ball:
            st_c = i
            if computer[st_c - 1][0] == snake[-1][1]:
                snake.append(computer.pop(st_c - 1))
                break
            elif computer[st_c - 1][1] == snake[-1][1]:
                computer[st_c - 1][0], computer[st_c - 1][1] = computer[st_c - 1][1], computer[st_c - 1][0]
                snake.append(computer.pop(st_c - 1))
                break
            st_c = -st_c
            if computer[abs(st_c) - 1][0] == snake[0][0]:
                computer[abs(st_c) - 1][0], computer[abs(st_c) - 1][1] = computer[abs(st_c) - 1][1], \
                                                                         computer[abs(st_c) - 1][0]
                snake.insert(0, computer.pop(abs(st_c) - 1))
                break
            elif computer[abs(st_c) - 1][1] == snake[0][0]:
                snake.insert(0, computer.pop(abs(st_c) - 1))
                break
            elif i == ball[-1]:
                if len(stock) != 0:
                    computer.append(stock.pop(0))
                break
        status = 'player'
    else:
        print("Status: It's your turn to make a move. Enter your command.")
        while True:
            st_p = put_p()
            if st_p > 0:
                if player[st_p - 1][0] == snake[-1][1]:
                    snake.append(player.pop(st_p - 1))
                    break
                elif player[st_p - 1][1] == snake[-1][1]:
                    player[st_p - 1][0], player[st_p - 1][1] = player[st_p - 1][1], player[st_p - 1][0]
                    snake.append(player.pop(st_p - 1))
                    break
            elif st_p < 0:
                if player[abs(st_p) - 1][0] == snake[0][0]:
                    player[abs(st_p) - 1][0], player[abs(st_p) - 1][1] = player[abs(st_p) - 1][1], player[abs(st_p) - 1][0]
                    snake.insert(0, player.pop(abs(st_p) - 1))
                    break
                elif player[abs(st_p) - 1][1] == snake[0][0]:
                    snake.insert(0, player.pop(abs(st_p) - 1))
                    break
            elif st_p == 0:
                if len(stock) != 0:
                    player.append(stock.pop(0))
                break
            print('Illegal move. Please try again.')
        status = 'computer'

    # Проверка условия окончания игры
    if len(computer) == 0:
        status = 'lose'

    if len(player) == 0:
        status = 'win'

    # Проверка условия ничьи
    draw = []
    for el in range(len(snake)):
        draw.append(snake[el][0])
        draw.append(snake[el][1])
    if (draw[0] == draw[-1]) and (draw.count(draw[0]) == 8):
        status = 'draw'

    desk(stock, computer, player, snake)
    return status


status = step(status, stock, computer, player, snake)
while (status == 'computer') or (status == 'player'):
    status = step(status, stock, computer, player, snake)

if status == 'lose':
    print('Status: The game is over. The computer won!')
elif status == 'win':
    print('Status: The game is over. You won!')
elif status == 'draw':
    print("Status: The game is over. It's a draw!")

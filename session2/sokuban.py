player_x = 1
player_y = 1
playing = True
while playing :
    for y in range(5):
        map = ''
        for x in range(5):
            if x == player_x and y == player_y:
                map = map +'P '
            elif x == 3 and y == 3:
                map = map +'B '
            else:
                map = map +'- '
        print(map)
    move = input('Your move?(wasd)')
    if move == 'w':
        player_y = player_y-1
    elif move == 's':
        player_y = player_y+1
    elif move == 'a':
        player_x = player_x+1
    elif move == 'd':
        player_x = player_x-1
    else:
        print('xin moi nhap lai')

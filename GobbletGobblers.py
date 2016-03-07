screen = ['  '] * 10
hidden_screen = [[] for i in range(10)]
weights = [0]*10
blue_small = 2
blue_medium = 2
blue_large = 2
orange_small = 2
orange_medium = 2
orange_large = 2
active_game = True
active_player = 'Blue'


def printscreen():
    print('-------------------')
    print('      |      |')
    print('7:' + screen[7] + '  |8:' + screen[8] + '  |9: ' + screen[9])
    print('      |      |')
    print('-------------------')
    print('      |      |')
    print('4:' + screen[4] + '  |5:' + screen[5] + '  |6: ' + screen[6])
    print('      |      |')
    print('-------------------')
    print('      |      |')
    print('1:' + screen[1] + '  |2:' + screen[2] + '  |3: ' + screen[3])
    print('      |      |')
    print('-------------------')

def bluePlayerMove():
# Let the player type in their move.
    print('-------------------')
    print ('Player ', active_player, 'is now playing!')
    valid_move = False
    move_made = False
    
    while valid_move == False:
        if (blue_small > 0 or blue_medium > 0 or blue_large > 0):
            new_obj_answer = input ('Do you wish to move a new object in the screen? (Y/N)')
            if new_obj_answer in ['Y' , 'y']:
                move_made = True
                print ('Please select what kind of object you wish to move into the screen. You have ', blue_small, 'Blue Small objects, ', blue_medium,
                       'Blue Medium objects and ', blue_large, ' Blue Large objects. Please type BS (Blue SMALL) or BM (Blue Medium) or BL (Blue Large):  ' )
                selected_obj = input ()
                if selected_obj in ['BS' , 'BM' , 'BL']:
                    if check_obj_quantity (selected_obj) == False:
                        print ('You do not have any ' , selected_obj , ' available out of the screen!' )
                    else:
                        print ('Enter the number of the cell that you want to move your', selected_obj, 'object to:')
                        selected_cell = input ()
                        if selected_cell in ['1' , '2' , '3' , '4' , '5' , '6', '7' , '8' , '9']:
                            valid_move = check_move (selected_obj, selected_cell)
                            if valid_move == True:
                                make_move_new_obj(selected_obj, selected_cell)
        if (move_made == False) and (obj_exists_in_screen('B')):
            print ('Please move an object in the screen to a new cell' )
            source_cell = input ('Select the object! Please type the number of the source cell:')
            destination_cell = input ('Select the number of the new cell that you want to move the object to:')
            if screen[int(source_cell)][0] != 'B':
                print ('The object you have selected is not yours!!!' )
            else:
                valid_move = check_move (screen[int(source_cell)], destination_cell)
                if valid_move == True:
                    make_move_existing_obj(source_cell, destination_cell)
                                      
        if valid_move == False:            
            print ('Invalid move! Please select a new move!')
            print('-------------------')
        move_made = False

def orangePlayerMove():
# Let the player type in their move.
    print('-------------------')
    print ('Player ', active_player, 'is now playing!')
    valid_move = False
    move_made = False
    
    while valid_move == False:
        if (orange_small > 0 or orange_medium > 0 or orange_large > 0):
            new_obj_answer = input ('Do you wish to move a new object in the screen? (Y/N)')
            if new_obj_answer in ['Y' , 'y']:
                move_made = True
                print ('Please select what kind of object you wish to move into the screen. You have ', orange_small, 'Orange Small objects, ', orange_medium,
                       'Orange Medium objects and ', orange_large, ' Orange Large objects. Please type OS (Orange SMALL) or OM (Orange Medium) or OL (Orange Large):  ' )
                selected_obj = input ()
                if selected_obj in ['OS' , 'OM' , 'OL']:
                    if check_obj_quantity (selected_obj) == False:
                        print ('You do not have any ' , selected_obj , ' available out of the screen!' )
                    else:
                        print ('Enter the number of the cell that you want to move your', selected_obj, 'object to:')
                        selected_cell = input ()
                        if selected_cell in ['1' , '2' , '3' , '4' , '5' , '6', '7' , '8' , '9']:
                            valid_move = check_move (selected_obj, selected_cell)
                            if valid_move == True:
                                make_move_new_obj(selected_obj, selected_cell)
        if (move_made == False) and (obj_exists_in_screen('O')):
            print ('Please move an object in the screen to a new cell' )
            source_cell = input ('Select the object! Please type the number of the source cell:')
            destination_cell = input ('Select the number of the new cell that you want to move the object to:')
            if screen[int(source_cell)][0] != 'O':
                print ('The object you have selected is not yours!!!' )
            else:
                valid_move = check_move (screen[int(source_cell)], destination_cell)
                if valid_move == True:
                    make_move_existing_obj(source_cell, destination_cell)
                                      
        if valid_move == False:            
            print ('Invalid move! Please select a new move!')
            print('-------------------')
        move_made = False


def check_obj_quantity (selected_obj):
    if (selected_obj == 'BS') and (blue_small > 0):
        return True
    elif (selected_obj == 'BM') and (blue_medium > 0):
        return True
    elif (selected_obj == 'BL') and (blue_large > 0):
        return True
    elif (selected_obj == 'OS') and (orange_small > 0):
        return True
    elif (selected_obj == 'OM') and (orange_medium > 0):
        return True
    elif (selected_obj == 'OL') and (orange_large > 0):
        return True
    else:
        return False

def check_move (selected_obj, selected_cell):
    if selected_obj [1] == 'S':
        obj_weight = 1
    elif selected_obj [1] == 'M':
        obj_weight = 2
    elif selected_obj [1] == 'L':
        obj_weight = 3
    if obj_weight > weights[int(selected_cell)]:
        weights[int(selected_cell)] = obj_weight
        return True
    else:
        return False

def make_move_new_obj(selected_obj, selected_cell):
    global blue_small, blue_medium, blue_large, orange_small, orange_medium, orange_large
    screen[int(selected_cell)] = selected_obj
    hidden_screen[int(selected_cell)].append(selected_obj)
    if selected_obj == 'BS':
        blue_small = blue_small - 1
    elif selected_obj == 'BM':
        blue_medium = blue_medium - 1
    elif selected_obj == 'BL':
        blue_large = blue_large - 1
    elif selected_obj == 'OS':
        orange_small = orange_small - 1
    elif selected_obj == 'OM':
        orange_medium = orange_medium - 1
    elif selected_obj == 'OL':
        orange_large = orange_large - 1

def make_move_existing_obj(source_cell, destination_cell):
    screen[int(destination_cell)] = screen[int(source_cell)]
    hidden_screen[int(destination_cell)].append(screen[int(source_cell)])
    hidden_screen[int(source_cell)].pop()
    if (len(hidden_screen[int(source_cell)])) == 0:
        screen[int(source_cell)] = '  '
        weights[int(source_cell)] = 0
    else:
        screen[int(source_cell)] = hidden_screen[int(source_cell)][len(hidden_screen[int(source_cell)]) - 1]
        if screen[int(source_cell)][1] == 'S':
            weights[int(source_cell)] = 1
        elif screen[int(source_cell)][1] == 'M':
            weights[int(source_cell)] = 2
        elif screen[int(source_cell)][1] == 'L':
            weights[int(source_cell)] = 3

def obj_exists_in_screen(color):
    for i in range(1, 10):
        if screen[i][0] == color:
            return True
    return False

def checkforWinner(color):
    if ((screen[7][0] == color and screen[8][0] == color and screen[9][0] == color) or # across the top
        (screen[4][0] == color and screen[5][0] == color and screen[6][0] == color) or # across the middle
        (screen[1][0] == color and screen[2][0] == color and screen[3][0] == color) or # across the bottom
        (screen[7][0] == color and screen[4][0] == color and screen[1][0] == color) or # down the left side
        (screen[8][0] == color and screen[5][0] == color and screen[2][0] == color) or # down the middle
        (screen[9][0] == color and screen[6][0] == color and screen[3][0] == color) or # down the right side
        (screen[7][0] == color and screen[5][0] == color and screen[3][0] == color) or # diagonal
        (screen[9][0] == color and screen[5][0] == color and screen[1][0] == color)): # diagonal
        return True
    else:
        return False
        
print('Welcome to Gobblet Gobblers!')
while active_game:
    printscreen()
    if (active_player == 'Blue'):
        bluePlayerMove()
    else:
        orangePlayerMove()
    if checkforWinner('B'):
        print ('Congratulations BLUE player!!! You have won the game!!!')
        active_game = False
    if checkforWinner('O'):
        print ('Congratulations ORANGE player!!! You have won the game!!!')
        active_game = False
    if (active_player == 'Blue'):
        active_player = 'Orange'
    else:
        active_player = 'Blue'
printscreen()

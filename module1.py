
def display_broad():
    board=[' ']*10
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[7]+'|'+board[8]+'|'+board[9])
def player_choice():
    choice=' '
    while choice !='x' and choice!='o':
        choice=input('player1 pick x or o')
    player1=choice
    if player1=='x':
        player2='o'
    else:
        player2='x'
    return (player1,player2)
    print(player2)
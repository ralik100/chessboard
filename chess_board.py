import random


def show_board(board):
    for x in board:
        print(x)
    
     
def place_piece(board,piece):
    while True:

        x=random.randint(0,7)
        y=random.randint(0,7)

        if board[x][y]=='0 ':
            board[x][y]=piece
            break
    return board

def start_game(board,k):
    
    for i in range(k):
        place_piece(board,'Q ')
    place_piece(board,'P ')
    return board

def capture_check(board):
    can_capture=[]
    for i in range(8):
        try:
            position=board[i].index("P ")
            pawn_position_x=i
            pawn_position_y=position
        except ValueError:
            continue
    
    for i in range(8):
        if board[pawn_position_x][i]=='Q ':
            can_capture.append([pawn_position_x,i])

        if board[i][pawn_position_y]=='Q ':
            can_capture.append([i,pawn_position_y])

        if pawn_position_x-i>=0 and pawn_position_y-i>=0 and board[pawn_position_x-i][pawn_position_y-i]=='Q ':
            can_capture.append([pawn_position_x-i,pawn_position_y-i])

        if pawn_position_x+i<=7 and pawn_position_y-i>=0 and board[pawn_position_x+i][pawn_position_y-i]=='Q ':
            can_capture.append([pawn_position_x+i,pawn_position_y-i])

        if pawn_position_x-i>=0 and pawn_position_y+i<=7 and board[pawn_position_x-i][pawn_position_y+i]=='Q ':
            can_capture.append([pawn_position_x-i,pawn_position_y+i])

        if pawn_position_x+i<=7 and pawn_position_y+i<=7 and board[pawn_position_x-i][pawn_position_y-i]=='Q ':
            can_capture.append([pawn_position_x+i,pawn_position_y+i])
    
    return can_capture

def capture_menu(board):
    print("Wybierz nastepny krok")
    print("1 - wylosuj nowa pozycje dla pionka")
    print("2 - usun dowolnego hetmana (potrzebne [x,y])")
    print("3 - weryfikacja bicia")
    print("4 - wyjscie z menu")
    swicz=input()
    match swicz:
        case '1':
            new_pawn_position(board)
            show_board(board)
            return capture_menu(board)
        case '2':
            print("podaj x")
            x=input()
            print("podaj y")
            y=input()
            queen_removal(board,int(x),int(y))
            show_board(board)
            return capture_menu(board)
        case '3':
            print(capture_check(board))
            return capture_menu(board)
        case '4':
            exit(0)
        case _: 
            print("niepoprawna wartosc")
            return capture_menu(board)

def new_pawn_position(board):

    for i in range(8):
        try:
            position=board[i].index("P ")

            pawn_position_x=i
            pawn_position_y=position

        except ValueError:
            continue

    board[pawn_position_x][pawn_position_y]='0 '

    place_piece(board,"P ")

    return board

def queen_removal(board,pos_x,pos_y):

    if board[pos_x][pos_y]=="Q ":
        board[pos_x][pos_y]="0 "
    else:
        print("Podano bledna lokalizacje")
        
    return board

board=[['0 ' for i in range(8)] for j in range(8)]
k=10

start_game(board,k)
show_board(board)
capture_menu(board)


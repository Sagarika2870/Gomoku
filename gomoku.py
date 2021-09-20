
def is_empty(board):
    counter = 0
    for i in range(len(board)):

        for j in range(len(board[0])):
            if board[i][j] == " ":
                counter += 1

    if counter == (len(board)* len(board[0])):

        return True



def is_bounded(board, y_end, x_end, length, d_y, d_x):
    if d_y == 0 and d_x == 1:
        x_start = x_end - (length -1)
        bound = x_start - 1
        bound_end = x_end +1
        free = get_free_spaces(board)
        if [y_end,bound] in free and [y_end,bound_end] in free:
            return "OPEN"
        elif [y_end,bound] in free or [y_end,bound_end] in free:
            return "SEMIOPEN"
        else:
            return "CLOSED"



    if d_y == 1 and d_x == 0:
        y_start = y_end - (length -1)
        bound = y_start - 1
        bound_end = y_end + 1
        free = get_free_spaces(board)

        if [bound, x_end] in free and [bound_end,x_end] in free:
            return "OPEN"
        elif [bound, x_end] in free or [bound_end,x_end] in free:
            return "SEMIOPEN"
        else:
            return "CLOSED"





    if d_y == 1 and d_x == 1:
        y_start = y_end - (length-1)
        x_start  = x_end - (length-1)
        boundy = y_start - 1
        boundx = x_start -1
        bound_endy = y_end +1
        bound_endx = x_end +1
        free = get_free_spaces(board)

        if [boundy, boundx] in free and [bound_endy,bound_endx] in free:
            return "OPEN"
        elif [boundy, boundx] in free or [bound_endy, bound_endx] in free:
            return "SEMIOPEN"
        else:
            return "CLOSED"



    if d_y == 1 and d_x == -1:
        y_start = y_end - (length-1)
        x_start  = x_end + (length-1)
        boundy = y_start - 1
        boundx = x_start + 1
        bound_endy = y_end +1
        bound_endx = x_end - 1
        free = get_free_spaces(board)

        if [boundy, boundx] in free and [bound_endy,bound_endx] in free:
            return "OPEN"
        elif [boundy, boundx] in free or [bound_endy, bound_endx] in free:
            return "SEMIOPEN"
        else:
            return "CLOSED"







def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    semi_open_seq_count=0
    open_seq_count=0
    if (d_y == 0 and d_x == 1) or (d_y == 1 and d_x == 0):
        for i in range(len(board)):
            if board[y_start +(i*d_y)][x_start + (i*d_x)] == col:
                y_end = (y_start +(i*d_y)) + (length-1)*d_y
                x_end =( x_start + (i*d_x)) + (length-1)*d_x
                if is_bounded(board,y_end,x_end,length,d_y,d_x) == "OPEN":
                    open_seq_count =1
                elif is_bounded(board,y_end,x_end,length,d_y,d_x) == "SEMIOPEN":
                    semi_open_seq_count = 1
                else:
                    semi_open_seq_count = 0
                    open_seq_count = 0



                return open_seq_count, semi_open_seq_count
    elif d_y == 1 and d_x == 1:
        for i in range(len(board)):
            if board[y_start +(i*d_y)][x_start] == col:
                x_end = x_start + ((length*d_x)-1)
                y_end =(y_start +(i*d_y)) + (length -1)
                if is_bounded(board,y_end,x_end,length,d_y,d_x) == "OPEN":
                    open_seq_count =1
                elif is_bounded(board,y_end,x_end,length,d_y,d_x) == "SEMIOPEN":
                    semi_open_seq_count = 1
                else:
                    semi_open_seq_count = 0
                    open_seq_count = 0


                return open_seq_count, semi_open_seq_count

    else:
        for i in range(len(board)):
            if board[y_start +(i*d_y)][x_start] == col:
                x_end = x_start - ((length)-1)
                y_end =(y_start +(i*d_y)) + (length -1)
                if is_bounded(board,y_end,x_end,length,d_y,d_x) == "OPEN":
                    open_seq_count =1
                elif is_bounded(board,y_end,x_end,length,d_y,d_x) == "SEMIOPEN":
                    semi_open_seq_count = 1
                else:
                    semi_open_seq_count = 0
                    open_seq_count = 0


                return open_seq_count, semi_open_seq_count


def detect_rows(board, col, length):
    counter = 0
    semi_open_seq_count=0
    open_seq_count=0
    y_end = 0
    x_end = 0
    for i in range(len(board)):

        for j in range(len(board)):

            if board[i][j] == col:
                y_start = i
                x_start = j

                for k in range(length):
                    if j + (length-1)<= 7:

                        if board[i][j+k] == col:
                            counter +=1
                            x_end = j+k
                            if counter == length:
                                if ((x_end + 1) <= 7) and (x_end-length) >=0:
                                    if board[i][x_end+1]!= col and board[i][x_end-length]!=col:

                                        count = detect_row(board,col,y_start,x_start,length,0,1)
                                        open_seq_count += count[0]
                                        semi_open_seq_count += count[1]
                                        counter = 0
                                    else:
                                        counter = 0
                                elif (x_end +1) > 7:
                                    if board[i][x_end-length]!=col:
                                        count = detect_row(board,col,y_start,x_start,length,0,1)
                                        open_seq_count += count[0]
                                        semi_open_seq_count += count[1]
                                        counter = 0
                                    else:
                                        counter = 0
                                elif (x_end - length) <0:
                                    if board[i][x_end+1]!= col:
                                        count = detect_row(board,col,y_start,x_start,length,0,1)
                                        open_seq_count += count[0]
                                        semi_open_seq_count += count[1]
                                        counter = 0
                                    else:
                                        counter = 0
                                else:
                                    counter = 0
                            elif k ==(length-1) and counter != length:
                                counter = 0

                        else:
                            counter = 0

                for k in range(length):
                    if i + (length-1) <=7:
                        if board[i+k][j] == col:
                            counter +=1
                            if counter == length:
                                y_end = i+k
                                if (y_end+1)<=7 and (y_end-length)>=0:
                                    if board[y_end+1][j]!= col and board[y_end-length][j]!=col:
                                        count1 = detect_row(board,col,y_start,x_start,length,1,0)
                                        open_seq_count += count1[0]
                                        semi_open_seq_count += count1[1]
                                        counter = 0
                                    else:
                                        counter = 0
                                elif (y_end+1)>7:
                                    if board[y_end-length][j]!=col:

                                        count1 = detect_row(board,col,y_start,x_start,length,1,0)
                                        open_seq_count += count1[0]
                                        semi_open_seq_count += count1[1]
                                        counter = 0
                                    else:
                                        counter = 0
                                elif (y_end-length)<0:
                                    if board[y_end+1][j]!= col:
                                        count1 = detect_row(board,col,y_start,x_start,length,1,0)
                                        open_seq_count += count1[0]
                                        semi_open_seq_count += count1[1]
                                        counter = 0
                                    else:
                                        counter = 0
                                else:
                                    counter = 0
                            elif k ==(length-1) and counter != length:
                                counter = 0


                        else:
                            counter = 0
                for k in range(length):
                    if (i+ (length-1))<= 7 and (j+(length-1))<=7:

                        if board[i+k][j+k] == col:

                            counter +=1
                            if counter == length:
                                y_end = i+k
                                x_end = j+k
                                if ((y_end+1)<= 7 and (x_end+1)<=7) and ((y_end-length)>=0 and (x_end-length>=0)):
                                    if board[y_end+1][x_end+1]!=col and board[y_end-length][x_end-length]!=col:
                                        count2 = detect_row(board,col,y_start,x_start,length,1,1)
                                        open_seq_count += count2[0]
                                        semi_open_seq_count += count2[1]
                                        counter = 0
                                    else:
                                        counter = 0
                                elif ((y_end+1)> 7 or (x_end+1)>7):
                                    if  board[y_end-length][x_end-length]!=col:

                                        count2 = detect_row(board,col,y_start,x_start,length,1,1)
                                        open_seq_count += count2[0]
                                        semi_open_seq_count += count2[1]
                                        counter = 0
                                    else:
                                        counter = 0
                                elif ((y_end-length)<0 or (x_end-length<0)):
                                    if board[y_end+1][x_end+1]!=col:
                                        count2 = detect_row(board,col,y_start,x_start,length,1,1)
                                        open_seq_count += count2[0]
                                        semi_open_seq_count += count2[1]
                                        counter = 0
                                    else:
                                        counter = 0
                                else:
                                    counter = 0
                            elif k ==(length-1) and counter != length:
                                counter = 0

                        else:
                            counter = 0
                for k in range(length):
                    if (i+(length-1))<=7 and (j-(length-1))>=0:
                        if board[i+k][j-k] == col:
                            counter +=1
                            if counter == length:
                                y_end = (i+k)
                                x_end = (j-k)
                                if ((y_end+1)<= 7 and (x_end-1)>=0) and ((y_end-length)>=0 and (x_end+length<=7)):
                                    if board[y_end+1][x_end-1]!=col and board[y_end-length][x_end+length]!=col:
                                        count3 = detect_row(board,col,y_start,x_start,length,1,-1)
                                        open_seq_count += count3[0]
                                        semi_open_seq_count += count3[1]
                                        counter = 0
                                    else:
                                        counter = 0
                                elif ((y_end+1)> 7 or (x_end-1)<0): #changed to or
                                    if  board[y_end-length][x_end+length]!=col:

                                        count3 = detect_row(board,col,y_start,x_start,length,1,-1)
                                        open_seq_count += count3[0]
                                        semi_open_seq_count += count3[1]
                                        counter = 0
                                    else:
                                        counter = 0
                                elif ((y_end-length)<0 or (x_end+length>7)): #changed to or
                                    if board[y_end+1][x_end-1]!=col:
                                        count3 = detect_row(board,col,y_start,x_start,length,1,-1)
                                        open_seq_count += count3[0]
                                        semi_open_seq_count += count3[1]
                                        counter = 0
                                    else:
                                        counter = 0
                                else:
                                    counter = 0
                            elif k ==(length-1) and counter != length:
                                counter = 0

                        else:
                            counter = 0

    return open_seq_count, semi_open_seq_count











    ####CHANGE ME
    open_seq_count, semi_open_seq_count = 0, 0
    return open_seq_count, semi_open_seq_count


def get_free_spaces(board):
    free = []
    for i in range(len(board)):

        for j in range(len(board)):
            coord = []
            if board[i][j] == " ":
                coord.append(i)
                coord.append(j)

                free.append(coord)

    return free

def search_max(board):
    coord = get_free_spaces(board)
    first_max = 0
    final_max = -100000
    move_y = coord[0][0]
    move_x = coord[0][1]

    for i in range(len(coord)-1):
        y,x = coord[i][0],coord[i][1]
        board[y][x] = "b"
        first_max = score(board)

        final_max = max(first_max,final_max)

        #if first_max != final_max:
        board[y][x] = " "
        #first_max = 0 #added this
        if first_max == final_max:
            move_y = y
            move_x = x
            first_max = 0 #added this line


            #return move_y, move_x
    return move_y,move_x
def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)


    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4])+
            500  * open_b[4]                     +
            50   * semi_open_b[4]                +
            -100  * open_w[3]                    +
            -30   * semi_open_w[3]               +
            50   * open_b[3]                     +
            10   * semi_open_b[3]                +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])


def is_win(board):
    if score(board) == 100000:
        return "Black won"
    elif score(board) == -100000:
        return "White won"
    elif len(get_free_spaces(board)) == 0:
        return "Draw"
    else:
        return "Continue playing"

    #pass


def print_board(board):

    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board



def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        print(" ")
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))

            print("Semi-open rows of length %d: %d" % (i, semi_open))






def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res





        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res



def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 7; y =5 ; d_x = -1; d_y =1 ; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 7
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'CLOSED':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = -1; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (0,1):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 1; y = 5; d_x = 1; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (0,1):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 0; y = 5; d_x = 1; d_y = 0; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (5,4):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)

    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0

    y = 3; x = 5; d_x = -1; d_y = 1; length = 2

    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #

    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);

    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #
    #
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0




if __name__ == '__main__':
    print(play_gomoku(8))


    #print(is_empty(board))
    #print(test_is_bounded())
    #print(test_detect_row())
    #print(detect_row(board,col,))
    #print(test_detect_rows())

    #print(test_search_max())
    #print(search_max(board))
    #print(easy_testset_for_main_functions())
    #print(some_tests())
    board = make_empty_board(8)
    #
    # put_seq_on_board(board, 0, 0, 0, 1, 1, "w")
    # put_seq_on_board(board, 1, 1, 0, 1, 2, "w")
    # put_seq_on_board(board, 3, 6, 0, 1, 1, "w")
    # put_seq_on_board(board, 0, 3, 0, 1, 3, "w")
    # put_seq_on_board(board, 6, 6, 0, 1, 1, "w")
    # put_seq_on_board(board, 2, 3, 1, 1, 3, "w")
    # put_seq_on_board(board, 7, 4, 0, 1, 4, "w")
    # put_seq_on_board(board, 2, 5, 0, 1, 2, "w")
    # put_seq_on_board(board, 5, 2, 1, 1, 2, "w")
    # put_seq_on_board(board, 7, 0, 0, 1, 1, "b")
    # put_seq_on_board(board, 0, 6, 0, 1, 1, "b")
    # put_seq_on_board(board, 7, 2, 0, 1, 2, "b")
    # put_seq_on_board(board, 2, 2, 1, 1, 4, "b")
    # put_seq_on_board(board, 3, 2, 1, 1, 3, "b")
    # put_seq_on_board(board, 3, 1, 1, 1, 3, "b")
    # put_seq_on_board(board, 0, 7, 1, 0, 3, "b")
    # put_seq_on_board(board, 6, 0, 0, 1, 2, "b")
    # put_seq_on_board(board, 2, 0, 1, 0, 3, "b")
    # put_seq_on_board(board, 3, 5, 1, 1, 3, "b")
    # put_seq_on_board(board, 1, 4, 0, 1, 2, "b")
    # print_board(board)
    # analysis(board)

""" Tic Tac Toe Game by D4V1DH4YT3R """
import sys


def map_ticking(lines, *args):
    """This function is main map"""

    # If the user sent the location and sign information, the move is made.
    if len(args) == 2:
        tic = args[0]
        if len(tic) == 1:
            tic = args[0] + " "
        else:
            tic = tic[0] + " "

        location = int(args[1])

        # For example, if the user chooses 5th position,
        # the index value is taken from this list.
        #  this index value is "11"
        indexex = [
            "00", "01", "02",
            "10", "11", "12",
            "20", "21", "22",
        ]
        # The location specified by the user is marked.
        for i in range(1, 10):
            if location == i:
                # We took the locations between 1 and 9,
                # but since the indexes were in the range of 0-8, we used the value of i - 1.
                field_indexes = indexex[i-1]
                start_ind, end_ind = int(field_indexes[0]), int(field_indexes[1])

                if lines[start_ind][end_ind] == "_ ":
                    lines[start_ind][end_ind] = tic
                    break
                print("Please Try Again! This field is full!")
                # Tic is still the same because the user is the same.
                new_tic = tic
                # A new one is requested because the old location is full.
                new_location = int(input("Please select new location: "))
                map_ticking(lines, new_tic, new_location)
    # If the user has sent one of the location or sign information missing,
    # an error message will be displayed.
    else:
        print("Error!!!")


def show_map(lines):
    """This function display the map"""

    # exists to show the current status of the map.
    game_map = lines
    for line in game_map:
        row = ""
        for item in line:
            row += item + " "
        print(row)


def is_winner(game_board):
    """This function for control"""
    #  The cont_stat variable exists to check whether
    #  rows, columns and diagonals are completed.
    cont_stat = ('X X X ', 'O O O ')
    # Game map is taken.
    game_map = game_board
    # With the for loop here, row checks are performed.
    for line in game_map:
        row = ""
        for item in line:
            row.join(item)
        if row in cont_stat:
            show_map(game_map)
            return True

    # The next checks are made for the columns.
    column1 = ""
    column2 = ""
    column3 = ""

    for i, _ in enumerate(game_map):
        column1 += game_map[i][0]
        column2 += game_map[i][1]
        column3 += game_map[i][2]

    if column1 in cont_stat or column2 in cont_stat or column3 in cont_stat:
        show_map(game_map)
        return True

    # Cross cells are being checked.
    cross_line1 = game_map[0][0] + game_map[1][1] + game_map[2][2]
    cross_line2 = game_map[0][2] + game_map[1][1] + game_map[2][0]

    if cross_line1 in cont_stat or cross_line2 in cont_stat:
        show_map(game_map)
        return True

    # If there is no winning condition, False value is returned!
    return False


def map_control(game_board):
    """This function for map fulled control"""
    game_map = game_board

    # Check whether there is free space or not.
    control_counter = 0
    for i, _ in enumerate(game_map):
        for j, _ in enumerate(game_map):
            if game_map[i][j] == "_ ":
                control_counter += 1

    if control_counter == 0:
        # If there is no more space on the map,
        # True is returned to indicate that the game is over.
        return True

    return False


def player_move(player_no, player_name, game_board):
    """This function for player1 moves"""
    game_map = game_board
    player = player_name
    player_name = player_no

    # The map is checked before player 1 plays.
    map_isfulled = map_control(game_map)
    if map_isfulled:
        print("GAME OVER!")
        try_again = input("Do you want try again?: y/N: ")
        if try_again in ('y', 'Y'):
            main()
        else:
            print("Exiting!!!")
            sys.exit()

    # The map is shown before Player 1 moves.
    show_map(game_map)

    print()
    # Which Player's move sequence shows it.
    print(player_name)
    # U'll get information about which position player 1 will put the sign.
    # Check that location information is a number and is between 1-9.
    player_selection = 0
    while player_selection == 0:
        player_selection = input("Which location would you like to tick? [1-9]: ")
        if player_selection.isnumeric():
            player_selection = int(player_selection)
            if 1 <= player_selection <= 9:
                break
            print("Please enter a number between 1 and 9!")
            player_selection = 0
        else:
            print("Please enter a number between 1 and 9!")
            player_selection = 0
    # Player1's move is accomplished with the player_move function.
    map_ticking(game_map, player, player_selection)
    # After Player 1 moves, the status of the game map is checked.
    control = is_winner(game_map)
    # If the value returned from the is_winner() func is True, the player is declared winning.
    # The value of the control variable can be either True or False.
    # If the value returned from the is_winner function is False, the game continues.
    if control:
        # This block works when the value of the control variable is True.
        # The player who won the game is shown. By specifying X or O.
        print("{0} ({1}) is win".format(player_name, player))
        try_again = input("Do you want try again?: y/N: ")
        if try_again in ('y', 'Y'):
            print()
            print("--- New Game ---")
            main()
        else:
            print("Exiting!!!")
            # False value returns when the game is closed.
            return False

    # True value will return as the game continues.
    return True


def player_assigments():
    """This function for player assignment"""
    # Player 1's choice
    player1 = input("Do you want X or O: ")
    if player1 not in ('x', 'X', 'o', 'O'):
        # If the user enters a value other than X or O values,
        # we will ask him to make a selection again.
        print("Please enter your choice again. x/O: ")
        main()
    # X and O assignments are made according to Player1's choice.
    if player1 in ('x', 'X'):
        player1 = 'X'
        player2 = 'O'
        print("""
                Player 1 -> X
                Player 2 -> O
            """)
        return player1, player2
    player1 = 'O'
    player2 = 'X'
    print("""
            Player 1 -> O
            Player 2 -> X
        """)
    return player1, player2


def main():
    """This is main function, it's director."""
    # The game map must be defined in the main function or in the global scope.
    game_map = [
        ["_ ", "_ ", "_ "],
        ["_ ", "_ ", "_ "],
        ["_ ", "_ ", "_ "]
    ]

    player1, player2 = player_assigments()
    while 1:
        # Player 1 moves
        p1_control = player_move("Player 1", player1, game_map)
        if not p1_control:
            break

        # Player 2 moves
        p2_control = player_move("Player 2", player2, game_map)
        if not p2_control:
            break


main()

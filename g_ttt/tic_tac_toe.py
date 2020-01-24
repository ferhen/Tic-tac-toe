WINNING_CONDITIONS = [
	[7, 8, 9], [4, 5, 6], [1, 2, 3], # lines
	[7, 4, 1], [8, 5, 2], [9, 6, 3], # columns
	[7, 5, 3], [9, 5, 1] 			 # diagonals
]

# Prints the board
def print_board(moves):
    print(
        f" {moves[7]} | {moves[8]} | {moves[9]}"
        "\n-----------\n"
        f" {moves[4]} | {moves[5]} | {moves[6]}"
        "\n-----------\n"
        f" {moves[1]} | {moves[2]} | {moves[3]}"
    )


# Checks winning condition
def check_win(moves, letter):
    return any(all(moves[i] == letter for i in x) for x in WINNING_CONDITIONS)


def ask_to_play_again():
	answer = input("\n\nDo you want to play again (Y/N)? ")
	if answer.lower() == "n":
		print("\nThank you for playing!")
		return False
	elif answer.lower() == "y":
		print("\n")
		return True
	else:
		print("Please, input a valid answer")


def print_instructions():
    print("\nInstructions of how to play the game:\n\n")
    print(
        "When choosing a place to make a move, "
        "use the correspondent number keys as stated here: \n"
    )
    print(f" 7 | 8 | 9 \n-----------\n 4 | 5 | 6 \n-----------\n 1 | 2 | 3 ")
    print("\n")


# Prints the score
def print_game_score(score):
    print(f"X score: {score[0]}")
    print(f"O score: {score[1]}")
    print("\n")


# Starting the game
def start_game():
    score = [0, 0]
    while True:

        # Introduction
        print("\n\n\nHey, welcome to Tic Tac Toe!")
        print_instructions()
        print_game_score(score)
        # Choosing the letter of the first player
        XO = ["X", "O"]
        first_letter = input(
            "Does the first player " "want to be the O or the X? "
        )
        while True:
            if first_letter == "X" or first_letter == "x":
                break
            elif first_letter == "O" or first_letter == "o":
                XO = XO[::-1]
                break
            else:
                first_letter = input('Please, choose between "X" or "O": ')

        # Setting starting conditions
        moves = [" "] * 10
        print("\n" * 3)
        print_board(moves)

        # Starts the game
        for i in range(1, 10):
            print(f"\nTURN: {XO[i%2 - 1]}")

            # Checking for legal move
            while True:
                u = input("Where do you to make your move? ")

                if u not in "123456789":
                    print("\nPlease make a legal move")
                elif moves[int(u)] == "X" or moves[int(u)] == "O":
                    print("\nPlease make a legal move")
                else:
                    u = int(u)
                    break

            print("\n" * 3)
            moves[u] = XO[i % 2 - 1]
            print_board(moves)

            # Checking winning conditions
            if check_win(moves, XO[i % 2 - 1]):
                print(
                    f"\nTHE GAME IS OVER!\n{XO[i%2 - 1]} "
                    "IS THE WINNER! CONGRATULATIONS!"
                )

                if XO[i % 2 - 1] == "X":
                    score[0] += 1
                else:
                    score[1] += 1

                print_game_score(score)
                break

            if check_win(moves, XO[i % 2]):
                print(
                    f"\nTHE GAME IS OVER!\n{XO[i%2]} "
                    "IS THE WINNER! CONGRATULATIONS!"
                )

                if XO[i % 2] == "X":
                    score[0] += 1
                else:
                    score[1] += 1

                print_game_score(score)
                break

            if i == 9:
                print("\nTHE GAME IS OVER! IT'S A DRAW!")
                print_game_score(score)
                break

        if ask_to_play_again() == False:
            print("\nFINAL SCORES")
            print_game_score(score)
            break


if __name__ == "__main__":
    start_game()


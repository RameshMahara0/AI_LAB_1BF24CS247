import math
import time

board = [" "] * 9


# ---------------- DISPLAY BOARD ----------------
def display_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


# ---------------- CHECK WINNER ----------------
def winner(player):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == player and board[b] == player and board[c] == player:
            return True

    return False


# ---------------- CHECK DRAW ----------------
def is_full():
    return " " not in board


# ---------------- MINIMAX ----------------
def minimax(is_maximizing, bot, player):

    # Bot wins
    if winner(bot):
        return 1

    # Player/opponent wins
    if winner(player):
        return -1

    # Draw
    if is_full():
        return 0

    if is_maximizing:

        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":

                board[i] = bot

                score = minimax(False, bot, player)

                board[i] = " "

                best_score = max(best_score, score)

        return best_score

    else:

        best_score = math.inf

        for i in range(9):
            if board[i] == " ":

                board[i] = player

                score = minimax(True, bot, player)

                board[i] = " "

                best_score = min(best_score, score)

        return best_score


# ---------------- BOT MOVE ----------------
def bot_move(bot, opponent):

    best_score = -math.inf
    best_move = None

    for i in range(9):

        if board[i] == " ":

            # Try this move
            board[i] = bot

            # Check future possibilities
            score = minimax(False, bot, opponent)

            # Undo move
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = bot


# ---------------- MAN VS BOT ----------------
def man_vs_bot():

    global board
    board = [" "] * 9

    print("\nYou = X")
    print("Bot = O")

    while True:

        display_board()

        # Player move
        position = int(input("Enter position (1-9): ")) - 1

        if position < 0 or position > 8 or board[position] != " ":
            print("Invalid move!")
            continue

        board[position] = "X"

        if winner("X"):
            display_board()
            print("You Win!")
            break

        if is_full():
            display_board()
            print("Draw!")
            break

        # Bot move
        print("Bot is thinking...")
        bot_move("O", "X")

        if winner("O"):
            display_board()
            print("Bot Wins!")
            break

        if is_full():
            display_board()
            print("Draw!")
            break


# ---------------- BOT VS BOT ----------------
def bot_vs_bot():

    global board
    board = [" "] * 9

    print("\nBot X vs Bot O")
    print("Watch the AI play!\n")

    current_bot = "X"

    while True:

        display_board()

        print("Bot", current_bot, "is thinking...")

        if current_bot == "X":
            bot_move("X", "O")
        else:
            bot_move("O", "X")

        time.sleep(1)

        if winner(current_bot):
            display_board()
            print("Bot", current_bot, "Wins!")
            break

        if is_full():
            display_board()
            print("Draw!")
            break

        # Change bot
        if current_bot == "X":
            current_bot = "O"
        else:
            current_bot = "X"


# ---------------- MAIN PROGRAM ----------------
print("================================")
print("       TIC-TAC-TOE GAME")
print("================================")

print("1. Man vs Bot")
print("2. Bot vs Bot")

choice = int(input("Choose mode (1 or 2): "))

if choice == 1:
    man_vs_bot()

elif choice == 2:
    bot_vs_bot()

else:
    print("Invalid choice!")

import random

# Function to display the Tic-Tac-Toe board
def display_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")
    print("\n")

# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check row
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check column
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:  # Diagonal
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:  # Diagonal
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Function to handle player's turn
def player_turn(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, choose your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("That spot is taken, try again!")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")

# Function to make the AI's move (simple random move)
def ai_turn(board, ai_player):
    print(f"\nAI ({ai_player}) is making its move...")
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']
    row, col = random.choice(empty_cells)
    board[row][col] = ai_player
    print(f"AI chose position {row * 3 + col + 1}.\n")

# Function to play the Tic-Tac-Toe game
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    mode = input("Choose game mode: 1 for Player vs Player, 2 for Player vs AI: ")
    
    # Initialize board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    
    # Assign players
    if mode == "1":
        players = ['X', 'O']  # Player 1 is X, Player 2 is O
    elif mode == "2":
        players = ['X', 'O']  # Player is X, AI is O
    else:
        print("Invalid mode selected. Exiting.")
        return
    
    current_player = 0  # Start with Player 1 or Player (X)
    
    while True:
        display_board(board)
        
        if mode == "1" or (mode == "2" and current_player == 0):  # Human player's turn
            player_turn(board, players[current_player])
        else:  # AI's turn
            ai_turn(board, players[1])
        
        # Check for win or draw
        if check_win(board, players[current_player]):
            display_board(board)
            print(f"Player {players[current_player]} wins!")
            break
        
        if is_board_full(board):
            display_board(board)
            print("It's a tie!")
            break
        
        # Switch player
        current_player = 1 - current_player  # Switch between 0 and 1

# Run the game
if __name__ == "__main__":
    play_game()

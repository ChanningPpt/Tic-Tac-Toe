import random
from player import HumanPlayer, ComputerPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        # Initialize a 3x3 board (empty cells)
        self.board = [' ' for _ in range(9)]
        self.human_marker = 'X'
        self.computer_marker = 'O'
        self.scores = {"Human": 0, "AI": 0, "Ties": 0}

    def print_board(self):
        # Print the current state of the board
        print('-------------')
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
        print('-------------')

    def print_board_nums(self):
        # Print board with numbers for reference
        num_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        print('-------------')
        for row in num_board:
            print('| ' + ' | '.join(row) + ' |')
        print('-------------')

    def make_move(self, player, position):
        # Place the player's marker on the board at the given position
        if 0 <= position < 9 and self.board[position] == ' ':  # Check if the position is valid and empty
            self.board[position] = player
            return True
        return False  # Invalid move

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for row in range(3):
            if self.board[row*3] == self.board[row*3+1] == self.board[row*3+2] != ' ':
                return self.board[row*3]

        for col in range(3):
            if self.board[col] == self.board[col+3] == self.board[col+6] != ' ':
                return self.board[col]

        if self.board[0] == self.board[4] == self.board[8] != ' ':
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != ' ':
            return self.board[2]

        return None  # No winner yet

    def is_board_full(self):
        # Return True if all cells are filled
        return ' ' not in self.board

    def reset_board(self):
        # Clear the board for a new game
        self.board = [' ' for _ in range(9)]

    def play_game(self, human_player, computer_player):
        # Show reference board with numbers before starting the game
        print("\nBoard positions reference:")
        self.print_board_nums()

        current_player = human_player  # Start with human player
        while True:
            self.print_board()
            if current_player == human_player:
                while True:
                    try:
                        position = int(input(f"Enter your move (0-8) for {self.human_marker}: "))  # Human move
                        if self.make_move(self.human_marker, position):
                            break
                        else:
                            print("Invalid move. Position already taken or out of range. Try again.")
                    except ValueError:
                        print("Invalid input. Please enter a number between 0 and 8.")
                if self.check_winner() == self.human_marker:
                    self.print_board()
                    print("🎉 Human wins! 🎉")
                    self.scores["Human"] += 1
                    break
                current_player = computer_player  # Switch to AI
            else:
                print("AI is making a move...")
                position = computer_player.make_move(self.board)  # AI move
                self.make_move(self.computer_marker, position)  # AI marker
                if self.check_winner() == self.computer_marker:
                    self.print_board()
                    print("🤖 AI wins! 🤖")
                    self.scores["AI"] += 1
                    break
                current_player = human_player  # Switch back to human

            if self.is_board_full():
                self.print_board()
                print("🤝 It's a tie! 🤝")
                self.scores["Ties"] += 1
                break

    def show_scores(self):
        # Print the current score of the games
        print("\n🏆 Scores:")
        print(f"Human: {self.scores['Human']}")
        print(f"AI: {self.scores['AI']}")
        print(f"Ties: {self.scores['Ties']}\n")


# Initialize players and start the game
if __name__ == '__main__':
    print("Welcome to Tic-Tac-Toe!")
    human = HumanPlayer()

    # Player customization
    while True:
        human_marker = input("Choose your marker (X/O): ").strip().upper()
        if human_marker not in ['X', 'O']:
            print("Invalid selection. Please enter 'X' or 'O'.")
        else:
            break

    game = TicTacToe()
    game.human_marker = human_marker
    game.computer_marker = 'O' if human_marker == 'X' else 'X'

    # Choose AI mode
    while True:
        mode = input("\nChoose AI mode (1: Random, 2: Minimax): ")
        if mode not in ['1', '2']:
            print("Invalid selection. Please enter 1 for Random AI or 2 for Minimax AI.")
        else:
            break

    if mode == '1':
        computer = RandomComputerPlayer()
        print("\nYou have chosen to play against the Random AI.")
    else:
        computer = ComputerPlayer()
        print("\nYou have chosen to play against the Minimax AI.")

    while True:
        game.reset_board()
        game.play_game(human, computer)
        game.show_scores()
        while True:
            play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
            if play_again not in ['y', 'n']:
                print("Invalid input. Please enter 'y' to play again or 'n' to exit.")
            else:
                break
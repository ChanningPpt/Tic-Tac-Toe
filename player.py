import random

class Player:
    def make_move(self, board):
        pass  # Placeholder for player move logic


class HumanPlayer(Player):
    def make_move(self, board):
        pass  # Human move input handled in TicTacToe class


class ComputerPlayer(Player):
    def make_move(self, board):
        best_score = -float('inf')
        best_move = None
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'  # Try AI move
                score = self.minimax(board, 0, False)
                board[i] = ' '  # Undo move
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_move

    def minimax(self, board, depth, is_maximizing):
        result = self.evaluate_board(board)  # Check if game is over
        if result is not None:
            return result

        if is_maximizing:  # AI's turn
            best_score = -float('inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'O'
                    score = self.minimax(board, depth + 1, False)
                    board[i] = ' '  # Undo move
                    best_score = max(score, best_score)
            return best_score
        else:  # Human's turn
            best_score = float('inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'X'
                    score = self.minimax(board, depth + 1, True)
                    board[i] = ' '  # Undo move
                    best_score = min(score, best_score)
            return best_score

    def evaluate_board(self, board):
        # Evaluate board state
        winner = self.check_winner(board)
        if winner == 'O':
            return 10  # AI win
        elif winner == 'X':
            return -10  # Human win
        elif ' ' not in board:
            return 0  # Draw
        return None  # Game not over

    def check_winner(self, board):
        # Check rows, columns, and diagonals for a winner
        for row in range(3):
            if board[row*3] == board[row*3+1] == board[row*3+2] != ' ':
                return board[row*3]

        for col in range(3):
            if board[col] == board[col+3] == board[col+6] != ' ':
                return board[col]

        if board[0] == board[4] == board[8] != ' ':
            return board[0]
        if board[2] == board[4] == board[6] != ' ':
            return board[2]

        return None  # No winner yet


class RandomComputerPlayer(Player):
    def make_move(self, board):
        # Make a random valid move
        empty_positions = [i for i, cell in enumerate(board) if cell == ' ']
        if empty_positions:
            return random.choice(empty_positions)
        return None  # No moves left
# game/views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse

def game_view(request):
    return render(request, 'game/tictactoe.html',{'range_9': range(9)})

# Function to check if a player has won
def check_winner(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != "":
            return board[condition[0]]
    if "" not in board:
        return "Tie"
    return None

# Minimax AI move calculation
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1  # AI wins
    elif winner == "X":
        return -1  # Player wins
    elif winner == "Tie":
        return 0  # Tie game

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == "":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = ""
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == "":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = ""
                best_score = min(score, best_score)
        return best_score

# Function to get the best AI move using Minimax
def get_ai_move(board):
    best_score = -float("inf")
    move = None
    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = ""
            if score > best_score:
                best_score = score
                move = i
    return move

def play_move(request):
    board = request.GET.get("board").split(",")  # Board from the frontend
    board = [cell if cell != "-" else "" for cell in board]  # Convert "-" to empty strings

    # Check if the player has already won or it's a tie
    winner = check_winner(board)
    if winner:
        return JsonResponse({"status": "finished", "winner": winner})

    # AI move using Minimax
    ai_move = get_ai_move(board)
    if ai_move is not None:
        board[ai_move] = "O"

    # Check for a winner or a tie after AI's move
    winner = check_winner(board)
    if winner:
        return JsonResponse({"status": "finished", "winner": winner, "board": board})

    return JsonResponse({"status": "ongoing", "board": board})


def quit_game(request):
    # Logic to handle quitting the game, like redirecting to the main page
    return redirect('game_view')  # Redirects to the main game view
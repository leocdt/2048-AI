import random
import os

# Initialisation du plateau de jeu
board = [[0 for _ in range(4)] for _ in range(4)]


# Fonction pour ajouter un nouveau nombre (2 ou 4) à une position aléatoire vide sur le plateau
def add_new_number():
    empty_cells = [(i, j) for i in range(4)
                   for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = random.choice([2, 4])


# Fonction pour afficher le plateau de jeu
def print_board():
    for row in board:
        print('\t'.join(map(str, row)))
        print()
        
def print_colored_board():
    for row in board:
        colored_row : list[str] = []
        for num in row:
            if num == 0:
                colored_row.append('\033[0m' + str(num).center(6))
            elif num == 2:
                colored_row.append('\033[94m' + str(num).center(6))  # Blue color for 2
            elif num == 4:
                colored_row.append('\033[92m' + str(num).center(6))  # Green color for 4
            elif num == 8:
                colored_row.append('\033[93m' + str(num).center(6))  # Yellow color for 8
            else:
                colored_row.append('\033[91m' + str(num).center(6))  # Red color for other numbers

        print(''.join(colored_row) + '\033[0m')  # Reset color after each row
        print()

def move_left():
    global board
    for row in board:
        # Move non-zero numbers to the left
        temp_row = [num for num in row if num != 0]
        i = 0
        while i < len(temp_row) - 1:
            if temp_row[i] == temp_row[i + 1]:
                temp_row[i] *= 2
                temp_row[i + 1] = 0
                i += 2
            else:
                i += 1
        # Move numbers to the left after merging
        temp_row = [num for num in temp_row if num != 0]
        while len(temp_row) < 4:
            temp_row.append(0)
        board[board.index(row)] = temp_row

# Update move_right(), move_up(), and move_down() functions in a similar way

def move_right():
    global board
    for row in board:
        # Move non-zero numbers to the right
        temp_row = [num for num in row if num != 0]
        i = len(temp_row) - 1
        while i > 0:
            if temp_row[i] == temp_row[i - 1]:
                temp_row[i] *= 2
                temp_row[i - 1] = 0
                i -= 2
            else:
                i -= 1
        # Move numbers to the right after merging
        temp_row = [num for num in temp_row if num != 0]
        while len(temp_row) < 4:
            temp_row.insert(0, 0)
        board[board.index(row)] = temp_row

def move_up():
    global board
    for j in range(4):
        # Extract column
        column = [board[i][j] for i in range(4)]
        # Move non-zero numbers up
        temp_column = [num for num in column if num != 0]
        i = 0
        while i < len(temp_column) - 1:
            if temp_column[i] == temp_column[i + 1]:
                temp_column[i] *= 2
                temp_column[i + 1] = 0
                i += 2
            else:
                i += 1
        # Move numbers up after merging
        temp_column = [num for num in temp_column if num != 0]
        while len(temp_column) < 4:
            temp_column.append(0)
        # Update the board with the merged numbers
        for i in range(4):
            board[i][j] = temp_column[i]

def move_down():
    global board
    for j in range(4):
        # Extract column
        column = [board[i][j] for i in range(4)]
        # Move non-zero numbers down
        temp_column = [num for num in column if num != 0]
        i = len(temp_column) - 1
        while i > 0:
            if temp_column[i] == temp_column[i - 1]:
                temp_column[i] *= 2
                temp_column[i - 1] = 0
                i -= 2
            else:
                i -= 1
        # Move numbers down after merging
        temp_column = [num for num in temp_column if num != 0]
        while len(temp_column) < 4:
            temp_column.insert(0, 0)
        # Update the board with the merged numbers
        for i in range(4):
            board[i][j] = temp_column[i]

            
def is_game_over():
    # Check if there are any possible moves left
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0 or \
               (j > 0 and board[i][j] == board[i][j - 1]) or \
               (j < 3 and board[i][j] == board[i][j + 1]) or \
               (i > 0 and board[i][j] == board[i - 1][j]) or \
               (i < 3 and board[i][j] == board[i + 1][j]):
                return False
    return True


def play_game():
    add_new_number()
    add_new_number()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_colored_board()
        if is_game_over():
            print("Game Over! Merci d'avoir joué.")
            break
        move = input(
            "Entrez votre mouvement (gauche, droite, haut, bas) ou 'q' pour quitter : ").lower()
        if move == 'q':
            print("Merci d'avoir joué !")
            break
        elif move in ['gauche', 'droite', 'haut', 'bas']:
            if move == 'gauche':
                move_left()
            elif move == 'droite':
                move_right()
            elif move == 'haut':
                move_up()
            elif move == 'bas':
                move_down()
            add_new_number()
        else:
            print("Mouvement non valide. Essayez encore.")


# Lancer le jeu
if __name__ == "__main__":
    play_game()
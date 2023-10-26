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


def move_left():
    global board
    for row in board:
        # Fusionner les nombres identiques
        for i in range(3):
            for j in range(i+1, 4):
                if row[i] == row[j] and row[i] != 0:
                    row[i] *= 2
                    row[j] = 0
                    break
        # Déplacer les nombres vers la gauche
        temp_row = [num for num in row if num != 0]
        while len(temp_row) < 4:
            temp_row.append(0)
        board[board.index(row)] = temp_row

def move_right():
    global board
    for row in board:
        # Fusionner les nombres identiques
        for i in range(3, 0, -1):
            for j in range(i-1, -1, -1):
                if row[i] == row[j] and row[i] != 0:
                    row[i] *= 2
                    row[j] = 0
                    break
        # Déplacer les nombres vers la droite
        temp_row = [num for num in row if num != 0]
        while len(temp_row) < 4:
            temp_row.insert(0, 0)
        board[board.index(row)] = temp_row

def move_up():
    global board
    for j in range(4):
        # Fusionner les nombres identiques de haut en bas
        column = [board[i][j] for i in range(4)]
        for i in range(3):
            for k in range(i+1, 4):
                if column[i] == column[k] and column[i] != 0:
                    column[i] *= 2
                    column[k] = 0
                    break
        # Déplacer les nombres vers le haut
        temp_column = [num for num in column if num != 0]
        while len(temp_column) < 4:
            temp_column.append(0)
        for i in range(4):
            board[i][j] = temp_column[i]

def move_down():
    global board
    for j in range(4):
        # Fusionner les nombres identiques de bas en haut
        column = [board[i][j] for i in range(4)]
        for i in range(3, 0, -1):
            for k in range(i-1, -1, -1):
                if column[i] == column[k] and column[i] != 0:
                    column[i] *= 2
                    column[k] = 0
                    break
        # Déplacer les nombres vers le bas
        temp_column = [num for num in column if num != 0]
        while len(temp_column) < 4:
            temp_column.insert(0, 0)
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
        print_board()
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

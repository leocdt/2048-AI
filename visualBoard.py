import random
import pygame


# Initialize the game
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 4
CELL_SIZE = WIDTH // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TILE_COLORS = {
    0: (204, 192, 179),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}

# Initialize the game board
board = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Fonction pour ajouter un nouveau nombre (2 ou 4) à une position aléatoire vide sur le plateau
def add_new_number():
    empty_cells = [(i, j) for i in range(4)
                   for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = random.choice([2, 4])


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

def game_over_screen(screen : pygame.Surface):
    font = pygame.font.Font(None, 36)  # Reduced font size to 36
    text = font.render("Game Over!", True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))

    restart_text = font.render("Appuyez sur Entrée pour rejouer", True, BLACK)
    restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

    # Draw semi-transparent white rectangle to overlay the game
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    pygame.draw.rect(overlay, (255, 255, 255, 128), (0, 0, WIDTH, HEIGHT))
    screen.blit(overlay, (0, 0))

    screen.blit(text, text_rect)
    screen.blit(restart_text, restart_rect)

    pygame.display.flip()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    initialize_game()
                    waiting_for_input = False


def initialize_game():
    global board
    board = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    add_new_number()
    add_new_number()


def add_new_number():
    empty_cells = [(i, j) for i in range(GRID_SIZE)
                   for j in range(GRID_SIZE) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2 if random.random() < 0.9 else 4

def draw_board(screen : pygame.Surface):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            pygame.draw.rect(screen, TILE_COLORS[board[i][j]],
                             (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            if board[i][j] != 0:
                font = pygame.font.Font(None, 36)
                text = font.render(str(board[i][j]), True, BLACK)
                text_rect = text.get_rect(center=(j * CELL_SIZE + CELL_SIZE / 2, i * CELL_SIZE + CELL_SIZE / 2))
                screen.blit(text, text_rect)

    pygame.display.flip()

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('2048 Game')
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left()
                    add_new_number()
                elif event.key == pygame.K_RIGHT:
                    move_right()
                    add_new_number()
                elif event.key == pygame.K_UP:
                    move_up()
                    add_new_number()
                elif event.key == pygame.K_DOWN:
                    move_down()
                    add_new_number()

        screen.fill(WHITE)
        draw_board(screen)
        pygame.display.update()

        if is_game_over():
            print("Game Over! Merci d'avoir joué.")
            game_over_screen(screen)

    pygame.quit()

if __name__ == "__main__":
    initialize_game()
    main()
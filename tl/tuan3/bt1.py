import pygame
import sys

# Constants
WIDTH, HEIGHT = 540, 600
BACKGROUND_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
CELL_SIZE = WIDTH // 9
FONT = None
FONT_SIZE = 40

# Initialize Pygame
pygame.init()
FONT = pygame.font.SysFont("comicsans", FONT_SIZE)

class Cell:
    def __init__(self, value, row, col):
        self.value = value
        self.temp_value = 0
        self.row = row
        self.col = col
        self.selected = False

    def draw(self, win):
        if self.temp_value != 0 and self.value == 0:
            text = FONT.render(str(self.temp_value), True, (128, 128, 128))
            win.blit(text, (self.col * CELL_SIZE + 5, self.row * CELL_SIZE + 5))
        elif self.value != 0:
            text = FONT.render(str(self.value), True, LINE_COLOR)
            win.blit(text, (self.col * CELL_SIZE + (CELL_SIZE // 2 - text.get_width() // 2), 
                            self.row * CELL_SIZE + (CELL_SIZE // 2 - text.get_height() // 2)))

        if self.selected:
            pygame.draw.rect(win, (255, 0, 0), (self.col * CELL_SIZE, self.row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)

    def set_value(self, value):
        self.value = value

    def set_temp(self, temp_value):
        self.temp_value = temp_value

class Grid:
    def __init__(self, board):
        self.board = board
        self.cells = [[Cell(self.board[row][col], row, col) for col in range(9)] for row in range(9)]
        self.selected = None

    def draw(self, win):
        for row in range(10):
            if row % 3 == 0 and row != 0:
                thickness = 4
            else:
                thickness = 1
            pygame.draw.line(win, LINE_COLOR, (0, row * CELL_SIZE), (WIDTH, row * CELL_SIZE), thickness)
            pygame.draw.line(win, LINE_COLOR, (row * CELL_SIZE, 0), (row * CELL_SIZE, WIDTH), thickness)

        for row in range(9):
            for col in range(9):
                self.cells[row][col].draw(win)

    def select(self, row, col):
        for r in range(9):
            for c in range(9):
                self.cells[r][c].selected = False
        self.cells[row][col].selected = True
        self.selected = (row, col)

    def click(self, pos):
        if pos[0] < WIDTH and pos[1] < WIDTH:
            x = pos[0] // CELL_SIZE
            y = pos[1] // CELL_SIZE
            return (y, x)
        return None

    def clear(self):
        row, col = self.selected
        if self.cells[row][col].value == 0:
            self.cells[row][col].set_temp(0)

    def sketch(self, value):
        row, col = self.selected
        self.cells[row][col].set_temp(value)

    def place(self, value):
        row, col = self.selected
        if self.cells[row][col].value == 0:
            self.cells[row][col].set_value(value)
            if self.is_valid(value, (row, col)) and self.solve():
                return True
            else:
                self.cells[row][col].set_value(0)
                self.cells[row][col].set_temp(0)
                return False

    def is_valid(self, num, pos):
        for i in range(9):
            if self.cells[pos[0]][i].value == num and pos[1] != i:
                return False
            if self.cells[i][pos[1]].value == num and pos[0] != i:
                return False

        box_x = pos[1] // 3
        box_y = pos[0] // 3
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.cells[i][j].value == num and (i, j) != pos:
                    return False

        return True

    def solve(self):
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if self.is_valid(i, (row, col)):
                self.cells[row][col].set_value(i)

                if self.solve():
                    return True

                self.cells[row][col].set_value(0)

        return False

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.cells[i][j].value == 0:
                    return (i, j)
        return None

class SudokuGame:
    def __init__(self):
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Sudoku")
        self.board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        self.grid = Grid(self.board)
        self.key = None
        self.run()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    clicked = self.grid.click(pos)
                    if clicked:
                        self.grid.select(clicked[0], clicked[1])
                        self.key = None
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.key = 1
                    if event.key == pygame.K_2:
                        self.key = 2
                    if event.key == pygame.K_3:
                        self.key = 3
                    if event.key == pygame.K_4:
                        self.key = 4
                    if event.key == pygame.K_5:
                        self.key = 5
                    if event.key == pygame.K_6:
                        self.key = 6
                    if event.key == pygame.K_7:
                        self.key = 7
                    if event.key == pygame.K_8:
                        self.key = 8
                    if event.key == pygame.K_9:
                        self.key = 9
                    if event.key == pygame.K_DELETE:
                        self.grid.clear()
                        self.key = None
                    if event.key == pygame.K_RETURN:
                        i, j = self.grid.selected
                        if self.grid.cells[i][j].temp_value != 0:
                            if self.grid.place(self.grid.cells[i][j].temp_value):
                                print("Success")
                            else:
                                print("Wrong")
                            self.key = None
                        
                    if self.grid.selected and self.key:
                        self.grid.sketch(self.key)

            self.update()

    def update(self):
        self.win.fill(BACKGROUND_COLOR)
        self.grid.draw(self.win)
        pygame.display.update()

if __name__ == "__main__":
    SudokuGame()

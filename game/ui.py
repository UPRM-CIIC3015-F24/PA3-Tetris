import pygame

from game.constants import background_image, ROWS, COLUMNS, CELL_SIZE, GRID_X, GRID_Y, NEXT_PIECE_X, NEXT_PIECE_Y, \
    SCORE_X, SCORE_Y, TEXT_COLOR, SCREEN_WIDTH, FONT, SCREEN_HEIGHT

class UI:
    def __init__(self, screen):
        self.screen = screen

    def draw_board(self, board, current_piece, next_piece):
        self.screen.blit(background_image, (0, 0))
        for y in range(ROWS):
            for x in range(COLUMNS):
                if board.grid[y][x]:
                    pygame.draw.rect(self.screen,
                                     board.grid[y][x],
                                     (GRID_X + x * CELL_SIZE, GRID_Y + y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        for y, row in enumerate(current_piece.get_current_shape()):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen,
                                     current_piece.color,
                                     (GRID_X + (current_piece.x + x) * CELL_SIZE,
                                      GRID_Y + (current_piece.y + y) * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        # TODO TASK 2 Draw the nex_piece
        #   To draw the next piece the code is similar to the draw of the current_piece (previous code)
        #   but using next_piece instead of current_piece.
        #   HINT: The rectangle X is NEXT_PIECE_X + 50 + x * CELL_SIZE
        #         The rectangle Y is NEXT_PIECE_Y + 40 + y * CELL_SIZE

        score_text = FONT.render(f"{board.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (SCORE_X, SCORE_Y))
        pygame.display.flip()

    def draw_game_over(self):
        game_over_text = FONT.render("GAME OVER", True, TEXT_COLOR)
        restart_text = FONT.render("Press R to Restart", True, TEXT_COLOR)
        self.screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 3))
        self.screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 3 + 50))
        pygame.display.flip()

    def draw_pause(self):
        pause_text = FONT.render("PAUSED", True, TEXT_COLOR)
        self.screen.blit(pause_text, (SCREEN_WIDTH // 2 - pause_text.get_width() // 2, SCREEN_HEIGHT // 3))
        pause_text = FONT.render("Press P to Resume", True, TEXT_COLOR)
        self.screen.blit(pause_text, (SCREEN_WIDTH // 2 - pause_text.get_width() // 2, SCREEN_HEIGHT // 3 + 50))
        pygame.display.flip()

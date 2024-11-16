import pygame
import sys
import random

pygame.init()
pygame.font.init()

from game.board import Board
from game.tetrimino import Tetrimino
from game.ui import UI
from game.constants import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.ui = UI(self.screen)
        self.current_piece = None
        self.next_piece = None
        self.last_drop_time = pygame.time.get_ticks()
        # TODO TASK 4: Implement game over tracking
        #   Add a game_over attribute
        #   Hint: Make the a boolean and defined them as False
        # TODO TASK 5: Implement pause state tracking
        #   Add a paused attribute
        #   # Hint: Make the a boolean and defined them as False

    def new_piece(self):
        self.current_piece = self.next_piece or Tetrimino(random.choice(list(SHAPES.keys())))
        self.next_piece = Tetrimino(random.choice(list(SHAPES.keys())))
        # TODO TASK 4: Implement game over logic when a new piece cannot be placed at the top
        #   If the current piece is not a valid position modify the game_over attribute to True

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self.board.is_valid_position(self.current_piece, -1, 0):
                        self.current_piece.x -= 1
                        MOVE_SOUND.play()
                elif event.key == pygame.K_RIGHT:
                    if self.board.is_valid_position(self.current_piece, 1, 0):
                        self.current_piece.x += 1
                        MOVE_SOUND.play()
                elif event.key == pygame.K_DOWN:
                    if self.board.is_valid_position(self.current_piece, 0, 1):
                        self.current_piece.y += 1
                elif event.key == pygame.K_UP:
                    rotated = self.current_piece.rotation
                    self.current_piece.rotate()
                    if not self.board.is_valid_position(self.current_piece, 0, 0):
                        self.current_piece.rotation = rotated
                elif event.key == pygame.K_SPACE:
                    self.drop_piece()
                # TODO TASK 5: Implement pause game functionality (toggle the paused state)
                #   If the key is k_p toggle the paused attribute
                # TODO TASK 4: Implement game_over  functionality
                #   If the key is k_r and game_over is True called restart_game()

    def drop_piece(self):
        # TODO TASK 3: Implement the logic to drop the piece.
        #   Move the current piece downwards while it remains in a valid position.
        #   Once it can no longer move down, lock the piece in place on the board.
        #   Play a sound effect when the piece is successfully placed.
        #   Generate a new piece after the current piece is locked.
        pass  # Placeholder, to be replaced with the actual implementation.

    def update(self):
        if pygame.time.get_ticks() - self.last_drop_time >= PIECE_DROP_TIME:
            if self.board.is_valid_position(self.current_piece, 0, 1):
                self.current_piece.y += 1
            else:
                self.board.lock_piece(self.current_piece)
                PLACE_SOUND.play()
                self.new_piece()
            self.last_drop_time = pygame.time.get_ticks()

    def run(self):
        self.new_piece()
        while True:
            self.handle_input()
            self.update()
            self.ui.draw_board(self.board, self.current_piece, self.next_piece)
            # TODO TASK 4: Implement the logic to display game over screen
            #   If game_over is true call draw_game_over()
            # TODO TASK 5: Implement the logic to display pause screen
            #   If paused is true call draw_pause()
            self.clock.tick(FPS)

    def restart_game(self):
        self.board = Board()  # Reset board and score
        self.game_over = False
        self.paused = False
        self.new_piece()

if __name__ == "__main__":
    game = Game()
    game.run()

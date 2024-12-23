# Tetris Game (PA3)

## CIIC3015 – Introduction to Programming

![image](https://github.com/user-attachments/assets/cbfe6743-41c7-45d8-8119-c140ac8184a0)


### **Project Overview**
This is a Python-based implementation of the classic *Tetris* game using the **Pygame** library. The game allows players to manipulate falling Tetrimino pieces, attempting to fill rows on the game grid without leaving gaps. When a row is filled, it is cleared from the board, and the player's score increases. The game ends when there is no room for a new piece to appear at the top of the screen.

### **Features to Implement**
- Rotation of Tetrimino pieces.
- Display of the next Tetrimino.
- Logic to drop pieces and lock them in place.
- Scorekeeping and line clearing logic.
- Pause and game-over functionality.

---

### **Controls**
- **Left Arrow**: Move piece left.
- **Right Arrow**: Move piece right.
- **Down Arrow**: Speed up piece fall.
- **Up Arrow**: Rotate piece.
- **P**: Pause and resume the game.
- **R**: Restart the game after game over.

---

### **Game Rules**
- The game is played on a grid where Tetrimino shapes fall from the top.
- Players can move and rotate the pieces to fill entire rows.
- When a row is filled completely, it is cleared, and the score is updated.
- The game ends when a new Tetrimino cannot be placed on the grid.

---

### **Structure**
The game consists of the following files:

- **main.py**: The main game loop and logic.
- **board.py**: Contains the logic for the Tetris board and line-clearing functionality.
- **tetrimino.py**: Defines the Tetrimino class and its rotations.
- **ui.py**: Handles the rendering of the game, including drawing the board, pieces, and score.
- **constants.py**: Contains game constants, including grid size, screen dimensions, and piece shapes.
- **sounds.py**: Handles loading and playing sound effects for different game actions.
- **README.md**: This file, which provides instructions for setting up and running the game.

---

### **Tasks to Complete**
The starter code contains several incomplete sections marked with `TODO` comments. These sections should be completed as per the following requirements:
1. **Task 1**: Implement `rotate_piece` in `tetrimino.py`.
2. **Task 2**: Draw the next piece in `ui.py`.
3. **Task 3**: Implement `drop_piece()` to drop the current piece downwards.
4. **Task 4**: Implement game over logic.
5. **Task 5**: Implement pause functionality.
6. **Task 6**: Implement line clearing using recursion.
7. **Task 7**: Update the score when lines are cleared.
8. **Task 8**: Add the teams name in this README file

---

### **Acknowledgments**
This project was developed as part of the **CIIC3015** course at University of Puerto Rico - Mayagüez. The Tetris game was originally created by Alexey Pajitnov in 1984.

---

### **Contact Information**
For any questions or suggestions, please contact:
- **Instructor**: Alanis Negroni ([alanis.negroni@upr.edu](mailto:alanis.negroni@upr.edu))
- **Student Names**: [Student Name 1] & [Student Name 2]

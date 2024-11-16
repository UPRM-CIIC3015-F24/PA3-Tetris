from game.constants import COLUMNS, SHAPES, COLORS, MOVE_SOUND

class Tetrimino:
    def __init__(self, shape_key):
        self.shape_key = shape_key
        self.shape = SHAPES[shape_key]
        self.color = COLORS[shape_key]
        self.rotation = 0
        self.x = COLUMNS // 2 - len(self.shape[0][0]) // 2
        self.y = 0

    def get_current_shape(self):
        return self.shape[self.rotation]

    def rotate(self):
        # TODO TASK 1: Implement the rotation logic for the shape.
        #   Update the 'rotation' attribute to the next rotation state based on the shape's length.
        #   Ensure that the rotation wraps around to the first state once the end is reached.
        #   Play the rotation sound effect when the shape is rotated.
        pass # Placeholder remove once your code is implemented
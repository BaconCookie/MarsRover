class Plateau:

    def __init__(self, x, y):
        self.max_x = x
        self.max_y = y
        self.currently_occupied_positions = []

    def add_to_currently_occupied_positions(self, new_x, new_y):
        if self.is_valid_position(new_x, new_y):
            self.currently_occupied_positions.append([new_x, new_y])
            return True
        else:
            return False

    def is_valid_position(self, x, y):
        return self.is_on_plateau(x, y) and self.causes_no_collision(x, y)

    def is_on_plateau(self, x, y):
        return x <= self.max_x and y <= self.max_y and (self.max_x >= 0 or self.max_y >= 0)

    def causes_no_collision(self, x, y):
        return [x, y] not in self.currently_occupied_positions

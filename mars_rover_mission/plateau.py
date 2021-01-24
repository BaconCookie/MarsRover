class Plateau:

    def __init__(self, x, y):
        if self.coordinates_are_positive_ints_or_zero(x, y):
            self.max_x = x
            self.max_y = y
            self.currently_occupied_positions = []
        else:
            raise ValueError('Plateau coordinates invalid')

    def add_to_currently_occupied_positions(self, new_x, new_y):
        if self.is_valid_position(new_x, new_y):
            self.currently_occupied_positions.append([new_x, new_y])
            return True
        else:
            return False

    def update_currently_occupied_positions(self, old_x, old_y, new_x, new_y):
        if [old_x, old_y] in self.currently_occupied_positions and self.is_valid_position(new_x, new_y):
            self.currently_occupied_positions.remove([old_x, old_y])
            self.currently_occupied_positions.append([new_x, new_y])
            return True
        else:
            return False

    def is_valid_position(self, x, y):
        if self.coordinates_are_positive_ints_or_zero(x, y):
            return self.is_on_plateau(x, y) and self.causes_no_collision(x, y)
        else:
            return False

    def coordinates_are_positive_ints_or_zero(self, x, y):
        return isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0

    def is_on_plateau(self, x, y):
        return x <= self.max_x and y <= self.max_y

    def causes_no_collision(self, x, y):
        return [x, y] not in self.currently_occupied_positions

    def __eq__(self, other):
        if not isinstance(other, Plateau):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.max_x == other.max_x and self.max_y == other.max_y and self.currently_occupied_positions == other.currently_occupied_positions

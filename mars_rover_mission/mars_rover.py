class MarsRover:

    def __init__(self, start_x, start_y, start_heading, instructions, plateau):
        self.plateau = plateau
        if not self.plateau.add_to_currently_occupied_positions(start_x, start_y):
            raise ValueError
        self.x = start_x
        self.y = start_y
        self.heading = start_heading
        self.instructions = instructions

    def explore_plateau_get_final_position(self):
        for order in self.instructions:
            if order == 'L':
                self.turn_left()
            if order == 'R':
                self.turn_right()
            if order == 'M':
                self.move_forward_if_possible()
        return [self.x, self.y, self.heading]

    def move_forward_if_possible(self):
        new_x, new_y = self.calc_new_position()
        # Update position if valid, else the 'M' order is ignored
        if self.plateau.update_currently_occupied_positions(self.x, self.y, new_x, new_y):
            self.x = new_x
            self.y = new_y

    # Todo figure out a more elegant solution for turns(e.g. mapping)
    def turn_left(self):
        new_heading = ''
        if self.heading == 'N':
            new_heading = 'W'
        if self.heading == 'E':
            new_heading = 'N'
        if self.heading == 'S':
            new_heading = 'E'
        if self.heading == 'W':
            new_heading = 'S'
        self.heading = new_heading

    def turn_right(self):
        new_heading = ''
        if self.heading == 'N':
            new_heading = 'E'
        if self.heading == 'E':
            new_heading = 'S'
        if self.heading == 'S':
            new_heading = 'W'
        if self.heading == 'W':
            new_heading = 'N'
        self.heading = new_heading

    def calc_new_position(self):
        if self.heading == 'N':
            new_x = self.x
            new_y = self.y + 1
        if self.heading == 'E':
            new_x = self.x + 1
            new_y = self.y
        if self.heading == 'S':
            new_x = self.x
            new_y = self.y - 1
        if self.heading == 'W':
            new_x = self.x - 1
            new_y = self.y
        return new_x, new_y

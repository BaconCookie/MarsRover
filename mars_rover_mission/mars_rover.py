class MarsRover:

    def __init__(self, start_x, start_y, start_heading, instructions, plateau):
        self.plateau = plateau
        if not self.plateau.add_to_currently_occupied_positions(start_x, start_y):
            raise ValueError
        self.x = start_x
        self.y = start_y
        self.heading = start_heading
        self.instructions = instructions

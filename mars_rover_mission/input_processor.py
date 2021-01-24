from mars_rover_mission.plateau import Plateau


class InputProcessor:
    def __init__(self):
        pass

    def init_plateau(self, size):
        # casting raises ValueError if impossible
        if len(size.split()) != 2:
            raise ValueError
        else:
            max_x = int(size.split()[0])
            max_y = int(size.split()[1])
            if self.is_positive_integer(max_x) and self.is_positive_integer(max_y):
                return Plateau(max_x, max_y)
            else:
                raise ValueError

    def get_startposition(self, start_position):
        x, y, heading = start_position.split()
        x = int(x)
        y = int(y)
        if not self.is_zero_or_positive_integer(x):
            raise ValueError
        if not self.is_zero_or_positive_integer(y):
            raise ValueError
        if not self.is_valid_heading(heading):
            raise ValueError
        return x, y, heading

    def validate_instructions(self, instructs):
        for letter in instructs:
            if letter not in ['L', 'R', 'M']:
                raise ValueError
        return True

    def is_positive_integer(self, integer):
        return integer > 0

    def is_zero_or_positive_integer(self, integer):
        return integer >= 0

    def is_valid_heading(self, heading):
        return heading in ['N', 'E', 'S', 'W']

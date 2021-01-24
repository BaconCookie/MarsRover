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

    def is_positive_integer(self, integer):
        return integer > 0

    def is_valid_heading(self, heading):
        return heading in ['N', 'E', 'S', 'W']

import sys

from mars_rover_mission.mars_rover import MarsRover
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

    def init_mars_rover(self, instructions, plateau, rover_count, startposition):
        try:
            start_x, start_y, start_heading = self.get_startposition(startposition)
        except ValueError:
            print(f'Start position of MarsRover{rover_count} invalid. Please try again.')
            raise
        try:
            self.validate_instructions(instructions)
        except ValueError:
            print(f'Instructions of MarsRover{rover_count} invalid. Please try again.')
            raise
        try:
            rover = MarsRover(start_x, start_y, start_heading, instructions, plateau)
        except ValueError:
            print(f'Initiating MarsRover{rover_count} failed. Please try again.')
            raise
        return rover, start_x, start_y

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
        for letter in instructs.strip():
            if letter not in ['L', 'R', 'M']:
                raise ValueError
        return True

    def is_positive_integer(self, integer):
        return integer > 0

    def is_zero_or_positive_integer(self, integer):
        return integer >= 0

    def is_valid_heading(self, heading):
        return heading in ['N', 'E', 'S', 'W']

    def run_mission(self, mars_rovers):
        fin_positions = []
        for i, mars_rover in enumerate(mars_rovers):
            fin_position = mars_rover.explore_plateau_get_final_position()
            print(f'Final coordinates of MarsRover {i+1}: ', mars_rover.x, mars_rover.y, mars_rover.heading)
            fin_positions.append(fin_position)
        return fin_positions

    def process_input(self):
        print('Welcome to Mars Rover Mission. Please enter the mission data: ')

        startposition = ''
        mars_rovers_on_mission = []
        line_count = 0
        rover_count = 1
        for line in sys.stdin:
            if 'q' == line.rstrip():
                break
            if 'f' == line.rstrip() or '' == line.rstrip():
                print('Calculating ...')
                final_positions = self.run_mission(mars_rovers_on_mission)
                print('All final positions: ', final_positions)
                sys.exit(0)

            if line_count == 0:
                plateau_size = line
                print(f'Plateau size : {plateau_size}')
                try:
                    plateau = self.init_plateau(plateau_size)
                except ValueError:
                    print('Plateau size invalid. Please try again. Enter two positive integers separated by a space.')
                    sys.exit(1)

            if line_count >= 1 and line_count % 2 == 1:
                startposition = line
                print(f'MarsRover {rover_count} startposition: {startposition}')

            if line_count >= 1 and line_count % 2 == 0:
                instructions = line
                print(f'MarsRover {rover_count} instructions: {instructions}')

                try:
                    rover, start_x, start_y = self.init_mars_rover(instructions, plateau, rover_count, startposition)
                except ValueError:
                    sys.exit(1)

                mars_rovers_on_mission.append(rover)

                rover_count += 1

            line_count += 1

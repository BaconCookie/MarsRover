import unittest

from mars_rover_mission.mars_rover import MarsRover
from mars_rover_mission.plateau import Plateau


class TestMarsRover(unittest.TestCase):

    def setUp(self):
        self.mars_rover = MarsRover(start_x=1, start_y=2, start_heading='N', instructions='LMLMLMLMM',
                                    plateau=Plateau(5, 5))

    def tearDown(self):
        self.mars_rover = None

    def test_mars_rover_exists(self):
        self.assertIsInstance(self.mars_rover, MarsRover, "MarsRover class is missing or initiated incorrectly")

    def test_mars_rover_cannot_be_init_with_invalid_starting_position_x_not_on_plateau(self):
        # x not on the plateau
        x = 6
        y = 3
        with self.assertRaises(ValueError):
            MarsRover(start_x=x, start_y=y, start_heading='N', instructions='LMLMLMLMM', plateau=Plateau(5, 5))

    def test_mars_rover_cannot_be_init_with_invalid_starting_position_y_not_on_plateau(self):
        # y not on the plateau
        x = 3
        y = 6
        with self.assertRaises(ValueError):
            MarsRover(start_x=x, start_y=y, start_heading='N', instructions='LMLMLMLMM', plateau=Plateau(5, 5))

    def test_mars_rover_cannot_be_init_with_invalid_starting_position_x_and_y_not_on_plateau(self):
        # x & y not on the plateau
        x = 6
        y = 6
        with self.assertRaises(ValueError):
            MarsRover(start_x=x, start_y=y, start_heading='N', instructions='LMLMLMLMM', plateau=Plateau(5, 5))

    def test_mars_rover_cannot_be_init_with_invalid_starting_position_already_occupied(self):
        # init a second MarsRover in the same spot is invalid (x & y are equal to the one in the setUp)
        x = 1
        y = 2
        with self.assertRaises(ValueError):
            MarsRover(start_x=x, start_y=y, start_heading='N', instructions='LMLMLMLMM', plateau=Plateau(5, 5))

    def test_turn_left(self):
        self.mars_rover.turn_left()
        heading_after_turning_left = self.mars_rover.heading
        expected_heading = 'W'
        self.assertEqual(heading_after_turning_left, expected_heading)

    def test_turn_right(self):
        self.mars_rover.turn_right()
        heading_after_turning_left = self.mars_rover.heading
        expected_heading = 'E'
        self.assertEqual(heading_after_turning_left, expected_heading)

    def test_move_to_valid_position(self):
        pass

    def test_move_to_invalid_position_not_on_plateau(self):
        pass

    def test_move_to_invalid_position_already_occupied(self):
        pass


if __name__ == '__main__':
    unittest.main()

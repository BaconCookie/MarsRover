import unittest

from mars_rover_mission.mars_rover import MarsRover
from mars_rover_mission.plateau import Plateau


class TestMarsRover(unittest.TestCase):

    def setUp(self):
        self.plateau = Plateau(5, 5)
        self.mars_rover = MarsRover(start_x=1, start_y=2, start_heading='N', instructions='LMLMLMLMM',
                                    plateau=self.plateau)

    def tearDown(self):
        self.plateau = None
        self.mars_rover = None

    def test_mars_rover_exists(self):
        self.assertIsInstance(self.mars_rover, MarsRover, "MarsRover class is missing or initiated incorrectly")

    def test_mars_rover_cannot_be_init_with_invalid_starting_position_x_not_on_plateau(self):
        # x not on the plateau
        x = 6
        y = 3
        with self.assertRaises(ValueError):
            MarsRover(start_x=x, start_y=y, start_heading='N', instructions='LMLMLMLMM', plateau=self.plateau)

    def test_mars_rover_cannot_be_init_with_invalid_starting_position_y_not_on_plateau(self):
        # y not on the plateau
        x = 3
        y = 6
        with self.assertRaises(ValueError):
            MarsRover(start_x=x, start_y=y, start_heading='N', instructions='LMLMLMLMM', plateau=self.plateau)

    def test_mars_rover_cannot_be_init_with_invalid_starting_position_x_and_y_not_on_plateau(self):
        # x & y not on the plateau
        x = 6
        y = 6
        with self.assertRaises(ValueError):
            MarsRover(start_x=x, start_y=y, start_heading='N', instructions='LMLMLMLMM', plateau=self.plateau)

    def test_mars_rover_cannot_be_init_with_invalid_starting_position_already_occupied(self):
        # init a second MarsRover in the same spot is invalid (x & y are equal to the one in the setUp)
        x = 1
        y = 2
        with self.assertRaises(ValueError):
            MarsRover(start_x=x, start_y=y, start_heading='N', instructions='LMLMLMLMM', plateau=self.plateau)

    def test_turn_left_start_N(self):
        self.mars_rover.turn_left()
        heading_after_turning_left = self.mars_rover.heading
        expected_heading = 'W'
        self.assertEqual(expected_heading, heading_after_turning_left)

    def test_turn_left_four_times_start_N(self):
        self.mars_rover.turn_left()
        heading_after_turning_left = self.mars_rover.heading
        expected_heading = 'W'
        self.assertEqual(expected_heading, heading_after_turning_left)
        self.mars_rover.turn_left()
        heading_after_turning_left = self.mars_rover.heading
        expected_heading = 'S'
        self.assertEqual(expected_heading, heading_after_turning_left)
        self.mars_rover.turn_left()
        heading_after_turning_left = self.mars_rover.heading
        expected_heading = 'E'
        self.assertEqual(expected_heading, heading_after_turning_left)
        self.mars_rover.turn_left()
        heading_after_turning_left = self.mars_rover.heading
        expected_heading = 'N'
        self.assertEqual(expected_heading, heading_after_turning_left)

    def test_turn_right_start_N(self):
        self.mars_rover.turn_right()
        heading_after_turning_left = self.mars_rover.heading
        expected_heading = 'E'
        self.assertEqual(expected_heading, heading_after_turning_left)

    def test_turn_right_four_times_start_N(self):
        self.mars_rover.turn_right()
        heading_after_turning_left = self.mars_rover.heading
        expected_heading = 'E'
        self.assertEqual(expected_heading, heading_after_turning_left)
        self.mars_rover.turn_right()
        heading_after_turning_left = self.mars_rover.heading
        expected_heading = 'S'
        self.assertEqual(expected_heading, heading_after_turning_left)
        self.mars_rover.turn_right()
        heading_after_turning_left = self.mars_rover.heading
        expected_heading = 'W'
        self.assertEqual(expected_heading, heading_after_turning_left)
        self.mars_rover.turn_right()
        heading_after_turning_left = self.mars_rover.heading
        expected_heading = 'N'
        self.assertEqual(expected_heading, heading_after_turning_left)

    def test_move_to_valid_position_North(self):
        mars_rover_heading_north = MarsRover(start_x=3, start_y=3, start_heading='N', instructions='LMLMLMLMM',
                                             plateau=Plateau(5, 5))
        mars_rover_heading_north.move_forward_if_possible()
        expected_x = 3
        expected_y = 4
        actual_x = mars_rover_heading_north.x
        actual_y = mars_rover_heading_north.y
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)

    def test_move_to_valid_position_East(self):
        mars_rover_heading_east = MarsRover(start_x=3, start_y=3, start_heading='E', instructions='LMLMLMLMM',
                                            plateau=Plateau(5, 5))
        mars_rover_heading_east.move_forward_if_possible()
        expected_x = 4
        expected_y = 3
        actual_x = mars_rover_heading_east.x
        actual_y = mars_rover_heading_east.y
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)

    def test_move_to_valid_position_South(self):
        mars_rover_heading_south = MarsRover(start_x=3, start_y=3, start_heading='S', instructions='LMLMLMLMM',
                                             plateau=Plateau(5, 5))
        mars_rover_heading_south.move_forward_if_possible()
        expected_x = 3
        expected_y = 2
        actual_x = mars_rover_heading_south.x
        actual_y = mars_rover_heading_south.y
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)

    def test_move_to_valid_position_West(self):
        mars_rover_heading_west = MarsRover(start_x=3, start_y=3, start_heading='W', instructions='LMLMLMLMM',
                                            plateau=Plateau(5, 5))
        mars_rover_heading_west.move_forward_if_possible()
        expected_x = 2
        expected_y = 3
        actual_x = mars_rover_heading_west.x
        actual_y = mars_rover_heading_west.y
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)

    def test_doesnt_move_to_invalid_position_not_on_plateau_top_right_north(self):
        mars_rover_heading_north_on_top_right_edge = MarsRover(start_x=5, start_y=5, start_heading='N',
                                                               instructions='LMLMLMLMM',
                                                               plateau=self.plateau)
        mars_rover_heading_north_on_top_right_edge.move_forward_if_possible()
        expected_x = 5
        expected_y = 5
        actual_x = mars_rover_heading_north_on_top_right_edge.x
        actual_y = mars_rover_heading_north_on_top_right_edge.y
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)

    def test_doesnt_move_to_invalid_position_not_on_plateau_top_right_east(self):
        mars_rover_heading_east_on_top_right_edge = MarsRover(start_x=5, start_y=5, start_heading='E',
                                                              instructions='LMLMLMLMM',
                                                              plateau=self.plateau)
        mars_rover_heading_east_on_top_right_edge.move_forward_if_possible()
        expected_x = 5
        expected_y = 5
        actual_x = mars_rover_heading_east_on_top_right_edge.x
        actual_y = mars_rover_heading_east_on_top_right_edge.y
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)

    def test_doesnt_move_to_invalid_position_not_on_plateau_bottom_left_south(self):
        mars_rover_heading_east_on_top_right_edge = MarsRover(start_x=0, start_y=0, start_heading='S',
                                                              instructions='LMLMLMLMM',
                                                              plateau=self.plateau)
        mars_rover_heading_east_on_top_right_edge.move_forward_if_possible()
        expected_x = 0
        expected_y = 0
        actual_x = mars_rover_heading_east_on_top_right_edge.x
        actual_y = mars_rover_heading_east_on_top_right_edge.y
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)

    def test_doesnt_move_to_invalid_position_not_on_plateau_bottom_left_west(self):
        mars_rover_heading_east_on_top_right_edge = MarsRover(start_x=0, start_y=0, start_heading='W',
                                                              instructions='LMLMLMLMM',
                                                              plateau=self.plateau)
        mars_rover_heading_east_on_top_right_edge.move_forward_if_possible()
        expected_x = 0
        expected_y = 0
        actual_x = mars_rover_heading_east_on_top_right_edge.x
        actual_y = mars_rover_heading_east_on_top_right_edge.y
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)

    def test_move_to_invalid_position_already_occupied(self):
        mars_rover_2 = MarsRover(start_x=1, start_y=1, start_heading='N', instructions='M', plateau=self.plateau)
        # position forward would be (x=1, y=2)
        # --> invalid for this rover to move to, since this position is already occupied by the rover in the setUp
        mars_rover_2.move_forward_if_possible()
        expected_x = 1
        expected_y = 1
        actual_x = mars_rover_2.x
        actual_y = mars_rover_2.y
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)

    def test_explore_plateau_by_following_instructions_and_finish_in_correct_position_example_1(self):
        actual_position = self.mars_rover.explore_plateau_get_final_position()
        expected_position = [1, 3, 'N']
        self.assertEqual(expected_position, actual_position)

    def test_explore_plateau_example_1_with_2nd_mars_rover_on_plateau(self):
        mars_rover_2 = MarsRover(start_x=3, start_y=3, start_heading='E', instructions='MMRMMRMRRM',
                                 plateau=self.plateau)
        actual_position = self.mars_rover.explore_plateau_get_final_position()
        expected_position = [1, 3, 'N']
        self.assertEqual(expected_position, actual_position)

    def test_explore_plateau_by_following_instructions_and_finish_in_correct_position_example_2(self):
        mars_rover_2 = MarsRover(start_x=3, start_y=3, start_heading='E', instructions='MMRMMRMRRM',
                                 plateau=self.plateau)
        actual_position = mars_rover_2.explore_plateau_get_final_position
        expected_position = [5, 1, 'E']
        self.assertEqual(expected_position, actual_position)


if __name__ == '__main__':
    unittest.main()

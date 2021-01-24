import unittest

from mars_rover_mission.plateau import Plateau


class TestPlateau(unittest.TestCase):

    def setUp(self):
        self.plateau = Plateau(5, 5)

    def tearDown(self):
        self.plateau = None

    def test_plateau_exists(self):
        self.assertIsInstance(self.plateau, Plateau, "Mission class is missing or initiated incorrectly")

    def test_plateau_size_can_be_valid_and_narrow_x0(self):
        self.assertTrue(Plateau(0, 3))

    def test_plateau_size_can_be_valid_and_narrow_y0(self):
        self.assertTrue(Plateau(1, 0))

    def test_plateau_size_can_be_valid_and_allow_no_movement_x0_y0(self):
        self.assertTrue(Plateau(0, 0))

    def test_plateau_size_cannot_be_invalid_negavtive_x(self):
        x = -1
        y = 5
        with self.assertRaises(ValueError):
            Plateau(x, y)

    def test_plateau_size_cannot_be_invalid_negavtive_y(self):
        x = 1
        y = -5
        with self.assertRaises(ValueError):
            Plateau(x, y)

    def test_plateau_size_cannot_be_invalid_negavtive_x_and_y(self):
        x = -2
        y = -3
        with self.assertRaises(ValueError):
            Plateau(x, y)

    def test_plateau_size_cannot_be_invalid_floats(self):
        x = 0.5
        y = 3.7
        with self.assertRaises(ValueError):
            Plateau(x, y)

    def test_add_valid_position_to_currently_occupied_positions(self):
        self.plateau.add_to_currently_occupied_positions(3, 3)
        expected = [[3, 3]]
        self.assertEqual(self.plateau.currently_occupied_positions, expected)

    def test_add_valid_position_on_bottom_left_corner_to_currently_occupied_positions(self):
        self.assertTrue(self.plateau.add_to_currently_occupied_positions(0, 0))
        expected = [[0, 0]]
        self.assertEqual(self.plateau.currently_occupied_positions, expected)

    def test_add_valid_position_on_top_right_corner_to_currently_occupied_positions(self):
        self.assertTrue(self.plateau.add_to_currently_occupied_positions(5, 5))
        expected = [[5, 5]]
        self.assertEqual(self.plateau.currently_occupied_positions, expected)

    def test_add_invalid_too_large_x_position_to_currently_occupied_positions_returns_false(self):
        self.assertFalse(self.plateau.add_to_currently_occupied_positions(6, 3))

    def test_add_invalid_too_large_y_position_to_currently_occupied_positions_returns_false(self):
        self.assertFalse(self.plateau.add_to_currently_occupied_positions(3, 6))

    def test_add_invalid_too_large_x_and_y_position_to_currently_occupied_positions_returns_false(self):
        self.assertFalse(self.plateau.add_to_currently_occupied_positions(6, 6))

    def test_add_invalid_negative_x_position_to_currently_occupied_positions_returns_false(self):
        self.assertFalse(self.plateau.add_to_currently_occupied_positions(-1, 3))

    def test_add_invalid_negative_y_position_to_currently_occupied_positions_returns_false(self):
        self.assertFalse(self.plateau.add_to_currently_occupied_positions(3, -1))

    def test_add_invalid_negative_x_and_y_position_to_currently_occupied_positions_returns_false(self):
        self.assertFalse(self.plateau.add_to_currently_occupied_positions(-1, -6))

    def test_add_invalid_float_x_position_to_currently_occupied_positions_returns_false(self):
        self.assertFalse(self.plateau.add_to_currently_occupied_positions(0.5, 3))

    def test_add_invalid_float_y_position_to_currently_occupied_positions_returns_false(self):
        self.assertFalse(self.plateau.add_to_currently_occupied_positions(3, 1.7))

    def test_add_invalid_float_x_and_y_position_to_currently_occupied_positions_returns_false(self):
        self.assertFalse(self.plateau.add_to_currently_occupied_positions(3.3, 4.4))

    def test_update_currently_occupied_positions_from_valid_to_valid(self):
        start_x = 3
        start_y = 3
        self.plateau.add_to_currently_occupied_positions(start_x, start_y)  # valid 'from' position
        new_x = 3
        new_y = 4
        self.assertTrue(self.plateau.update_currently_occupied_positions(start_x, start_y, new_x, new_y))

    def test_update_currently_occupied_positions_from_valid_to_invalid_because_occupied(self):
        start_x = 3
        start_y = 3
        self.plateau.add_to_currently_occupied_positions(start_x, start_y)  # valid 'from' position
        new_x = 3
        new_y = 4
        # occupy the 'to' position and thereby making it invalid to move to:
        self.plateau.add_to_currently_occupied_positions(new_x, new_y)
        self.assertFalse(self.plateau.update_currently_occupied_positions(start_x, start_y, new_x, new_y))

    def test_update_currently_occupied_positions_from_valid_to_invalid_because_not_on_plateau(self):
        start_x = 5
        start_y = 5
        self.plateau.add_to_currently_occupied_positions(start_x, start_y)  # valid 'from' position
        new_x = 5
        new_y = 6  # value is outside of plateau
        self.assertFalse(self.plateau.update_currently_occupied_positions(start_x, start_y, new_x, new_y))

    def test_update_currently_occupied_positions_from_valid_to_invalid_because_float(self):
        start_x = 5
        start_y = 5
        self.plateau.add_to_currently_occupied_positions(start_x, start_y)  # valid 'from' position
        new_x = 5
        new_y = 4.5  # float values are not valid plateau coordinates
        self.assertFalse(self.plateau.update_currently_occupied_positions(start_x, start_y, new_x, new_y))


if __name__ == '__main__':
    unittest.main()

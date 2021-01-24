import unittest

from mars_rover_mission.plateau import Plateau


class TestPlateau(unittest.TestCase):

    def setUp(self):
        self.plateau = Plateau(5, 5)

    def tearDown(self):
        self.plateau = None

    def test_plateau_exists(self):
        self.assertIsInstance(self.plateau, Plateau, "Mission class is missing or initiated incorrectly")

    def test_add_valid_position_to_currently_occupied_positions(self):
        self.plateau.add_to_currently_occupied_positions(3, 3)
        expected = [[3, 3]]
        self.assertEqual(self.plateau.currently_occupied_positions, expected)

    def test_add_invalid_position_to_currently_occupied_positions_returns_false(self):
        self.assertFalse(self.plateau.add_to_currently_occupied_positions(3, 6))

    def test_update_currently_occupied_positions_from_valid_to_valid(self):
        start_x = 3
        start_y = 3
        self.plateau.add_to_currently_occupied_positions(start_x, start_y)  # valid 'from' position
        new_x = 3
        new_y = 4
        self.assertTrue(self.plateau.update_currently_occupied_positions(start_x, start_y, new_x, new_y))

    def test_update_currently_occupied_positions_from_valid_to_invalid(self):
        start_x = 3
        start_y = 3
        self.plateau.add_to_currently_occupied_positions(start_x, start_y)  # valid 'from' position
        new_x = 3
        new_y = 4
        # occupy the 'to' position and thereby making it invalid to move to:
        self.plateau.add_to_currently_occupied_positions(new_x, new_y)
        self.assertFalse(self.plateau.update_currently_occupied_positions(start_x, start_y, new_x, new_y))


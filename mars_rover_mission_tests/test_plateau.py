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

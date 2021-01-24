import unittest

from mars_rover_mission.plateau import Plateau


class TestPlateau(unittest.TestCase):

    def test_plateau_exists(self):
        plateau = Plateau(5, 5)
        self.assertIsInstance(plateau, Plateau, "Mission class is missing or initiated incorrectly")

    def test_add_valid_position_to_currently_occupied_positions(self):
        plateau = Plateau(5, 5)
        plateau.currently_occupied_positions.append([3, 3])
        expected = [[3, 3]]
        self.assertEqual(plateau.currently_occupied_positions, expected)

    def test_add_invalid_position_to_currently_occupied_positions_returns_false(self):
        plateau = Plateau(5, 5)
        self.assertFalse(plateau.currently_occupied_positions.append(3, 6))

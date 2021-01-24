import unittest

from mars_rover_mission.plateau import Plateau


class TestPlateau(unittest.TestCase):

    def test_plateau_exists(self):
        plateau = Plateau()
        self.assertIsInstance(plateau, Plateau, "Mission class is missing or initiated incorrectly")

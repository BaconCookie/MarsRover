import unittest

from mars_rover_mission.mars_rover import MarsRover


class TestMarsRover(unittest.TestCase):

    def setUp(self):
        self.mars_rover = MarsRover()

    def test_mars_rover_exists(self):
        self.assertIsInstance(self.mars_rover, MarsRover, "MarsRover class is missing or initiated incorrectly")

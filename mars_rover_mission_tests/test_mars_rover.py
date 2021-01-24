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

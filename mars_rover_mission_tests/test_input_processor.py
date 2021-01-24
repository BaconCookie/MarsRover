import unittest

from mars_rover_mission.input_processor import InputProcessor


class TestInputProcessor(unittest.TestCase):

    def setUp(self):
        self.input_processor = InputProcessor()

    def tearDown(self):
        self.input_processor = None

    def test_mars_rover_exists(self):
        self.assertIsInstance(self.input_processor, InputProcessor,
                              "InputProcessor class is missing or initiated incorrectly")

    def test_init_plateau_with_positive_integers(self):
        pass

    def test_cannot_init_plateau_with_neg_integer_x(self):
        pass

    def test_cannot_init_plateau_with_neg_integer_y(self):
        pass

    def test_cannot_init_plateau_with_neg_integers_x_and_y(self):
        pass

    def test_cannot_init_plateau_with_floats_x(self):
        pass

    def test_cannot_init_plateau_with_floats_y(self):
        pass

    def test_cannot_init_plateau_with_floats_x_and_y(self):
        pass

    def test_validate_and_get_startposition(self):
        pass

    # def test_startposition_is_valid(self):
    #     pass

    def test_heading_is_valid(self):
        valid_heading = 'N'
        self.assertTrue()

    def test_invalid_heading_returns_false(self):
        invalid_heading = 'X'
        # self.assertFalse()

    def test_startposition_invalid_already_occupied(self):
        pass

    def test_startposition_invalid_x_too_large_not_on_plateau(self):
        pass

    def test_startposition_invalid_y_too_large_not_on_plateau(self):
        pass

    def test_startposition_invalid_x_and_y_too_large_not_on_plateau(self):
        pass

    def test_startposition_invalid_x_neg_not_on_plateau(self):
        pass

    def test_startposition_invalid_y_neg_not_on_plateau(self):
        pass

    def test_startposition_invalid_x_and_y_neg_not_on_plateau(self):
        pass

    def test_valid_instructions(self):
        valid_instructions1 = ''
        valid_instructions2 = 'L'
        valid_instructions3 = 'R'
        valid_instructions4 = 'M'
        valid_instructions5 = 'LRM'
        valid_instructions6 = 'LMRRMLLLMMMRR'

    def test_invalid_instructions_raise_value_error(self):
        invalid_instructions1 = 'X'
        invalid_instructions2 = 'LMXR'
        invalid_instructions3 = 'LM R'
        invalid_instructions4 = ' '
        invalid_instructions5 = 'lmr'
        invalid_instructions6 = 1
        invalid_instructions7 = '1'
        invalid_instructions8 = 'None'
        invalid_instructions9 = None


if __name__ == '__main__':
    unittest.main()

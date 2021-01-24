import unittest

from mars_rover_mission.input_processor import InputProcessor
from mars_rover_mission.plateau import Plateau


class TestInputProcessor(unittest.TestCase):

    def setUp(self):
        self.input_processor = InputProcessor()

    def tearDown(self):
        self.input_processor = None

    def test_input_processor_exists(self):
        self.assertIsInstance(self.input_processor, InputProcessor,
                              "InputProcessor class is missing or initiated incorrectly")

    def test_init_plateau_with_positive_integers(self):
        expected_plateau = Plateau(5, 5)
        actual_plateau = self.input_processor.init_plateau('5 5')
        self.assertEqual(expected_plateau, actual_plateau)

    def test_cannot_init_plateau_with_neg_integer_x(self):
        with self.assertRaises(ValueError):
            self.input_processor.init_plateau('-5 5')

    def test_cannot_init_plateau_with_neg_integer_y(self):
        with self.assertRaises(ValueError):
            self.input_processor.init_plateau('5 -5')

    def test_cannot_init_plateau_with_neg_integers_x_and_y(self):
        with self.assertRaises(ValueError):
            self.input_processor.init_plateau('-5 -5')

    def test_cannot_init_plateau_with_floats_x(self):
        with self.assertRaises(ValueError):
            self.input_processor.init_plateau('1.5 5')

    def test_cannot_init_plateau_with_floats_y(self):
        with self.assertRaises(ValueError):
            self.input_processor.init_plateau('5 1.5')

    def test_cannot_init_plateau_with_floats_x_and_y(self):
        with self.assertRaises(ValueError):
            self.input_processor.init_plateau('1.5 5.3')

    def test_cannot_init_plateau_with_incorrect_format_too_few(self):
        # correct format is a string of two integers separated by a space
        with self.assertRaises(ValueError):
            self.input_processor.init_plateau('5')

    def test_cannot_init_plateau_with_incorrect_format_too_many(self):
        # correct format is a string of two integers separated by a space
        with self.assertRaises(ValueError):
            self.input_processor.init_plateau('5 5 5')

    def test_get_startposition(self):
        expected_x = 1
        expected_y = 2
        expected_heading = 'N'
        actual_x, actual_y, actual_heading = self.input_processor.get_startposition('1 2 N')
        print(type(expected_x))
        print(type(actual_x))
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)
        self.assertEqual(expected_heading, actual_heading)


    def test_heading_is_valid(self):
        valid_heading = 'N'
        self.assertTrue(self.input_processor.is_valid_heading(valid_heading))

    def test_invalid_heading_returns_false(self):
        invalid_heading = 'X'
        self.assertFalse(self.input_processor.is_valid_heading(invalid_heading))

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

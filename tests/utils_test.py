import unittest
import utils

DATA = 'data/day01/testdata'

# no file should return error
# correct file should return list of strings

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.result = utils.load_data(DATA)

    def test_given_correct_file_should_return_list(self):
        self.assertIsInstance(self.result, list)

    def test_given_correct_file_should_return_integers(self):
        self.assertIsInstance(self.result[0], int)

    def test_given_correct_file_should_return_list_of_certain_length(self):
        self.assertEqual(len(self.result), 10)

if __name__ == '__main__':
    unittest.main()

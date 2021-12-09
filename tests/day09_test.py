import unittest
import utils

DATA = 'data/day09/testdata'

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.result = utils.load_data(DATA)

if __name__ == '__main__':
    unittest.main()

import unittest

# Event check in and attendance system

#TODO
# Python's testing library
# CI/CD integration through Github Actions
# Database or Data file??
# The app itself (Console) <- PyGame if there is time

class TestMain(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 2, 3, "Test Addition True")

    def test_subtraction(self):
        self.assertNotEqual(1 - 2, 3, "Test Subtraction False")

if __name__ == '__main__':
    unittest.main()


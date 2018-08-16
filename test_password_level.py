"""
test_password_level class defines four unit tests
to test the functions defined in password_generator.py
"""

# dependencies
import password_generator
import unittest


class test_password_level(unittest.TestCase):

    """
    test_should_verify_password_level_one - asserts that a randomly generated password with complexity of 1
    matches the complexity level returned from the check_password_level
    """

    def test_should_verify_password_level_one(self):
        try:
            self.assertEqual(
                password_generator.check_password_level(
                    password_generator.generate_password(
                        5, 1)), 1)
            print("Level 1-PASS")
        except BaseException:
            print("Level 1-FAIL")

    """
    test_should_verify_password_level_two - asserts that a randomly generated password with complexity of 2
    matches the complexity level returned from the check_password_level
    """

    def test_should_verify_password_level_two(self):
        try:
            self.assertEqual(
                password_generator.check_password_level(
                    password_generator.generate_password(
                        7, 2)), 2)
            print("Level 2-PASS")
        except BaseException:
            print("Level 2-FAIL")

    """
    test_should_verify_password_level_three - asserts that a randomly generated password with complexity of 3
    matches the complexity level returned from the check_password_level
    """

    def test_should_verify_password_level_three(self):
        try:
            self.assertEqual(
                password_generator.check_password_level(
                    password_generator.generate_password(
                        9, 3)), 3)
            print("Level 3-PASS")
        except BaseException:
            print("Level 3-FAIL")

    """
    test_should_verify_password_level_four - asserts that a randomly generated password with complexity of 4
    matches the complexity level returned from the check_password_level
    """

    def test_should_verify_password_level_four(self):
        try:
            self.assertEqual(
                password_generator.check_password_level(
                    password_generator.generate_password(
                        13, 4)), 4)
            print("Level 4-PASS")
        except BaseException:
            print("Level 4-FAIL")


# main() runs the 4 unit tests defined above and prints the results to the
# console


if __name__ == '__main__':
    unittest.main()

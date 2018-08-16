'''
password_generator.py script defines two functions required as per the README.md
'''

# dependencies
import random
import re
import string


'''
generate_password function is responsible for randomly generating a password
when given size and complexity.

Args:
size - The number of characters for password
complexity - level of password from 1 to 4 where
1 == password with lower case letters
2 == previous level plus at least 1 digit
3 == previous level plus at least 1 uppercase character
4 == previous level plust at least 1 punctuation character

Returns: generated password
'''


def generate_password(size: int, complexity: int) -> str:

    if complexity == 1:
        return ''.join(random.choice(string.ascii_lowercase)
                       for c in range(size))

    if complexity == 2:
        one_number = ''.join(random.choice(string.digits) for c in range(1))
        complexity_two = ''.join(
            random.choice(
                string.ascii_lowercase +
                string.digits) for c in range(
                size -
                1))
        return one_number + complexity_two

    if complexity == 3:
        one_uppercase_letter = ''.join(random.choice(
            string.ascii_uppercase) for c in range(1))
        complexity_three = ''.join(
            random.choice(
                string.ascii_lowercase +
                string.digits +
                string.ascii_uppercase) for c in range(
                size -
                1))
        return one_uppercase_letter + complexity_three

    if complexity == 4:
        one_punctuation_character = ''.join(
            random.choice(string.punctuation) for c in range(1))
        complexity_four = ''.join(
            random.choice(
                string.ascii_lowercase +
                string.digits +
                string.ascii_uppercase +
                string.punctuation) for c in range(
                size -
                1))
        return one_punctuation_character + complexity_four


'''
check_password_level function is responsible for returning the complexity level of a given password

Args:
password - A string of characters

Complexity levels:
    Return complexity 1: If password has only lowercase chars
    Return complexity 2: Previous level condition and at least 1 digit
    Return complexity 3: Previous levels condition and at least 1 uppercase char
    Return complexity 4: Previous levels condition and at least 1 punctuation

Complexity level overrides:
    Return complexity 2: password has length >= 8 chars and only lowercase chars
    Return complexity 3: password has length >= 8 chars and only lowercase and digits

Returns: complexity level
'''


def check_password_level(password: str) -> int:
    password_level = 0

    if re.search('[a-z]', password) is not None:
        password_level = 1

    if re.search('\d', password) is not None:
        password_level = 2

    if re.search('[A-Z]', password) is not None:
        password_level = 3

    if re.search('\W', password) is not None:
        password_level = 4

    if len(password) >= 8 and password_level == 1:
        password_level = 2

    if len(password) >= 8 and password_level == 2:
        password_level = 3

    return password_level


import unittest
import os
from app import FacebookPoster
from unittest import mock


class TestFacebookPoster(unittest.TestCase):

    def setUp(self) -> None:
        self.args = {
            "login": "random2022@hsswork.p",
            "password": "Ewelina2022",
            "groups": ["https://www.facebook.com/groups/1281302162058634/"],
            "image_path": r"C:\Users\kacpe\OneDrive\Pulpit\Python\Projekty\facebook-group-poster\images\11.jpg",
        }

        self.my_class = FacebookPoster(**self.args)

    def tearDown(self) -> None:
        pass

    def test1_init(self):
        self.assertEqual(self.my_class.login, self.args["login"])
        self.assertEqual(self.my_class.password, self.args["password"])
        self.assertEqual(self.my_class.groups, self.args["groups"])
        self.assertEqual(self.my_class.image_path, self.args["image_path"])

    def test2_get_text(self):
        test_file = "test.txt"
        test_content = "test content"

        # Write test content to test file
        with open(test_file, "w+", encoding="utf-8") as file:
            file.write(test_content)

        # Test if the function returns the correct content
        assert self.my_class.get_txt(test_file) == test_content

        os.remove(test_file)

    def test3_move_cursor_raises_error_on_invalid_direction(self):
        content = "This is a test content."
        selenium_element = mock.Mock()
        position = None
        to_move = None
        self.assertRaises(
            ValueError,
            self.my_class.move_cursor,
            content,
            selenium_element,
            "invalid",
            position,
            to_move,
        )

    def test4_move_cursor_with_invalid_position(self):
        content = "This is a test content."
        selenium_element = mock.Mock()
        position = "not_an_int"
        to_move = None
        self.assertRaises(
            ValueError,
            self.my_class.move_cursor,
            content,
            selenium_element,
            "position",
            position,
            to_move,
        )

    def test5_move_cursor_direction_start_and_correct_it(self):
        content = "Można też dodać testy dla różnych wartości parametrów wejściowych, np. dla różnych wartości direction, position lub to_move, oraz dodać testy dla przypadków błędów, np. gdy podany jest nieprawidłowy argument direction lub position nie jest liczbą całkowitą."
        direction = "start"
        position = None
        to_move = None
        selenium_element = self.my_class.create_selenium_object_for_testing(content, direction)
        expected_result = 4

        result = self.my_class.move_cursor(
            content, selenium_element, direction, position, to_move
        )

        self.assertEqual(result, expected_result)

    def test6_move_cursor_direction_start_without_correct(self):
        content = "Można też dodać testy dla różnych wartości"
        direction = "start"
        position = None
        to_move = None
        selenium_element = self.my_class.create_selenium_object_for_testing(content, direction)
        expected_result = 0

        result = self.my_class.move_cursor(
            content, selenium_element, direction, position, to_move
        )

        self.assertEqual(result, expected_result)

    def test7_move_cursor_direction_end_and_correct_it(self):
        content = "Można też dodać testy dla różnych wartości parametrów wejściowych, np. dla różnych wartości direction, position lub to_move, oraz dodać testy dla przypadków błędów, np. gdy podany jest nieprawidłowy argument direction lub position nie jest liczbą całkowitą."
        direction = "end"
        position = None
        to_move = None
        selenium_element = self.my_class.create_selenium_object_for_testing(content, direction)
        expected_result = 4

        result = self.my_class.move_cursor(
            content, selenium_element, direction, position, to_move
        )

        self.assertEqual(result, expected_result)

    def test8_move_cursor_direction_end_without_correct(self):
        content = "Można też dodać testy dla różnych wartości"
        direction = "end"
        position = None
        to_move = None
        selenium_element = self.my_class.create_selenium_object_for_testing(content, direction)
        expected_result = 0

        result = self.my_class.move_cursor(
            content, selenium_element, direction, position, to_move
        )

        self.assertEqual(result, expected_result)

    def test9_move_cursor_direction_position_and_correct_it(self):
        content = "Można też dodać testy dla różnych wartości parametrów wejściowych, np. dla różnych wartości direction, position lub to_move, oraz dodać testy dla przypadków błędów, np. gdy podany jest nieprawidłowy argument direction lub position nie jest liczbą całkowitą."
        direction = "position"
        position = 149
        to_move = None
        selenium_element = self.my_class.create_selenium_object_for_testing(content, direction)
        expected_result = 2

        result = self.my_class.move_cursor(
            content, selenium_element, direction, position, to_move
        )

        self.assertEqual(result, expected_result)

    def test10_move_cursor_direction_position_without_correct(self):
        content = "Można też dodać testy dla różnych wartości parametrów wejściowych, np. dla różnych wartości direction, position lub to_move, oraz dodać testy dla przypadków błędów, np. gdy podany jest nieprawidłowy argument direction lub position nie jest liczbą całkowitą."
        direction = "position"
        position = 10
        to_move = None
        selenium_element = self.my_class.create_selenium_object_for_testing(content, direction)
        expected_result = 0

        result = self.my_class.move_cursor(
            content, selenium_element, direction, position, to_move
        )

        self.assertEqual(result, expected_result)


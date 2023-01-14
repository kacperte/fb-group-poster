import unittest
import os
from app import FacebookPoster
from unittest import mock


class TestFacebookPoster(unittest.TestCase):
    def setUp(self) -> None:
        print(f"Start testing: {__name__}")
        self.args = {
            "login": "random2022@hsswork.p",
            "password": "Ewelina2022",
            "groups": ["https://www.facebook.com/groups/1281302162058634/"],
            "image_path": r"C:\Users\kacpe\OneDrive\Pulpit\Python\Projekty\facebook-group-poster\images\11.jpg",
        }

        self.my_class = FacebookPoster(**self.args)

    def test_init(self):
        self.assertEqual(self.my_class.login, self.args["login"])
        self.assertEqual(self.my_class.password, self.args["password"])
        self.assertEqual(self.my_class.groups, self.args["groups"])
        self.assertEqual(self.my_class.image_path, self.args["image_path"])

    def test_get_text(self):
        test_file = "test.txt"
        test_content = "test content"

        # Write test content to test file
        with open(test_file, "w", encoding="utf-8") as file:
            file.write(test_content)

        # Test if the function returns the correct content
        assert self.my_class.get_txt(test_file) == test_content

        os.remove(test_file)

    def test_move_cursor_raises_error_on_invalid_direction(self):
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

    def test_move_cursor_with_invalid_position(self):
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

    # def test_move_cursor_direction_start(self):
    #     content = """It is important to have a proper test content to check if the function is working correctly
    #     <b>and is giving expected results.</b> """
    #     selenium_element = mock.Mock()
    #     direction = "start"
    #     position = None
    #     to_move = None
    #     expected_result = 1
    #
    #     result = self.my_class.move_cursor(content, selenium_element, direction, position, to_move)
    #
    #     self.assertEqual(result, expected_result)
    #
    # def test_move_cursor_direction_end(self):
    #     content = """It is important to have a proper test content to check if the function is working correctly
    #     <b>and is giving expected results.</b> """
    #     selenium_element = mock.Mock()
    #     direction = "end"
    #     position = None
    #     to_move = None
    #     expected_result = 1
    #
    #     result = self.my_class.move_cursor(content, selenium_element, direction, position, to_move)
    #
    #     self.assertEqual(result, expected_result)

    def tearDown(self) -> None:
        print(f"End testing: {__name__}")

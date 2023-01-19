import unittest
import os
from app import FacebookPoster
from unittest import mock
from selenium.webdriver.common.by import By
import requests


class TestFacebookPoster(unittest.TestCase):
    def setUp(self) -> None:
        self.args = {
            "login": "random2022@hsswork.pl",
            "password": "Ewelina2022",
            "groups": ["https://www.facebook.com/groups/1281302162058634/"],
            "image_path": r"C:\Users\kacpe\OneDrive\Pulpit\Python\Projekty\facebook-group-poster\images\11.jpg",
        }

        self.my_class = FacebookPoster(**self.args)

    def tearDown(self) -> None:
        pass

    # def test_init_class_FacebookPoster(self):
    #     """Test if the class is initialized correctly with correct input arguments"""
    #     self.assertEqual(self.my_class.login, self.args["login"])
    #     self.assertEqual(self.my_class.password, self.args["password"])
    #     self.assertEqual(self.my_class.groups, self.args["groups"])
    #     self.assertEqual(self.my_class.image_path, self.args["image_path"])
    #
    # def test_get_text_from_file(self):
    #     """Test if the function returns the correct content from the text file"""
    #     test_file = "test.txt"
    #     test_content = "test content"
    #
    #     # Write test content to test file
    #     with open(test_file, "w+", encoding="utf-8") as file:
    #         file.write(test_content)
    #
    #     # Test if the function returns the correct content
    #     assert self.my_class.get_txt(test_file) == test_content
    #
    #     os.remove(test_file)
    #
    # def test_move_cursor_raises_error_on_invalid_direction_argument(self):
    #     """Test if the function raises ValueError when an invalid direction argument is passed"""
    #     content = "This is a test content."
    #     selenium_element = mock.Mock()
    #     position = None
    #     to_move = None
    #     self.assertRaises(
    #         ValueError,
    #         self.my_class.move_cursor,
    #         content,
    #         selenium_element,
    #         "invalid",
    #         position,
    #         to_move,
    #     )
    #
    # def test_move_cursor_raises_error_on_invalid_position_argument(self):
    #     """Test if the function raises ValueError when position argument is not an integer"""
    #     content = "This is a test content."
    #     selenium_element = mock.Mock()
    #     position = "not_an_int"
    #     to_move = None
    #     self.assertRaises(
    #         ValueError,
    #         self.my_class.move_cursor,
    #         content,
    #         selenium_element,
    #         "position",
    #         position,
    #         to_move,
    #     )
    #
    # def test_move_cursor_raises_error_on_invalid_n_for_end_and_position_argument(self):
    #     """Test if the function raises ValueError when n_for_end_and_position argument is not an integer"""
    #     content = "This is a test content."
    #     selenium_element = mock.Mock()
    #     position = None
    #     to_move = None
    #     self.assertRaises(
    #         ValueError,
    #         self.my_class.move_cursor,
    #         content,
    #         selenium_element,
    #         "position",
    #         position,
    #         to_move,
    #         n_for_end_and_position="test",
    #     )
    #
    # def test_move_cursor_with_direction_start_and_correct_it(self):
    #     """Test if the cursor is moved to the correct position when direction is set to 'start'"""
    #     content = "Można też dodać testy dla różnych wartości parametrów wejściowych, np. dla różnych wartości direction, position lub to_move, oraz dodać testy dla przypadków błędów, np. gdy podany jest nieprawidłowy argument direction lub position nie jest liczbą całkowitą."
    #     direction = "start"
    #     position = None
    #     to_move = None
    #     selenium_element, n = self.my_class.create_selenium_object_for_testing(
    #         content, direction
    #     )
    #     expected_result = 4
    #
    #     result = self.my_class.move_cursor(
    #         content, selenium_element, direction, position, to_move
    #     )
    #
    #     self.assertEqual(result, expected_result)
    #
    # def test_move_cursor_with_direction_start_without_correct(self):
    #     """Test if the cursor is moved to the start position when direction is set to 'start'"""
    #     content = "Można też dodać testy dla różnych wartości"
    #     direction = "start"
    #     position = None
    #     to_move = None
    #     selenium_element, n = self.my_class.create_selenium_object_for_testing(
    #         content, direction
    #     )
    #     expected_result = 0
    #
    #     result = self.my_class.move_cursor(
    #         content, selenium_element, direction, position, to_move
    #     )
    #
    #     self.assertEqual(result, expected_result)
    #
    # def test_move_cursor_with_direction_start_and_return_wrong_value(self):
    #     """Test if the cursor is moved to the start position when direction is set to 'start'"""
    #     content = "Można też dodać testy dla różnych wartości"
    #     direction = "start"
    #     position = None
    #     to_move = None
    #     selenium_element, n = self.my_class.create_selenium_object_for_testing(
    #         content, direction
    #     )
    #     expected_result = 2
    #
    #     result = self.my_class.move_cursor(
    #         content, selenium_element, direction, position, to_move
    #     )
    #
    #     self.assertNotEquals(result, expected_result)
    #
    # def test_move_cursor_with_direction_end_and_correct_it(self):
    #     """Test if the cursor is moved to the end position when direction is set to 'end' and the value is correct"""
    #     content = "Można też dodać testy dla różnych wartości parametrów wejściowych, np. dla różnych wartości direction, position lub to_move, oraz dodać testy dla przypadków błędów, np. gdy podany jest nieprawidłowy argument direction lub position nie jest liczbą całkowitą."
    #     direction = "end"
    #     position = None
    #     to_move = None
    #     selenium_element, n = self.my_class.create_selenium_object_for_testing(
    #         content, direction
    #     )
    #     expected_result = 4
    #
    #     result = self.my_class.move_cursor(
    #         content,
    #         selenium_element,
    #         direction,
    #         position,
    #         to_move,
    #         n_for_end_and_position=n,
    #     )
    #
    #     self.assertEqual(result, expected_result)
    #
    # def test_move_cursor_with_direction_end_without_correct(self):
    #     """Test if the cursor is moved to the end position when direction is set to 'end' and the value is not correct"""
    #     content = "Można też dodać testy dla różnych wartości"
    #     direction = "end"
    #     position = None
    #     to_move = None
    #     selenium_element, n = self.my_class.create_selenium_object_for_testing(
    #         content, direction
    #     )
    #     expected_result = 0
    #
    #     result = self.my_class.move_cursor(
    #         content,
    #         selenium_element,
    #         direction,
    #         position,
    #         to_move,
    #         n_for_end_and_position=n,
    #     )
    #
    #     self.assertEqual(result, expected_result)
    #
    # def test_move_cursor_with_direction_end_return_wrong_value(self):
    #     """Test if the cursor is moved to the end position when direction is set to 'end' and the value is not correct"""
    #     content = "Można też dodać testy dla różnych wartości"
    #     direction = "end"
    #     position = None
    #     to_move = None
    #     selenium_element, n = self.my_class.create_selenium_object_for_testing(
    #         content, direction
    #     )
    #     expected_result = 2
    #
    #     result = self.my_class.move_cursor(
    #         content,
    #         selenium_element,
    #         direction,
    #         position,
    #         to_move,
    #         n_for_end_and_position=n,
    #     )
    #
    #     self.assertNotEquals(result, expected_result)
    #
    # def test_move_cursor_with_direction_position_and_correct_it(self):
    #     """Test if the cursor is moved to the correct position when direction is set to 'position' and the value is correct"""
    #     content = "Można też dodać testy dla różnych wartości parametrów wejściowych, np. dla różnych wartości direction, position lub to_move, oraz dodać testy dla przypadków błędów, np. gdy podany jest nieprawidłowy argument direction lub position nie jest liczbą całkowitą."
    #     direction = "position"
    #     position = 80
    #     to_move = None
    #     selenium_element, n = self.my_class.create_selenium_object_for_testing(
    #         content, direction
    #     )
    #     expected_result = 1
    #
    #     result = self.my_class.move_cursor(
    #         content,
    #         selenium_element,
    #         direction,
    #         position,
    #         to_move,
    #         n_for_end_and_position=n,
    #     )
    #
    #     self.assertEqual(result, expected_result)
    #
    # def test_move_cursor_with_direction_position_without_correct(self):
    #     """Test if the cursor is moved to the correct position when direction is set to 'position' and the value is not correct"""
    #     content = "Można też dodać testy dla różnych wartości parametrów wejściowych, np. dla różnych wartości direction, position lub to_move, oraz dodać testy dla przypadków błędów, np. gdy podany jest nieprawidłowy argument direction lub position nie jest liczbą całkowitą."
    #     direction = "position"
    #     position = 10
    #     to_move = None
    #     selenium_element, n = self.my_class.create_selenium_object_for_testing(
    #         content, direction
    #     )
    #     expected_result = 0
    #
    #     result = self.my_class.move_cursor(
    #         content,
    #         selenium_element,
    #         direction,
    #         position,
    #         to_move,
    #         n_for_end_and_position=n,
    #     )
    #
    #     self.assertEqual(result, expected_result)
    #
    # def test_move_cursor_with_direction_position_return_wrong_value(self):
    #     """Test if the cursor is moved to the correct position when direction is set to 'position' and the value is not correct"""
    #     content = "Można też dodać testy dla różnych wartości parametrów wejściowych, np. dla różnych wartości direction, position lub to_move, oraz dodać testy dla przypadków błędów, np. gdy podany jest nieprawidłowy argument direction lub position nie jest liczbą całkowitą."
    #     direction = "position"
    #     position = 10
    #     to_move = None
    #     selenium_element, n = self.my_class.create_selenium_object_for_testing(
    #         content, direction
    #     )
    #     expected_result = 2
    #
    #     result = self.my_class.move_cursor(
    #         content,
    #         selenium_element,
    #         direction,
    #         position,
    #         to_move,
    #         n_for_end_and_position=n,
    #     )
    #
    #     self.assertNotEquals(result, expected_result)x1

    def test_login_to_facbook(self):
        self.my_class._login_to_facebook(human_simulation=False)
        self.assertTrue(self.my_class.driver.find_element(By.ID, "facebook"))

    def test_login_with_invalid_credentials(self):
        self.login = 'test@test.com'
        self.password = 'wrongpassword'

        self.my_class._login_to_facebook(human_simulation=False)

        self.assertTrue(self.my_class.driver.find_element(By.ID, ("error_box")))

    def test_login_without_internet_connection(self):
        self.base_url = 'https://www.facebook.com'
        self.login = 'test@test.com'
        self.password = 'testpassword'

        # Disabling internet connection
        with mock.patch('urllib3.PoolManager.request') as mocked:
            mocked.side_effect = requests.exceptions.ConnectionError()

            self.my_class._login_to_facebook(human_simulation=False)

        self.assertTrue(self.my_class.driver.find_element(By.ID, "error_box"))


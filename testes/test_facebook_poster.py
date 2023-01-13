import unittest
import os
from app import FacebookPoster


class TestFacebookPoster(unittest.TestCase):
    def setUp(self) -> None:
        self.args = {
            "login": "random2022@hsswork.p",
            "password": "Ewelina2022",
            "groups": ["https://www.facebook.com/groups/1281302162058634/"],
            "image_path": r"C:\Users\kacpe\OneDrive\Pulpit\Python\Projekty\facebook-group-poster\images\11.jpg",
        }
        self.my_class = FacebookPoster(**self.args)

    def test_get_text(self):
        test_file = "test.txt"
        test_content = "test content"

        # Write test content to test file
        with open(test_file, "w", encoding="utf-8") as file:
            file.write(test_content)

        # Test if the function returns the correct content
        assert self.my_class.get_txt(test_file) == test_content

        os.remove(test_file)

    def tearDown(self) -> None:
        pass



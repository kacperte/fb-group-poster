from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import re
import win32clipboard

# login BETA
LOGIN_BETA = "random2022@hsswork.pl"
PASSWORD_BETA = "Ewelina2022"


class FacebookPoster:
    """
    A class representing a bot for posting in groups on Facebook.
    """

    def __init__(self, login, password):
        """
        Initializes the attributes of the class.
        :param login: str Facebook login id credentials
        :param password: str Facebook login password credentials
        """

        # Facebook login id credentials
        self.login = login

        # Facebook login password credentials
        self.password = password

        # Facebook page url
        self.base_url = "https://www.facebook.com/"

        # Setup Selenium Options
        options = Options()

        # Add binary location for Firefox which is mandatory and headless mode on
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

        # options.add_argument("--headless")
        # options.add_argument("--headless")

        # Setup Firefox driver
        self.driver = Firefox(
            service=Service(GeckoDriverManager().install()), options=options
        )

        # Setup Selenium action chain
        self.action = ActionChains(self.driver)

        # By default, is set to 5,
        # will be used by time patterns
        self.time_pattern = 5  # seconds

        # Dict with text format action
        self.text_formatting_action = {
            0: "b",  # bold text
            1: "i",  # italics text
            2: "h1",  # h1 format
            3: "h2",  # h2 format
            4: "quote",  # quote text
            5: "ul",  # unordered list
            6: "ol",  # ordered list
        }

        # Run function to log into Facebook account
        self._login_to_facebook()

    @staticmethod
    def get_txt(filename):
        """
        Return content of a text file.
        :param filename: File path
        :return: str
        """
        # Open file in read mode with ut-8 encode
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
        return content

    def move_cursor_to_start(self, content: str, selenium_element):
        """
        Move cursor to the start of the line if it is in the wrong position.
        :param content: File path
        :param selenium_element: Location to web element we point with selenium
        :return: int
        """

        # Select three characters
        self.action.key_down(Keys.SHIFT).send_keys(Keys.RIGHT * 3).perform()
        self.action.reset_actions()

        # Copy selected characters
        self.action.key_down(Keys.CONTROL).key_down("c").perform()
        self.action.reset_actions()

        # Unselect selected characters
        selenium_element.send_keys(Keys.LEFT)

        # Get copied characters from clipboard
        win32clipboard.OpenClipboard()
        copied_text = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()

        # Calculate number of characters to move
        n_to_move = content.find(copied_text)

        # Move cursor to the start of the line
        for _ in range(n_to_move):
            selenium_element.send_keys(Keys.LEFT)
            self._time_patterns(2)

        return n_to_move

    def move_cursor_to_end(self, content: str, selenium_element):
        """
        Move cursor to the end of the line if it is in the wrong position.
        :param content: File path
        :param selenium_element: Location to web element we point with selenium
        :return: int
        """
        # Select three characters
        self.action.key_down(Keys.SHIFT).send_keys(Keys.LEFT * 3).perform()
        self.action.reset_actions()

        # Copy selected characters
        self.action.key_down(Keys.CONTROL).key_down("c").perform()
        self.action.reset_actions()

        # Unselect selected characters
        selenium_element.send_keys(Keys.RIGHT)

        # Get copied characters from clipboard
        win32clipboard.OpenClipboard()
        copied_text = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()

        # Calculate number of characters to move
        n_to_move = len(content) - content.find(copied_text)

        # Move cursor to the end of the line
        for _ in range(n_to_move):
            selenium_element.send_keys(Keys.RIGHT)
            self._time_patterns(2)

        return n_to_move

    def _login_to_facebook(self):
        """
        Log into Facebook.
        :return:
        """
        # Open Facebook at login page
        self.driver.get(self.base_url)

        # Close cookie popup
        self.driver.find_element(
            By.XPATH,
            "//button[text()='Zezwól na korzystanie z niezbędnych i opcjonalnych plików cookie']",
        ).click()

        # For pausing the script for some time
        self._time_patterns(3)

        # Enter login and password
        self.driver.find_element(By.ID, "email").send_keys(self.login)
        self.driver.find_element(By.ID, "pass").send_keys(self.password)

        # For pausing the script for some time
        self._time_patterns(3)

        # Click login button
        self.driver.find_element(By.XPATH, "//button[text()='Zaloguj się']").click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "facebook"))
        )

    def _time_patterns(self, tp=None):
        """
        Pause script for some time.
        :param tp: Time pattern in seconds
        :return:
        """

        # Check if time pattern is set as default
        if tp is None:
            time.sleep(self.time_pattern)

        # If not set time pattern as argument passed in function
        else:
            self.time_pattern = tp
            time.sleep(self.time_pattern)

    def bold_and_italic_formatting(
            self,
            content: str,
            content_without_tags: str,
            selenium_element,
            text_modify_butttons,
    ):
        """
        This function performs bolding and italicizing of text by determining the start and end index of the formatted
        text and assigning a method to it (0 for bold, 1 for italic).

        :param content: a line of text with text formatting tags (e.g. <b>)
        :param content_without_tags: a line of text without text formatting tags
        :param selenium_element: a web element that we point to with selenium
        :param text_modify_butttons: a web element with text modifier buttons
        :return: a tuple of two boolean values, which is necessary to switch off a Facebook glitch
        """
        # Split text into text content and text formatting tags
        splited_content = [x for x in re.split(r"<(.+?)>", content) if x != ""]

        # Init var steps as empty list
        steps = list()

        # Init var temp_clean_text as content_without_tags
        temp_clean_text = content_without_tags

        # Init var num as 0 - it will be simulated the current text index
        num = 0

        # Iterate through splited_content to find the start and end indexes of text formatting tags
        tags = ["b", "i", "/i", "/b"]  # tags to look for
        for elem in splited_content:
            # If we encounter a bold or italic tag, create a list containing the start/end index and the text formatting
            # tag and add it to the steps list
            if elem in tags:
                steps.append([num, elem])

            # If the element is not a text formatting tag, check how many characters it has and add it to
            # the num variable.
            # Ignore empty strings that may be created by the regex split.
            elif elem in temp_clean_text and elem != " ":
                num_to_add = temp_clean_text.index(elem) + len(elem)
                num = num_to_add

        for tag in steps:  # remove / character from list
            tag[1] = tag[1].replace("/", "")

        # Every element in the steps list is a tuple with two elements, such as (1, b) or (5, b).
        # The second element of the tuple represents a text formatting method, which has an equivalent integer value.
        # This information is stored in the self.text_formatting_action dictionary.
        # The code below swaps the text formatting method with its equivalent integer value.on
        mapping = {val: num for num, val in self.text_formatting_action.items()}
        for action in steps:
            if action[1] in mapping:
                action[1] = mapping[action[1]]

        # Initialize an empty list to store the text formatting actions to be executed
        action_to_execute = list()

        # In this step, we join the start and end indexes of actions for a single text formatting tag. One of the
        # final elements in the action_to_execute list should look like this (1, 10, 0) (start_index, end_index,
        # method)
        while steps:
            # Set the first element in the steps list as the current action
            action = steps[0]

            # Set the start index as the first element of the action tuple (the first element is the start index)
            start = action[0]

            # Set the text formatter as the second element of the action tuple (the second element is the text
            # formatting tag)
            text_formatter = action[1]

            # Iterate through the remaining elements in the steps list to find the next action with the same text
            # formatting tag
            for equal_action in steps[1:]:
                if equal_action[1] == text_formatter:
                    # Set the end index as the first element of the equal_action tuple (the first element is the end
                    # index)
                    end = equal_action[0]

                    # Add the prepared list to the action_to_execute list
                    action_to_execute.append([start, end, text_formatter])

                    # Remove both lists from the steps list and return to the main loop
                    steps.remove(equal_action)
                    steps.remove(action)
                    break

        # # Initialize the is_formatting_on and last_action variables as None
        is_formatting_on = None
        last_action = None

        # Iterate through the actions in the action_to_execute list
        for action in action_to_execute:
            # If the formatting starts at the first character in the line
            if action[0] == 0:
                # Press and hold SHIFT and move the cursor to the right by the number of characters specified in
                # action[1]
                self.action.key_down(Keys.SHIFT).send_keys(
                    Keys.RIGHT * int(action[1])
                ).perform()

                # Click text formatting button (after this, we reset action chain)
                text_modify_butttons[action[2]].click()
                self.action.reset_actions()

                # For pausing the script for some time
                self._time_patterns()

                # Unselect the selected characters
                selenium_element.send_keys(Keys.RIGHT)

                # Move back to the start of the line (after this, we reset action chain)
                self.action.send_keys(Keys.LEFT * int(action[1])).perform()
                self.action.reset_actions()

                # For pausing the script for some time
                self._time_patterns()

                # Check if we back to correct  place - if not correct it
                n_to_move = self.move_cursor_to_start(
                    content=content_without_tags, selenium_element=selenium_element
                )
                selenium_element.send_keys(Keys.LEFT * n_to_move)

                # There is a glitch in the Facebook text box - if our last word has formatting, the formatting will
                # be moved to the next line. So we have to check for this condition and if it's True,
                # save this information to variables which are needed to switch this off
                if action[1] == len(content_without_tags):
                    is_formatting_on = True
                    last_action = action[2]

            else:
                # Press and hold SHIFT and move cursor by n places to left
                self.action.send_keys(Keys.RIGHT * int(action[0])).perform()
                self.action.reset_actions()

                # Click text formatting button (after this, we reset action chain)
                self.action.key_down(Keys.SHIFT).send_keys(
                    Keys.RIGHT * (int(action[1]) - int(action[0]))
                ).perform()

                # Click text formatting button (after this, we reset action chain)
                text_modify_butttons[action[2]].click()
                self.action.reset_actions()

                # For pausing the script for some time
                self._time_patterns()

                # Unselect the selected characters
                selenium_element.send_keys(Keys.RIGHT)

                # Move back to the start of the line (after this, we reset action chain)
                self.action.send_keys(Keys.LEFT * (int(action[1]))).perform()
                self.action.reset_actions()

                # For pausing the script for some time
                self._time_patterns()

                # Check if we back to correct place - if not correct it
                n_to_move = self.move_cursor_to_start(
                    content=content_without_tags, selenium_element=selenium_element
                )
                selenium_element.send_keys(Keys.LEFT * n_to_move)

                # There is a glitch in the Facebook text box - if our last word has formatting, the formatting will
                # be moved to the next line. So we have to check for this condition and if it's True,
                # save this information to variables which are needed to switch this off
                if action[1] == len(content_without_tags):
                    is_formatting_on = True
                    last_action = action[2]

        return is_formatting_on, last_action

    def send_post(self, content: str, selenium_element):
        """
        Sends the given `content` string to the Facebook text box element specified by `selenium_element` and applies
        text formatting according to formatting tags in the `content` string.
        :param content: The string to be sent to the Facebook text box
        :param selenium_element: A Selenium web element object representing the Facebook text box element.
        """
        # Find the text formatting buttons in the Facebook text box
        text_modify_butttons = selenium_element.find_elements(
            By.XPATH, "//span[@class='x12mruv9 xfs2ol5 x1gslohp x12nagc']"
        )

        # Initialize empty lists to store text formatting actions for text without bold and italic formatting,
        # and text with only bold and italic formatting
        list_of_action_to_do_with_text_without_bold_and_italic = list()
        list_of_action_to_do_with_text_only_with_bold_and_italic = list()

        # Find all text formatting tags in the `content` string
        tags = re.findall(r"<(.+?)>", content)

        # If there are any tags in the `content` string
        if tags:
            # Create a dictionary mapping the tag strings to their corresponding values in the
            # `self.text_formatting_action` dictionary
            tag_values = {
                val: num
                for num, val in self.text_formatting_action.items()
                if val in tags
            }

            # Initialize empty lists to store text formatting actions for text without bold and italic formatting,
            # and text with only bold and italic formatting
            list_of_action_to_do_with_text_without_bold_and_italic = [
                num for num in tag_values.values() if num not in (0, 1)
            ]
            list_of_action_to_do_with_text_only_with_bold_and_italic = [
                num for num in tag_values.values() if num in (0, 1)
            ]

        # If there are no text formatting actions to perform
        if (
                not list_of_action_to_do_with_text_without_bold_and_italic
                and not list_of_action_to_do_with_text_only_with_bold_and_italic
        ):
            # Send the `content` to the Facebook text box and create a new line
            selenium_element.send_keys(content)
            selenium_element.send_keys(Keys.ENTER)

        # If there are text formatting actions to perform

        else:
            # Store the content without text formatting tags in `content_without_tags`
            content_without_tags = re.sub("<[^<>]+>", "", content)

            # Init var n where we store lenght of content_without_tags
            n = len(content_without_tags)

            # Send the `content_without_tags` to the Facebook text box
            selenium_element.send_keys(content_without_tags)

            # Press and hold Shift then press left by n times (after this, we reset action chain)
            self.action.key_down(Keys.SHIFT).send_keys(Keys.LEFT * n).perform()
            self.action.reset_actions()

            # For pausing the script for some time
            self._time_patterns()

            # Iterate through actions in `list_of_actions_without_bold_and_italic` and click the corresponding button
            # to trigger the action
            for action in list_of_action_to_do_with_text_without_bold_and_italic:
                text_modify_butttons[action].click()

                # For pausing the script for some time
                self._time_patterns(2)

            # Set cursor at the start of text
            selenium_element.send_keys(Keys.LEFT)

            # Check if the cursor is at the start of the line and move it if necessary
            n_to_move = self.move_cursor_to_start(
                content=content_without_tags, selenium_element=selenium_element
            )

            # Add n_to_move to variable when we store lenght of content to correct proper lenght
            n += n_to_move

            # Apply bold and italic formatting and fix the Facebook glitch if necessary
            is_formatting, last_action = self.bold_and_italic_formatting(
                content=content,
                content_without_tags=content_without_tags,
                selenium_element=selenium_element,
                text_modify_butttons=text_modify_butttons,
            )

            # For pausing the script for some time
            self._time_patterns()

            # Move the cursor to the end of the line
            selenium_element.send_keys(Keys.RIGHT * n)

            # Check if the cursor is at the end of the line and move it if necessary
            self.move_cursor_to_end(content=content, selenium_element=selenium_element)

            # If the last word was bold or italic, turn off the formatting before creating a new line
            if is_formatting:
                self.action.key_down(Keys.CONTROL).send_keys("b" if last_action == 0 else "i").perform()
                self.action.reset_actions()

            # If the text has a list formatting, press Enter twice to turn off the formatting
            if (
                    5 in list_of_action_to_do_with_text_without_bold_and_italic
                    or 6 in list_of_action_to_do_with_text_without_bold_and_italic
            ):
                selenium_element.send_keys(Keys.ENTER)
                selenium_element.send_keys(Keys.ENTER)

            # In any other case, press Enter once
            else:
                selenium_element.send_keys(Keys.ENTER)

        # For pausing the script for some time
        self._time_patterns(2)

    def prepare_and_send_post(self, content_filename):
        fb_groups = ["https://www.facebook.com/groups/1281302162058634/"]
        for group in fb_groups:

            # Open Facebook group url
            self.driver.get(group + "buy_sell_discussion")
            print(f"/// Start processing group: {group + 'buy_sell_discussion'}")

            # For pausing the script for sometime
            self._time_patterns(4)

            # Locate postbox element and click it
            self.driver.find_element(
                By.XPATH,
                "//div[@class='x6s0dn4 x78zum5 x1l90r2v x1pi30zi x1swvt13 xz9dl7a']",
            ).click()

            # For pausing the script for sometime
            self._time_patterns(8)

            # Activate postbox pop up to send value to it
            postbox = self.driver.switch_to.active_element

            # Load content from file
            content = self.get_txt(content_filename)

            for line in content.split("\n"):
                self.send_post(content=line, selenium_element=postbox)


FacebookPoster(LOGIN_BETA, PASSWORD_BETA).prepare_and_send_post(
    content_filename="content/1.txt"
)

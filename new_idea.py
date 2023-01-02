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
        The function performs bolding and italicizing of text. Iterating through the text, it determines the start and
        end index where the text is formatted and assigns a method to it (0 - bold; 1 - italic)
        :param content: Line of text with text formatting tags (i.e. <b>)
        :param content_without_tags: Line of text out text formatting tags
        :param selenium_element: Location to web element we point with selenium
        :param text_modify_butttons: Location to web element with text modifier buttons
        :return: (bool, bool) Return two bool value which is necessary to switch off Facebook glitch
        """
        # Split text into text content and text formatting tags
        splited_content = [x for x in re.split(r"<(.+?)>", content) if x != ""]

        # Init var steps as empty list
        steps = list()

        # Init var temp_clean_text as content_without_tags
        temp_clean_text = content_without_tags

        # Init var num as 0 - it will be simulated the current text index
        num = 0

        # Iterate through splited_content to find out where start and end (index) text formatting tags
        tags = ["b", "i", "/i", "/b"]
        for elem in splited_content:
            # If we encounter bold tag or italic tag, it creates a list which contain two element
            # (position_where_tag_start/end, text formatting tag). Then it's add to steps list
            if elem in tags:
                steps.append([num, elem])

            # If element is not a text formatting tags, check how ow many characters it has and then add to num
            # variable.
            # For some reasons, regex create some empty string after it has split text. So we have to ignore this
            elif elem in temp_clean_text and elem != " ":
                num_to_add = temp_clean_text.index(elem) + len(elem)
                num = num_to_add

        for tag in steps:
            tag[1] = tag[1].replace("/", "")

        # Every element in steps list look like this (1, b) or (5, b). Every text formatting method has equivalent in
        # integer (we set dict wiht that information in self.text_formatting_action). Code below swaps this information
        mapping = {val: num for num, val in self.text_formatting_action.items()}
        for action in steps:
            if action[1] in mapping:
                action[1] = mapping[action[1]]

        # Init var action_to_execute as empty list
        action_to_execute = list()

        # In this step, we join start index and end index action for a single text formatting tag. One of the final
        # element in action_to_execute list should look like this (1, 10, 0) (start_index, end_index, method)
        while steps:
            # Init var action as first element from steps list
            action = steps[0]

            # Init var start as first element from action (1-st element is start index)
            start = action[0]

            # Init var text_formatter as second element from action (2-nd element is text formatting tag)
            text_formatter = action[1]
            # Itarate through rest steps list to find next list with the same text formatting tag
            for equal_action in steps[1:]:
                if equal_action[1] == text_formatter:
                    # Init var end as first element from equal_action (1-st element is start index but in this
                    # case is end)
                    end = equal_action[0]

                    # Add prepare list to action_to_execute list
                    action_to_execute.append([start, end, text_formatter])

                    # Remove both list from steps list and return to main loop
                    steps.remove(equal_action)
                    steps.remove(action)
                    break
        # Init var is_formatting_on and last_action as None
        is_formatting_on = None
        last_action = None

        # Iterate through actions
        for action in action_to_execute:
            # If text fortatting start from first letters
            if action[0] == 0:
                # Press and hold SHIFT and move cursor by n places to left
                self.action.key_down(Keys.SHIFT).send_keys(
                    Keys.RIGHT * int(action[1])
                ).perform()

                # Click text formatting button (after this, we reset action chain)
                text_modify_butttons[action[2]].click()
                self.action.reset_actions()

                # For pausing the script for some time
                self._time_patterns()

                # Unselect selected characters
                selenium_element.send_keys(Keys.RIGHT)

                # Move back to the start of the line (after this, we reset action chain)
                self.action.send_keys(Keys.LEFT * int(action[1])).perform()
                self.action.reset_actions()

                # For pausing the script for some time
                self._time_patterns()

                # Check if we back to proper place - if not correct it
                n_to_move = self.move_cursor_to_start(
                    content=content_without_tags, selenium_element=selenium_element
                )
                selenium_element.send_keys(Keys.LEFT * n_to_move)

                # There is a glitch in Facebook text box - if our last word is formatting, the formatting will be moved
                # to next line. So we have to check this condition  and if it's True, save this information to variables
                # which are need to switch this off
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

                # Unselect selected characters
                selenium_element.send_keys(Keys.RIGHT)

                # Move back to the start of the line (after this, we reset action chain)
                self.action.send_keys(Keys.LEFT * (int(action[1]))).perform()
                self.action.reset_actions()

                # For pausing the script for some time
                self._time_patterns()

                # Check if we back to proper place - if not correct it
                n_to_move = self.move_cursor_to_start(
                    content=content_without_tags, selenium_element=selenium_element
                )
                selenium_element.send_keys(Keys.LEFT * n_to_move)

                # There is a glitch in Facebook text box - if our last word is formatting, the formatting will be moved
                # to next line. So we have to check this condition  and if it's True, save this information to variables
                # which are need to switch this off
                if action[1] == len(content_without_tags):
                    is_formatting_on = True
                    last_action = action[2]

        return is_formatting_on, last_action

    def send_post(self, content: str, selenium_element):
        """
        Function that sending content to Facebook Text Box and formatting it according to text formatting tags
        :param content: File path
        :param selenium_element: Location to web element we point with selenium
        """
        # Locate text formatting box
        text_modify_butttons = selenium_element.find_elements(
            By.XPATH, "//span[@class='x12mruv9 xfs2ol5 x1gslohp x12nagc']"
        )

        # Set empty list where we add text formatting tags - one for action without bold and italic and second for bold
        # and italic tags
        list_of_action_to_do_with_text_without_bold_and_italic = list()
        list_of_action_to_do_with_text_only_with_bold_and_italic = list()

        # Init var tags to store list with whole text formatting tags from text content
        tags = re.findall(r"<(.+?)>", content)

        # If any tags in text content
        if tags:
            # Iterate through tag in tags list
            for tag in tags:
                # Then take num and val from dictionary where we describe text formatting tag (i.e. 'b':0)
                for num, val in self.text_formatting_action.items():
                    # When val (i.e. 'b') is equal tag
                    if val == tag:
                        # To seperate bold and italic formatting from another tags, just check it and add to proper list
                        if num in (0, 1):
                            list_of_action_to_do_with_text_only_with_bold_and_italic.append(
                                num
                            )
                        # List for rest of text formatting actions
                        else:
                            list_of_action_to_do_with_text_without_bold_and_italic.append(
                                num
                            )

        # If we do not have any text formating action, just send a content and make a new line for next
        if (
            not list_of_action_to_do_with_text_without_bold_and_italic
            and not list_of_action_to_do_with_text_only_with_bold_and_italic
        ):
            # Send content and make a new line
            selenium_element.send_keys(content)
            selenium_element.send_keys(Keys.ENTER)

        # If we have text formatting
        else:
            # Init var content_without_tags where we store contenct without text formatting tags
            content_without_tags = re.sub("<[^<>]+>", "", content)

            # Init var n where we store lenght of content_without_tags
            n = len(content_without_tags)

            # Send content
            selenium_element.send_keys(content_without_tags)

            # Press and hold Shift then press left by n times (after this, we reset action chain)
            self.action.key_down(Keys.SHIFT).send_keys(Keys.LEFT * n).perform()
            self.action.reset_actions()

            # For pausing the script for some time
            self._time_patterns()

            # Iterate through action in list and click proper button to trigger them
            for action in list_of_action_to_do_with_text_without_bold_and_italic:
                text_modify_butttons[action].click()

                # For pausing the script for some time
                self._time_patterns(2)

            # Set cursor at the start of text
            selenium_element.send_keys(Keys.LEFT)

            # Check if we back to proper place - if not correct it
            n_to_move = self.move_cursor_to_start(
                content=content_without_tags, selenium_element=selenium_element
            )

            # Add n_to_move to variable when we store lenght of content to correct proper lenght
            n += n_to_move

            # Switch on bold and italic formatting and assign two variable is_formatting, last_action to fix FB glitch
            # (describe in 323 line)
            is_formatting, last_action = self.bold_and_italic_formatting(
                content=content,
                content_without_tags=content_without_tags,
                selenium_element=selenium_element,
                text_modify_butttons=text_modify_butttons,
            )

            # For pausing the script for some time
            self._time_patterns()

            # Move cursor to the end of line
            selenium_element.send_keys(Keys.RIGHT * n)

            # Check if we back to proper place - if not correct i
            self.move_cursor_to_end(content=content, selenium_element=selenium_element)

            # If last word was bold or italic, we have to switch it off before make new line
            if is_formatting:
                action = self.action
                key = "b" if last_action == 0 else "i"
                action.key_down(Keys.CONTROL).send_keys(key).perform()
                action.reset_actions()

            # If we use order or unorder list format we have to press Enter two times to switch off this formatting
            if (
                5 in list_of_action_to_do_with_text_without_bold_and_italic
                or 6 in list_of_action_to_do_with_text_without_bold_and_italic
            ):
                selenium_element.send_keys(Keys.ENTER)
                selenium_element.send_keys(Keys.ENTER)

            # In any other case press one time Enter will be ok
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

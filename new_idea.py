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
    def __init__(self, login, password):

        # For facebook login id credentials
        self.login = login

        # For facebook login password credentials
        self.password = password

        # Facebook page url
        self.base_url = "https://www.facebook.com/"

        # Setup Selenium Options
        # Add binary location for Firefox which is mandatory and headless mode on
        options = Options()
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
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

        # Run function to log into Facebook accocutn
        self._login_to_facebook()

    @staticmethod
    def get_txt(filename):
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
        return content

    def move_cursor_to_start(self, content: str, selenium_element):
        self.action.key_down(Keys.SHIFT).send_keys(Keys.RIGHT * 3).perform()
        self.action.reset_actions()

        self.action.key_down(Keys.CONTROL).key_down("c").perform()
        self.action.reset_actions()

        selenium_element.send_keys(Keys.LEFT)

        win32clipboard.OpenClipboard()
        copied_text = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()

        n_to_move = re.search(copied_text, content).start()

        for _ in range(n_to_move):
            selenium_element.send_keys(Keys.LEFT)
            self._time_patterns(2)

        return n_to_move

    def move_cursor_to_end(self, content: str, selenium_element):
        self.action.key_down(Keys.SHIFT).send_keys(Keys.LEFT * 3).perform()
        self.action.reset_actions()

        self.action.key_down(Keys.CONTROL).key_down("c").perform()
        self.action.reset_actions()

        selenium_element.send_keys(Keys.RIGHT)

        win32clipboard.OpenClipboard()
        copied_text = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()

        n_to_move = re.search(copied_text, content).end()
        n_to_move = len(content) - n_to_move

        if n_to_move > 0:
            for _ in range(n_to_move):
                selenium_element.send_keys(Keys.RIGHT)
                self._time_patterns(2)

        return n_to_move

    def _login_to_facebook(self):
        # This function is to log into Facebook

        self.driver.get(self.base_url)
        self.driver.find_element(
            By.XPATH,
            "//button[text()='Zezwól na korzystanie z niezbędnych i opcjonalnych plików cookie']",
        ).click()

        # For pausing the script for sometime
        self._time_patterns(3)

        self.driver.find_element(By.ID, "email").send_keys(self.login)
        self.driver.find_element(By.ID, "pass").send_keys(self.password)

        # For pausing the script for sometime
        self._time_patterns(3)

        self.driver.find_element(By.XPATH, "//button[text()='Zaloguj się']").click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "facebook"))
        )

    def _time_patterns(self, tp=None):
        # This function is to pause the script for some time
        # Also takes argument as second,
        # If not given then it will
        # Take by default seconds to wait
        if tp is None:
            time.sleep(self.time_pattern)

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
        splited_content = [x for x in re.split(r"<(.+?)>", content) if x != ""]

        steps = list()
        temp_clean_text = content_without_tags
        num = 0

        for elem in splited_content:
            if elem == "b" or elem == "i" or elem == "/i" or elem == "/b":
                to_add = [num, elem]
                steps.append(to_add)

            elif elem in temp_clean_text:
                if elem == " ":
                    continue
                num_to_add = temp_clean_text.index(elem) + len(elem)
                num = num_to_add

        for action in steps:
            for num, val in self.text_formatting_action.items():
                if val in action[1]:
                    action[1] = num
                    break

        action_to_execute = list()

        while steps:
            action = steps[0]
            start = action[0]
            text_formatter = action[1]
            for equal_action in steps[1:]:
                if equal_action[1] == text_formatter:
                    end = equal_action[0]
                    action_to_execute.append([start, end, text_formatter])

                    steps.remove(equal_action)
                    steps.remove(action)
                    break

        is_formatting_on = None
        last_action = None
        for action in action_to_execute:
            if action[0] == 0:
                self.action.key_down(Keys.SHIFT).send_keys(
                    Keys.RIGHT * int(action[1])
                ).perform()
                text_modify_butttons[action[2]].click()
                self.action.reset_actions()

                self._time_patterns()

                selenium_element.send_keys(Keys.RIGHT)
                self.action.send_keys(Keys.LEFT * int(action[1])).perform()
                self.action.reset_actions()

                self._time_patterns()

                n_to_move = self.move_cursor_to_start(
                    content=content_without_tags, selenium_element=selenium_element
                )
                selenium_element.send_keys(Keys.LEFT * n_to_move)

                if action[1] == len(content_without_tags):
                    is_formatting_on = True
                    last_action = action[2]

            else:
                self.action.send_keys(Keys.RIGHT * int(action[0])).perform()
                self.action.reset_actions()

                self.action.key_down(Keys.SHIFT).send_keys(
                    Keys.RIGHT * (int(action[1]) - int(action[0]))
                ).perform()
                text_modify_butttons[action[2]].click()
                self.action.reset_actions()

                self._time_patterns()

                selenium_element.send_keys(Keys.RIGHT)
                self.action.send_keys(Keys.LEFT * (int(action[1]))).perform()
                self.action.reset_actions()

                self._time_patterns()

                n_to_move = self.move_cursor_to_start(
                    content=content_without_tags, selenium_element=selenium_element
                )
                selenium_element.send_keys(Keys.LEFT * n_to_move)

                if action[1] == len(content_without_tags):
                    is_formatting_on = True
                    last_action = action[2]

        return is_formatting_on, last_action

    def text_editor(self, content: str, selenium_element):
        # Locate text formatting panel
        text_modify_butttons = selenium_element.find_elements(
            By.XPATH, "//span[@class='x12mruv9 xfs2ol5 x1gslohp x12nagc']"
        )

        # Set empty list where we add text modifier trigger - reference to self.text_formatting_action (check __init__)
        list_of_action_to_do_with_text_without_bold_and_italic = list()

        list_of_action_to_do_with_text_only_with_bold_and_italic = list()

        if re.findall(r"<(.+?)>", content):
            for tag in re.findall(r"<(.+?)>", content):
                for num, val in self.text_formatting_action.items():
                    if val == tag:
                        if num == 0 or num == 1:
                            list_of_action_to_do_with_text_only_with_bold_and_italic.append(
                                num
                            )
                        else:
                            list_of_action_to_do_with_text_without_bold_and_italic.append(
                                num
                            )

        # if we do not have any text formating action, just send a content and make a new line for next
        if (
            not list_of_action_to_do_with_text_without_bold_and_italic
            and not list_of_action_to_do_with_text_only_with_bold_and_italic
        ):
            selenium_element.send_keys(content)
            selenium_element.send_keys(Keys.ENTER)

        else:
            content_without_tags = re.sub("<[^<>]+>", "", content)
            n = len(content_without_tags)

            selenium_element.send_keys(content_without_tags)
            self.action.key_down(Keys.SHIFT).send_keys(Keys.LEFT * n).perform()
            self.action.reset_actions()
            self._time_patterns()

            for action in list_of_action_to_do_with_text_without_bold_and_italic:
                text_modify_butttons[action].click()
                self._time_patterns(2)

            # set cursor at the start of text
            selenium_element.send_keys(Keys.LEFT)

            n_to_move = self.move_cursor_to_start(
                content=content_without_tags, selenium_element=selenium_element
            )
            n += n_to_move

            is_formatting, last_action = self.bold_and_italic_formatting(
                content=content,
                content_without_tags=content_without_tags,
                selenium_element=selenium_element,
                text_modify_butttons=text_modify_butttons,
            )

            self._time_patterns()
            selenium_element.send_keys(Keys.RIGHT * n)
            self.move_cursor_to_end(content=content, selenium_element=selenium_element)

            if is_formatting:
                if last_action == 0:
                    time.sleep(2)
                    self.action.key_down(Keys.CONTROL).send_keys("b").perform()
                    self.action.reset_actions()

                else:
                    time.sleep(2)
                    self.action.key_down(Keys.CONTROL).send_keys("i").perform()
                    self.action.reset_actions()

            if (
                5 in list_of_action_to_do_with_text_without_bold_and_italic
                or 6 in list_of_action_to_do_with_text_without_bold_and_italic
            ):
                selenium_element.send_keys(Keys.ENTER)
                selenium_element.send_keys(Keys.ENTER)

            else:
                selenium_element.send_keys(Keys.ENTER)

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
                self.text_editor(content=line, selenium_element=postbox)


FacebookPoster(LOGIN_BETA, PASSWORD_BETA).prepare_and_send_post(
    content_filename="content/1.txt"
)

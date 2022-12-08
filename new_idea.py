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
        # Add binary location for Firefox which is mandatory
        # Headless mode on
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

        # INFO TO WRITE
        self.text_formatting_action = {
            0: "b",  # bold text
            1: "i",  # italics text
            2: "h1",  # h1 format
            3: "h2",  # h2 format
            4: "quote",  # quote text
            5: "ul",  # unordered list
            6: "ol",  # ordered list
        }

        # Run function to retrive or make cookie for Facebook session
        self._login_to_facebook()

    @staticmethod
    def get_txt(filename):
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
        return content

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

    def text_editor(self, content: str, selenium_element):
        # Locate text formatting bar with 7 buttons
        text_modify_butttons = selenium_element.find_elements(
            By.XPATH, "//span[@class='x12mruv9 xfs2ol5 x1gslohp x12nagc']"
        )

        # Set empty list where we add text modifier trigger - reference to self.text_formatting_action (check __init__)
        list_of_action_to_do_with_text = []

        # Check if text content contains ">" symbol - it's text modify tag i.e. <b> for bold text. If so, we itarate
        # through list elements (without last one, which is out text to modify) to check how many text modifier trigger
        # we have and then add them to list_of_action_to_do_with_text
        if len(content.split(">")) >= 2:
            for i in range(len(content.split(">")) - 1):
                for num, val in self.text_formatting_action.items():
                    if val == [con.replace("<", "") for con in content.split(">")][i]:
                        list_of_action_to_do_with_text.append(num)

        # left only last one element from list, which is text to post
        # set number of words and symbols in text to post
        if list_of_action_to_do_with_text:
            content_without_tags = content.split(">")[-1]
            n = len(content_without_tags.split())
            print(content_without_tags, n)

            selenium_element.send_keys(content_without_tags)
            self.action.key_down(Keys.SHIFT).key_down(Keys.CONTROL).send_keys(
                Keys.LEFT * n
            ).perform()
            self.action.reset_actions()

            for action in list_of_action_to_do_with_text:
                text_modify_butttons[action].click()

            self.action.key_down(Keys.SHIFT).key_down(Keys.CONTROL).send_keys(Keys.RIGHT * n).perform()
            self.action.reset_actions()

            if 0 in list_of_action_to_do_with_text:
                self.action.send_keys(Keys.SPACE).key_down(Keys.CONTROL).send_keys("b").perform()
                self.action.reset_actions()
            elif 1 in list_of_action_to_do_with_text:
                self.action.send_keys(Keys.SPACE).key_down(Keys.CONTROL).send_keys("i").perform()
                self.action.reset_actions()

            self.action.key_down(Keys.ENTER).perform()
            self.action.reset_actions()
            self._time_patterns(2)

        else:
            selenium_element.send_keys(content)
            self.action.key_down(Keys.SHIFT).key_down(Keys.ENTER).perform()
            self.action.reset_actions()

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
            self._time_patterns(3)

            # Activate postbox pop up to send value to it
            postbox = self.driver.switch_to.active_element

            # Load content from file
            content = self.get_txt(content_filename)

            for line in content.split("\n"):
                self.text_editor(content=line, selenium_element=postbox)

            # PLACE FOR NEW FUNCTION


FacebookPoster(LOGIN_BETA, PASSWORD_BETA).prepare_and_send_post(content_filename='content/1.txt')

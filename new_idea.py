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
import datetime
import math


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
        #options.add_argument("--headless")

        # Setup Firefox driver
        self.driver = Firefox(
            service=Service(GeckoDriverManager().install()), options=options
        )

        # Setup Selenium action chain
        self.action = ActionChains(self.driver)

        # By default, is set to 5,
        # will be used by time patterns
        self.time_pattern = 5  # seconds

        # Run function to retrive or make cookie for Facebook session
        self._login_to_facebook()

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

    def prepare_and_send_post(self):
        fb_groups = ['https://www.facebook.com/groups/1281302162058634/']
        for group in fb_groups:

            # Open Facebook group url
            self.driver.get(group + "buy_sell_discussion")
            print(f"/// Start processing group: {group + 'buy_sell_discussion'}")

            # For pausing the script for sometime
            self._time_patterns(8)

            # Locate postbox element and click it
            self.driver.find_element(
                By.XPATH,
                "//div[@class='x6s0dn4 x78zum5 x1l90r2v x1pi30zi x1swvt13 xz9dl7a']",
            ).click()

            # For pausing the script for sometime
            self._time_patterns(3)

            # Activate postbox pop up to send value to it
            element = self.driver.switch_to.active_element
            text_modify_butttons = element.find_elements(By.XPATH, "//span[@class='x12mruv9 xfs2ol5 x1gslohp x12nagc']")

            '''
            0 - pogrubienie
            1 - kursywa
            2 - h1
            3 - h2
            4 - cytat
            5 - unordered list
            6 - ordered list
            '''

            content = '[b]Nazwa stanowiska, tego genialnego zdania para tirara'
            n = len(content.split())

            element.send_keys(content)
            self.action.key_down(Keys.SHIFT).key_down(Keys.CONTROL).send_keys(Keys.LEFT * n).perform()
            text_modify_butttons[2].click()
            self.action.key_down(Keys.SHIFT).key_down(Keys.CONTROL).send_keys(Keys.RIGHT * n).send_keys(Keys.ENTER).perform()
            self.action.reset_actions()
            element.send_keys(Keys.ENTER)
            self._time_patterns(1)








# login BETA
LOGIN_BETA = "random2022@hsswork.pl"
PASSWORD_BETA = "Ewelina2022"

FacebookPoster(LOGIN_BETA, PASSWORD_BETA).prepare_and_send_post()
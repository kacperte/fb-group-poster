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

# Kacper
LOGIN_TRZEPIECINSKI = "kacper.trzepiecinski@hsswork.pl"
PASSWORD_TRZEPIECINSKI = "QuD*CC12d_Hju1!"

# Patrycja
LOGIN_ROSIK = "patrycja.rosik@hsswork.pl"
PASSWORD_ROSIK = "Patrycja2022!"

# Beta
LOGIN_BETA = "random2022@hsswork.pl"
PASSWORD_BETA = "Ewelina2022!"

# 1 HSS Work / Junior Sales / Łodź
# 2 Flex / OWW / Łódź
# 3 EMS / Lider UR / Ozorków
# 4 EMS / Lider magazynu / Ozorków
# 5 Commerz / AO Engineer / PL
# 6 Podcast #3
# 7 Ontex / Elektryk /
# 8 Commerzbank / Tester
# 9 Mera System / Lutowacz


list_of_group_ontex = [
    "https://www.facebook.com/groups/142724732594101",
    "https://www.facebook.com/groups/praca.radomsko.i.okolice/",
    "https://www.facebook.com/groups/753361791342068/",
    "https://www.facebook.com/groups/spottedradomsko/",
    "https://www.facebook.com/groups/1247057675373057/",
    "https://www.facebook.com/groups/2047887718650686/",
    "https://www.facebook.com/groups/399487134187093/",
    "https://www.facebook.com/groups/elektryka.zlecenia/",
]

list_of_groups_lodz = [
    "https://www.facebook.com/groups/pracawlodzkim/",
    "https://www.facebook.com/groups/1752579184959123/",
    "https://www.facebook.com/groups/960366354163646/",
    "https://www.facebook.com/groups/twojapraca/",
    "https://www.facebook.com/groups/760248644024490/",
    "https://www.facebook.com/groups/pracalodziokolice/",
    "https://www.facebook.com/groups/1136807080150710/",
    "https://www.facebook.com/groups/138646626771261/",
    "https://www.facebook.com/groups/763209430360245/",
    "https://www.facebook.com/groups/1416809508617643/",
    "https://www.facebook.com/groups/974282212628235/",
    "https://www.facebook.com/groups/2879497865669301/",
]

list_of_groups_near_to_lodz = [
    "https://www.facebook.com/groups/1591972677700028/",
    "https://www.facebook.com/groups/pracawlodzkim/",
    "https://www.facebook.com/groups/414347195775522/",
    "https://www.facebook.com/groups/1506773682975704/",
    "https://www.facebook.com/groups/787211341389390/",
    "https://www.facebook.com/groups/913932121977225/",
    "https://www.facebook.com/groups/1752579184959123/",
    "https://www.facebook.com/groups/960366354163646/",
    "https://www.facebook.com/groups/319428066419643/",
    "https://www.facebook.com/groups/743168796020262/",
    "https://www.facebook.com/groups/606779323257076/",
    "https://www.facebook.com/groups/twojapraca/",
    "https://www.facebook.com/groups/2129168737332275/",
    "https://www.facebook.com/groups/4747293448638141/",
    "https://www.facebook.com/groups/pracalodziokolice/",
    "https://www.facebook.com/groups/praca.zgierz.i.okolice/",
    "https://www.facebook.com/groups/763209430360245/",
    "https://www.facebook.com/groups/2879497865669301/",
    "https://www.facebook.com/groups/1746008952280288/",
    "https://www.facebook.com/groups/742377425799876/",
    "https://www.facebook.com/groups/579729288832677/",
    "https://www.facebook.com/groups/254387078043166/",
    "https://www.facebook.com/groups/290336925855596/",
    "https://www.facebook.com/groups/158416511613756/",
]

list_of_groups_test = ["https://www.facebook.com/groups/346798059107759"]

list_of_groups_it = [
    "https://www.facebook.com/groups/pracait/",
    "https://www.facebook.com/groups/codersbase/",
    "https://www.facebook.com/groups/695612637127175/",
    "https://www.facebook.com/groups/pracawbranzyit/",
    "https://www.facebook.com/groups/790784451359457/",
    "https://www.facebook.com/groups/217466495754575/",
    "https://www.facebook.com/groups/1037579849611331/",
    "https://www.facebook.com/groups/praca.it.wynagrodzenia/",
    "https://www.facebook.com/groups/1645832589008328/",
    "https://www.facebook.com/groups/2138351569774276/",
    "https://www.facebook.com/groups/1938514189734088/",
    "https://www.facebook.com/groups/1644439072503808/",
    "https://www.facebook.com/groups/1778129425801951/",
    "https://www.facebook.com/groups/1458889777456828/",
    "https://www.facebook.com/groups/programowanie.bez.ms/",
    "https://www.facebook.com/groups/663140057518227/",
    "https://www.facebook.com/groups/1401505446567527/",
    "https://www.facebook.com/groups/itselecta.comitrecruitment/",
    "https://www.facebook.com/groups/246806639124789/",
    "https://www.facebook.com/groups/234054030066096/",
    "https://www.facebook.com/groups/305254166296839/",
    "https://www.facebook.com/groups/268603053543086/",
]

list_of_groups_it_tester = [
    "https://www.facebook.com/groups/215557562210470/",
    "https://www.facebook.com/groups/testeroprogramowania/",
    "https://www.facebook.com/groups/TestowanieOprogramowania/",
    "https://www.facebook.com/groups/808752555920542/",
    "https://www.facebook.com/groups/1301980159852443/",
]

list_of_random_group_to_promote_podcast = [
    # "https://www.facebook.com/groups/1591972677700028/",
    "https://www.facebook.com/groups/pracawlodzkim/",
    "https://www.facebook.com/groups/414347195775522/",
    "https://www.facebook.com/groups/1506773682975704/",
    "https://www.facebook.com/groups/787211341389390/",
    "https://www.facebook.com/groups/913932121977225/",
    "https://www.facebook.com/groups/1752579184959123/",
    "https://www.facebook.com/groups/960366354163646/",
    "https://www.facebook.com/groups/319428066419643/",
    "https://www.facebook.com/groups/743168796020262/",
    "https://www.facebook.com/groups/606779323257076/",
    "https://www.facebook.com/groups/twojapraca/",
    "https://www.facebook.com/groups/2129168737332275/",
    "https://www.facebook.com/groups/4747293448638141/",
    "https://www.facebook.com/groups/pracalodziokolice/",
    "https://www.facebook.com/groups/praca.zgierz.i.okolice/",
    "https://www.facebook.com/groups/763209430360245/",
    "https://www.facebook.com/groups/2879497865669301/",
    "https://www.facebook.com/groups/1746008952280288/",
    "https://www.facebook.com/groups/742377425799876/",
    "https://www.facebook.com/groups/579729288832677/",
    "https://www.facebook.com/groups/254387078043166/",
    "https://www.facebook.com/groups/290336925855596/",
    "https://www.facebook.com/groups/158416511613756/",
    "https://www.facebook.com/groups/pracawlodzkim/",
    "https://www.facebook.com/groups/1752579184959123/",
    "https://www.facebook.com/groups/960366354163646/",
    "https://www.facebook.com/groups/twojapraca/",
    "https://www.facebook.com/groups/760248644024490/",
    "https://www.facebook.com/groups/pracalodziokolice/",
    "https://www.facebook.com/groups/1136807080150710/",
    "https://www.facebook.com/groups/138646626771261/",
    "https://www.facebook.com/groups/763209430360245/",
    "https://www.facebook.com/groups/1416809508617643/",
    "https://www.facebook.com/groups/974282212628235/",
    "https://www.facebook.com/groups/2879497865669301/",
    "https://www.facebook.com/groups/2119697838123790/",
    "https://www.facebook.com/groups/134620247233811/?ref=br_rs",
    "https://www.facebook.com/groups/WrocPraca/?ref=br_rs",
    "https://www.facebook.com/groups/1600710993482505/about/",
    "https://www.facebook.com/groups/wroclawpracapl/?ref=br_rs",
    "https://www.facebook.com/groups/1002400099791949/",
    "https://www.facebook.com/groups/329625857161837/?ref=br_rs",
    "https://www.facebook.com/groups/pracawroclawiokolice/about/",
    "https://www.facebook.com/groups/970385873014887/?ref=br_rs",
    "https://www.facebook.com/groups/894987590582987",
    "https://www.facebook.com/groups/830166273800534",
    "https://www.facebook.com/groups/586166761768852",
    "https://www.facebook.com/groups/314826248973624",
    "https://www.facebook.com/groups/ofertypracytychy",
    "https://www.facebook.com/groups/176926947533346",
    "https://www.facebook.com/groups/768998859799287/",
    "https://www.facebook.com/groups/251519282104808",
    "https://www.facebook.com/groups/172910724002911",
    "https://www.facebook.com/groups/1441643719216258/",
    "https://www.facebook.com/groups/1864456150448209/",
    "https://www.facebook.com/groups/1581482228819456/",
    "https://www.facebook.com/groups/2160293464226028/",
    "https://www.facebook.com/groups/422831414751045/",
    "https://www.facebook.com/groups/kutnopraca/",
    "https://www.facebook.com/groups/1761981317407784/",
    "https://www.facebook.com/groups/295322197529979/",
    "https://www.facebook.com/groups/1059257501093408/",
    "https://www.facebook.com/groups/136837740280564/",
    "https://www.facebook.com/groups/praca.plock.i.okolice/",
    "https://www.facebook.com/groups/1615681028454288/",
    "https://www.facebook.com/groups/pracawplocku/",
    "https://www.facebook.com/groups/780883142685634/",
]

list_of_groups_maintanance = [
    "https://www.facebook.com/groups/2204891923117646/",
    "https://www.facebook.com/groups/399487134187093/",
    "https://www.facebook.com/groups/elektryka.zlecenia/",
    "https://www.facebook.com/groups/elektryka.zlecenia/",
    "https://www.facebook.com/groups/967610236717155/",
    "https://www.facebook.com/groups/AutomatycyPoland/",
    "https://www.facebook.com/groups/UtrzymanieRuchuPL/",
    "https://www.facebook.com/groups/automatykairobotykaforum/",
    "https://facebook.com/groups/pracaautomatykarobotyka/",
    "https://www.facebook.com/groups/automatykaprzemyslowa/",
]

list_of_groups_mera = [
    "https://www.facebook.com/groups/praca.radom.oferty/",
    "https://www.facebook.com/groups/102812547144262/",
    "https://www.facebook.com/groups/1566853660289756/about",
    "https://www.facebook.com/groups/milanowekinfo/",
    "https://www.facebook.com/groups/1443439005961381/",
    "https://www.facebook.com/groups/radomsko.praca/",
    "https://www.facebook.com/groups/650962839027697/",
    "https://www.facebook.com/groups/1247057675373057/",
    "https://www.facebook.com/groups/151903202060044/",
    "https://www.facebook.com/groups/2027118057329011/",
    "https://www.facebook.com/groups/brwinowiokolica/",
    "https://www.facebook.com/groups/960260534307429/",
    "https://www.facebook.com/groups/2376693785885296/",
    "https://www.facebook.com/groups/1131602607257396/",
    "https://www.facebook.com/groups/1007691029384714/",
    "https://www.facebook.com/groups/791957241754089/",
    "https://www.facebook.com/groups/1952911918270413/",
    "https://www.facebook.com/groups/475463137187172/",
    "https://www.facebook.com/groups/552711378986043/",
    "https://www.facebook.com/groups/grodziskmaz/",
    "https://www.facebook.com/groups/1741013225979885/",
    "https://www.facebook.com/groups/227173234353057/",
    "https://www.facebook.com/groups/915405865154981/",
    "https://www.facebook.com/groups/791123128082671/",
]


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
        options.add_argument("--headless")

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

    def prepare_and_send_post(self, content_filename, image_path, groups):
        # This function is to post content on Facebook group

        # JS scripts to load images to post
        JS_DROP_FILE = """
            var target = arguments[0],
                offsetX = arguments[1],
                offsetY = arguments[2],
                document = target.ownerDocument || document,
                window = document.defaultView || window;

            var input = document.createElement('INPUT');
            input.type = 'file';
            input.onchange = function () {
              var rect = target.getBoundingClientRect(),
                  x = rect.left + (offsetX || (rect.width >> 1)),
                  y = rect.top + (offsetY || (rect.height >> 1)),
                  dataTransfer = { files: this.files };

              ['dragenter', 'dragover', 'drop'].forEach(function (name) {
                var evt = document.createEvent('MouseEvent');
                evt.initMouseEvent(name, !0, !0, window, 0, 0, 0, x, y, !1, !1, !1, !1, 0, null);
                evt.dataTransfer = dataTransfer;
                target.dispatchEvent(evt);
              });

              setTimeout(function () { document.body.removeChild(input); }, 25);
            };
            document.body.appendChild(input);
            return input;
        """

        # Load list of Facebook groups
        fb_groups = groups

        # Itarate through groups
        start_t = time.time()
        print(f"/// START PROCESS {datetime.datetime.now()}")
        for group in groups:

            # Load content from file
            content = self.get_txt(content_filename)

            try:
                # Open Facebook group url
                self.driver.get(group + "buy_sell_discussion")
                print(f"/// Start processing group: {group + 'buy_sell_discussion'}")

                # For pausing the script for sometime
                self._time_patterns(8)

                # Locate postbox element and click it
                self.driver.find_element(
                    By.XPATH,
                    "//div[@class='xi81zsa x1lkfr7t xkjl1po x1mzt3pk xh8yej3 x13faqbe']",
                ).click()

                # For pausing the script for sometime
                self._time_patterns(3)

                # Activate postbox pop up to send value to it
                element = self.driver.switch_to.active_element

                # Spilit content by newline symbol to dict
                content = content.split("\n")

                # Iterate through content
                for con in content:

                    # Make first paragraph bold
                    # Check if 1-st itarate element is 1-st element from content dict
                    if con == content[0]:

                        # Send value and then by action chain make it bold
                        element.send_keys(con)

                        # First using CTRL + A to select whole text and
                        # Then using CTRL + B to bold it
                        # Then using SHIFT + ENTER to make newline
                        self.action.key_down(Keys.CONTROL).send_keys("a").key_down(
                            Keys.CONTROL
                        ).send_keys("b").key_down(Keys.DOWN).key_down(
                            Keys.SHIFT
                        ).key_down(
                            Keys.ENTER
                        ).perform()

                        # Reste action chain
                        self.action.reset_actions()

                        # Then deactivate bold format
                        self.action.key_down(Keys.CONTROL).send_keys("b").perform()

                        # For pausing the script for sometime
                        self._time_patterns(3)

                    # Check if itarate element has colon symbol
                    # If so bold the paragraph before colon
                    elif ":" in con:
                        con = con.split(":")
                        self.action.key_down(Keys.CONTROL).send_keys("b").perform()
                        self.action.reset_actions()
                        element.send_keys(con[0] + ":")
                        self.action.send_keys(Keys.SPACE).key_down(
                            Keys.CONTROL
                        ).send_keys("b").perform()
                        self.action.reset_actions()
                        element.send_keys(con[1])
                        self.action.key_down(Keys.SHIFT).key_down(Keys.ENTER).perform()
                        self.action.reset_actions()

                    # Check if itarate element has question mark
                    # If so bold the paragraph before colon
                    elif "?" in con:
                        con = con.split("?")
                        self.action.key_down(Keys.CONTROL).send_keys("b").perform()
                        self.action.reset_actions()
                        element.send_keys(con[0] + "?")
                        self.action.send_keys(Keys.SPACE).key_down(
                            Keys.CONTROL
                        ).send_keys("b").perform()
                        self.action.reset_actions()
                        element.send_keys(con[1])
                        self.action.key_down(Keys.SHIFT).key_down(Keys.ENTER).perform()
                        self.action.reset_actions()

                    # If none of the above just send text
                    else:
                        element.send_keys(con)
                        self.action.key_down(Keys.SHIFT).key_down(Keys.ENTER).perform()
                        self.action.reset_actions()

                # For pausing the script for sometime
                self._time_patterns(5)

                # Add images to post
                driver = element.parent
                file_input = driver.execute_script(JS_DROP_FILE, element, 0, 0)
                file_input.send_keys(image_path)
                # For pausing the script for sometime
                self._time_patterns()

                # click post btn
                self.driver.find_element(
                    By.XPATH, "//div[@aria-label='Opublikuj']"
                ).click()

                # For pausing the script for sometime
                self._time_patterns(10)
                print(f"/// End processing group: {group + 'buy_sell_discussion'}\n")

            except Exception as e:
                print(
                    f"/// Problem with processing group: {group + 'buy_sell_discussion'}\nError: {e}"
                )
        duration_t = time.time() - start_t
        print(f"/// END PROCESS {datetime.datetime.now()}")
        print(f"/// Duration time: {math.ceil(duration_t / 60)} min")

    @staticmethod
    def get_txt(filename):
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
        return content


FacebookPoster(LOGIN_ROSIK, PASSWORD_ROSIK).prepare_and_send_post(
    content_filename="content/9.txt",
    groups=list_of_groups_mera,
    image_path=r"C:\Users\kacpe\OneDrive\Pulpit\Python\Projekty\facebook-group-poster\images\9.jpg",
)

from requests import get, post
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from requests.structures import CaseInsensitiveDict
import pyautogui
from multiprocessing import Pool
from quizes_imports import *


def main(time):
    # Selenium
    chrome_options = Options()

    port = 9222
    chrome_driver = "D:\Desktop\Programing\python\programs\Selenium\chromedriver\chromedriver.exe"

    # Dolphin Anti API
    username = "accounutsphemex@gmail.com"
    password = "1Qaz2Wsx3Edc"

    # Get access token
    token = post("https://anty-api.com/auth/login", data={"username": username, "password": password}).json()["token"]

    # Create request
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"

    # Get json structure with data about profiles(with id)
    profiles_data_json = get("https://anty-api.com/browser_profiles", headers=headers).json()["data"]

    profile_start = 1  # int(input("Enter the number of profile: "))
    while True:
        # Open profile and get opened port
        port = \
            get(f"http://localhost:3001/v1.0/browser_profiles/{profiles_data_json[profile_start - 1]['id']}/start?automation=1").json()[
                "automation"]["port"]

        # Selenium
        chrome_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{port}")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

        try:
            driver.maximize_window()
            driver.switch_to.window(driver.window_handles[1])
            profile_start += 1
            first_quiz(driver, time)  # passed
            second_quiz(driver, time)  # passed
            third_quiz(driver, time)  # passed
            fourth_quiz(driver, time)  # passed
            fifth_quiz(driver, time)  # passed
            sixth_quiz(driver, time)  # passed
            seventh_quiz(driver, time)  # soso
            eighth_quiz(driver, time)  # soso
            ninth_quiz(driver, time)  # passed
            tenth_quiz(driver, time)  # passed
            eleventh_quiz(driver, time)  # passed
            twelws_quiz(driver, time)  # passed

            sleep(5)
        except Exception as ex:
            print(ex)

        finally:
            driver.close()
            driver.quit()
            sleep(1)
            pyautogui.click(x=1900, y=4)
            sleep(0.2)
            pyautogui.click(x=993, y=434)
            sleep(5)
            pyautogui.click(x=925, y=435)
            sleep(7)
            if profile_start == 5:
                break


if __name__ == "__main__":
    p = Pool(processes=3)
    p.map(main, [3,3,3])


import random
import requests
from requests import get, post
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from requests.structures import CaseInsensitiveDict
import pyautogui
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from time import sleep
import openpyxl

#Selenium
chrome_options = Options()

port = 9222
chrome_driver = "D:\Desktop\Programing\python\programs\Selenium\chromedriver\chromedriver.exe"

# Dolphin Anti API
username = "accphemex@gmail.com"
password = "1Qaz2Wsx3Edc"

# Get access token
token = post("https://anty-api.com/auth/login", data={"username": username, "password": password}).json()["token"]

# Create request
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = f"Bearer {token}"

# Get json structure with data about profiles(with id)
profiles_data_json = get("https://anty-api.com/browser_profiles", headers=headers).json()["data"]

number_photo_start = int(input("Enter the number of photo ot start: "))
profile_start = int(input("Enter the number of profile to start: "))
profile_end = int(input("Enter the number of profile to end: "))

for i in range(profile_start-1, profile_end):

    # Get credentials for phemex
    book = openpyxl.load_workbook("accounts.xlsx")
    sheet = book.active

    login_onet = sheet[f"A{number_photo_start}"].value
    password_onet = sheet[f"B{number_photo_start}"].value  # [:-1]
    print(login_onet)
    print(password_onet)
    number_photo_start += 1

    # # Fake useragent
    # useragent = UserAgent()
    #
    # # Create profile
    #
    # data = {
    #     'name': f'{login_onet}',
    #     'tags[]': '',
    #     'tabs': [],
    #     'platform': 'windows',
    #     'mainWebsite': '',
    #     'useragent[mode]': 'auto',
    #     'useragent[value]': '',
    #     'webrtc[mode]': 'altered',
    #     'webrtc[ipAddress]': '',
    #     'canvas[mode]': 'real',
    #     'webgl[mode]': 'real',
    #     'webglInfo[mode]': 'real',
    #     'webglInfo[vendor]': '',
    #     'webglInfo[renderer]': '',
    #     'notes[icon]': '',
    #     'notes[color]': '',
    #     'notes[style]': '',
    #     'notes[content]': '',
    #     'timezone[mode]': 'auto',
    #     'timezone[value]': '',
    #     'locale[mode]': 'auto',
    #     'locale[value]': '',
    #     'statusId': '0',
    #     'geolocation[mode]': 'real',
    #     'geolocation[latitude]': '',
    #     'geolocation[longitude]': '',
    #     'cpu[mode]': 'manual',
    #     'cpu[value]': 'real',  # f'{random.choice([2, 4, 8, 16])}'
    #     'memory[mode]': 'manual',
    #     'memory[value]': 'real', # f'{random.choice([2, 4, 8])}'
    #     'doNotTrack': '0',
    #     'browserType': 'anty',
    #     'proxy[id]': '',
    #     'proxy[type]': 'http',
    #     'proxy[host]': '127.0.0.1',
    #     'proxy[port]': '9222',
    #     'proxy[login]': '',
    #     'proxy[password]': '',
    #     'proxy[name]': '',
    #     'proxy[changeIpUrl]': ''
    # }
    #
    # response = post('https://anty-api.com/browser_profiles', headers=headers, data=data,)
    # print(response.json()["browserProfileId"])
    # print(requests.patch(url=f'https://anty-api.com/browser_profiles/:{response.json()["browserProfileId"]}', data=data, headers=headers).json())
    # Open profile and get opened port
    port = get(f"http://localhost:3001/v1.0/browser_profiles/{profiles_data_json[i]['id']}/start?automation=1").json()[
                    "automation"]["port"]

    # Selenium
    chrome_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{port}")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

    try:
        driver.maximize_window()
        pyautogui.click(x=810, y=1060)
        sleep(0.1)
        pyautogui.click(x=860, y=1060)
        sleep(0.1)
        pyautogui.click(x=20, y=500)
        sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        sleep(1)
        cred_fields = driver.find_elements(By.TAG_NAME, "input")
        cred_fields[0].clear()  # clear the input form(optional)
        cred_fields[0].send_keys(login_onet)

        cred_fields[1].clear()  # clear the input form(optional)
        cred_fields[1].send_keys(password_onet)

        submit_button = driver.find_element(By.TAG_NAME, "button").click()

        # Change Tab
        driver.switch_to.window(driver.window_handles[0])
        driver.implicitly_wait(3)
        pyautogui.click(x=1057, y=799)
        driver.implicitly_wait(2)
        driver.find_element(By.XPATH, '//*[@id="mailFormLogin"]').send_keys(login_onet)
        driver.find_element(By.XPATH, '//*[@id="mailFormPassword"]').send_keys(password_onet)
        driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[3]/input').click()
        sleep(3)
        driver.refresh()
        driver.implicitly_wait(3)
        for i in range(2, 8):
            if driver.find_element(By.XPATH, f'//*[@id="wrapper"]/div[4]/div/div[1]/div/section/div/div/div[{i}]/div/div[3]/div/div/div/span/span').text == "PHEMEX":
                secret_code = driver.find_element(By.XPATH, f'//*[@id="wrapper"]/div[4]/div/div[1]/div/section/div/div/div[{i}]/div/div[4]/div/div/div/span[1]/span').text.split(' ')[0]
                break

        #  Change tab
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[4]/div/div[1]/div[1]/input').send_keys(secret_code)
        sleep(3)
        pyautogui.click(x=1150, y=899)
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div/div/div[3]/div[1]/div[2]/button').click()
        sleep(2)
        pyautogui.click(x=859, y=536)
        sleep(1)
        pyautogui.click(x=906, y=708)
        sleep(4)
        pyautogui.click(x=886, y=574)
        sleep(2)
        driver.find_element(By.XPATH, '//*[@id="country-search"]').send_keys("Poland")
        pyautogui.click(x=871, y=500)
        driver.implicitly_wait(2)
        pyautogui.click(x=958, y=804)
        sleep(2)
        pyautogui.click(x=1104, y=806)
        sleep(1)
        driver.find_element(By.CLASS_NAME, 'onfido-sdk-ui-CustomFileInput-input').send_keys(fr"D:\Desktop\accounts\{number_photo_start}\front.jpg")
        sleep(1)
        pyautogui.click(x=1031, y=809)
        sleep(9)
        driver.find_element(By.CLASS_NAME, 'onfido-sdk-ui-CustomFileInput-input').send_keys(fr"D:\Desktop\accounts\{number_photo_start}\back.jpg")
        sleep(1)
        pyautogui.click(x=1031, y=809)
        sleep(9)
        pyautogui.click(x=937, y=795)

        # sleep(0.5)
        # pyautogui.click(x=937, y=795)
        # sleep(0.5)
        # # Allove notification
        # pyautogui.click(x=268, y=162)
        # sleep(0.5)
        # # allow camera
        # pyautogui.click(x=268, y=162)
        # # Make photo
        # sleep(4)
        # pyautogui.click(x=959, y=785)
        # Submit photo
        sleep(25)
        pyautogui.click(x=1075, y=800)
        sleep(2)
        pyautogui.click(x=1190, y=300)
        sleep(1)


    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
        sleep(0.5)
        pyautogui.click(x=1900, y=4)
        sleep(40)
        # sleep(0.2)
        # pyautogui.click(x=993, y=434)
        # sleep(5)
        # pyautogui.click(x=925, y=435)
        # sleep(7)

# Point(x=906, y=708) Submit
# Point(x=859, y=536) Choice
# Point(x=838, y=580) Documents
# Point(x=871, y=500) Poland
# Point(x=958, y=804) Submit
# Point(x=1104, y=806) Confirm
# Point(x=985, y=795) Choce photo
# (x=1031, y=809) Confirm photo
# (x=937, y=795) Get secure link

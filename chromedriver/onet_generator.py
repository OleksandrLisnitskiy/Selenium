import pyautogui
from selenium import webdriver
# from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from fake_useragent import UserAgent
from vars import names, surnames
import random
chrome_options = Options()

chrome_driver = "D:\Desktop\Programing\python\programs\Selenium\chromedriver\chromedriver.exe"
characters = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# number_of_emails = int(input("Enter the number of emails to create: "))
# mails_end = ["op.pl", "onet.pl", "onet.eu", "vp.pl", "spoko.pl", "autograf.pl", "onet.com.pl"]

i = 0

# for i in range(number_of_emails):
while True:
    try:

        f2 = open("emails.txt", mode="a")
        #  Change UserAgent
        useragent = UserAgent()
        chrome_options.add_argument(f"useragent={useragent.random}")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        # chrome_options.add_argument("--headless")
        # proxy_options = {
        #     "proxy": {
        #         "https": "http://sasharexe3740:8df35d@109.248.7.193:10865",
        #         "http": "http://sasharexe3740:8df35d@109.248.7.193:10865"
        #     }
        # }
        driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)  # seleniumwire_options=proxy_options

        driver.get("https://konto.onet.pl/en/register?client_id=poczta.onet.pl.front.onetapi.pl")

        driver.implicitly_wait(2)
        sleep(1)
        button = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div[2]/div/div[6]/button[2]/span")
        driver.execute_script("arguments[0].click();", button)
        # Generate email
        email_name = random.choice(names) + random.choice(surnames) + str(random.randint(100000, 1000000))
        driver.find_element(By.TAG_NAME, "input").send_keys(email_name)

        sleep(1)
        driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div/div/div/form/div[2]/div/button'))

        # Generate the password
        sleep(1)
        password = "".join(random.sample(characters, 18))
        driver.find_element(By.ID, "newPassword").send_keys(password)
        driver.find_element(By.ID, "rePassword").send_keys(password)

        sleep(1)
        driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div/div/div/form/button'))

        # put additional email
        sleep(1)
        driver.find_element(By.ID, "recoveryEmail").send_keys(random.choice(names) + random.choice(surnames) + "@gmail.com")
        sleep(1)
        driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div/div/div/form/div[3]/button'))

        # enter data
        driver.implicitly_wait(2)
        sleep(2)
        button_2 = driver.find_element(By.XPATH, '//*[@id="K"]')
        driver.execute_script("arguments[0].click();", button_2)
        driver.find_element(By.ID, "name").send_keys(random.choice(names) + " " + random.choice(surnames))
        driver.find_element(By.ID, "birthDate.day").send_keys(random.randint(1, 30))
        driver.find_element(By.ID, "birthDate.month").send_keys("march")
        driver.find_element(By.ID, "birthDate.year").send_keys(random.randint(1996, 2002))
        sleep(1)
        driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div/div/div/form/div[5]/button'))
        sleep(1)
        # Chose plan
        driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div/div/div/div[3]/button'))

        # accept policies
        sleep(0.2)
        driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div/div/div/form/div[1]/button'))
        sleep(1)
        driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div/div/div/form/div[2]/div/button'))
        sleep(3.5)
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div/div/div/div[2]/a')
        driver.close()
        driver.quit()
        f2.write(f"{email_name.lower()}@op.pl:{password}\n")
        i += 1
        print(i)
        # i = 0
        f2.close()
        # sleep(1)
        # pyautogui.click(x=755, y=1057)
        # pyautogui.click(x=1180, y=415)
        # sleep(8)
        # pyautogui.click(x=1180, y=415)
        # sleep(9)

    except Exception as ex:
        print(ex)
        driver.close()
        driver.quit()
        # i += 1
        if i == -3:
            sleep(2)
            # pyautogui.click(x=755, y=1057)
            # pyautogui.click(x=1180, y=415)
            # sleep(8)
            # pyautogui.click(x=1180, y=415)
            # sleep(9)


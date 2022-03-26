from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


def take_quiz(driver, url):
    driver.get(url)
    driver.implicitly_wait(2)
    sleep(11)
    clicker(driver, "/html/body/div[2]/div/div/div/div[2]/div/div[2]/button", 11)  # Take quiz button
    driver.implicitly_wait(2)


def clicker(driver, xpath, time=10):
    """

    :param driver:
    :param xpath:
    :param time:
    :return:
    """
    element = WebDriverWait(driver, time).until(
        EC.presence_of_element_located((By.XPATH, xpath)))  # Take quiz button
    driver.execute_script("arguments[0].click();", element)


def sender(driver, xpath, value, time=5):
    """

    :param driver:
    :param xpath:
    :param value:
    :param time:
    :return:
    """
    element = WebDriverWait(driver, time).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
    element.send_keys(value)


def first_quiz(driver, time):
    take_quiz(driver, 'https://phemex.com/ru/learn-crypto/crypto-fiat/what-is-fiat')
    # First quiz

    sleep(time)
    clicker(driver, "/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[3]/span", 4)  # FIRST: Goverment and Central Banks
    sleep(1)
    clicker(driver, '/html/body/div[2]/div/div/div[3]/div[2]/button', 3)  # Next button

    sleep(time)
    clicker(driver, '/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[2]/span', 3) # SECOND:  NO
    sleep(1)
    clicker(driver, '/html/body/div[2]/div/div/div[3]/div[2]/button[2]', 3)  # Next button

    sleep(time)
    clicker(driver, '/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[1]/span', 3)  # THIRD: Inflation
    sleep(1)
    clicker(driver, '/html/body/div[2]/div/div/div[3]/div[2]/button[2]', 3)  # Next button

    sleep(time)
    clicker(driver, '/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[1]/img', 3)  # FOURTH: US Dollar
    clicker(driver, '/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[4]/img', 3)  # FOURTH: Euro
    sleep(1)
    clicker(driver, '/html/body/div[2]/div/div/div[3]/div[2]/button[2]', 3)  # Submit button

    sleep(3)


def second_quiz(driver, time):
    take_quiz(driver, 'https://phemex.com/ru/learn-crypto/crypto-fiat/what-is-crypto')

    sleep(time)
    sender(driver, "/html/body/div[2]/div/div/div[3]/div[1]/div/div[1]/input", "digital")  # FIRST: Digital
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button', time=3)  # Next button

    sleep(time)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[3]/span', time=2)  # SECOND: Unique digital...
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=3)  # Next button

    sleep(time)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[4]/span', time=3)  # THIRD: None of the above
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=3)  # Next button

    sleep(time)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[2]/img', time=3)  # FOURTH: Bitcoin
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=2)  # Next button

    sleep(time)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[1]/span', time=3)  # FIFTH: Inflation
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[2]/span', time=3)  # FIFTH: Deflation
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=2)  # Submit

    sleep(4)


def third_quiz(driver, time):
    take_quiz(driver, 'https://phemex.com/ru/learn-crypto/crypto-fiat/how-does-crypto-work')

    sleep(time)
    clicker(driver, '/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[2]/span', 3)  # FIRST: Blockchain Technology
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button', time=3)  # Next button

    sleep(time)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[1]/span', time=2)  # A digital ledger or notebook
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=3)  # Next button

    sleep(time)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[4]/span', time=3)  # THIRD: All of the above
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=3)  # Next button

    sleep(time)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[1]/span', time=3)  # FOURTH: It has multiple copies...
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[2]/span', time=3)  # FOURTH:  It uses encryption...
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=2)  # Submit

    sleep(4)


def fourth_quiz(driver, time):
    take_quiz(driver, 'https://phemex.com/ru/learn-crypto/how-to-buy-crypto/credit-card')

    sleep(time)
    clicker(driver, '/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[1]/span', 3)  # FIRST: YES
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button', time=3)  # Next button

    sleep(time)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[3]/img', time=3)  # SECOND: Bitcoin
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=3)  # Next button

    sleep(time)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[4]/span', time=3)  # THIRD: CoolCrypto
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=2)  # Submit

    sleep(4)


def fifth_quiz(driver, time):
    take_quiz(driver, 'https://phemex.com/ru/learn-crypto/how-to-buy-crypto/otc-activate')

    sleep(time)
    clicker(driver, "/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[1]/span", 4)  # FIRST: Over-the-counter
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button', time=3)  # Next button

    sleep(time)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[2]/span', time=2)  # SECOND: Purchasse crypto...
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=3)  # Next button

    sleep(time)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[4]/span', time=3)  # THIRD: Buy crypto
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=3)  # Next button

    sleep(time)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[2]/span', time=3)  # FOURTH: NO
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=2)  # Next button

    sleep(time)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[2]/span', time=3)  # FIFTH: Individual
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=2)  # Submit

    sleep(4)

def sixth_quiz(driver, time):
    take_quiz(driver, 'https://phemex.com/ru/learn-crypto/how-to-buy-crypto/otc-deposit')

    sleep(time)
    sender(driver, "/html/body/div[2]/div/div/div[3]/div[1]/div/div[1]/input[1]", 'balance')  # FIRST:
    sender(driver, "/html/body/div[2]/div/div/div[3]/div[1]/div/div[1]/input[2]", 'module')  # FIRST:
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button', time=3)  # Next button

    sleep(time)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[2]/span', time=2)  # SECOND: Deposit
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=3)  # Next button

    sleep(time)
    sender(driver, '/html/body/div[2]/div/div/div[3]/div[1]/div/div[1]/input', "NAEIQWH")  # THIRD: Buy crypto
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=3)  # Next button

    sleep(time)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[4]/span', time=3)  # FOURTH: NO
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=2)  # Submit

    sleep(4)


def seventh_quiz(driver, time):
    take_quiz(driver, 'https://phemex.com/ru/learn-crypto/how-to-buy-crypto/otc-purchase')

    sleep(time)
    clicker(driver, "/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[3]/span", 3)  # FIRST:
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button', time=3)  # Next button

    sleep(time)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[3]/span', time=3)  # SECOND: 11 second
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=3)  # Next button

    sleep(time)
    clicker(driver, '/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[2]/span', time=3)  # THIRD: 3.14
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=2)  # Submit

    sleep(4)


def eighth_quiz(driver, time):
    take_quiz(driver, 'https://phemex.com/ru/learn-crypto/how-to-buy-crypto/transfer')

    sleep(time)
    clicker(driver, "/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[1]/span", 3)  # FIRST: Deposit button
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button', time=3)  # Next button

    sleep(time)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[2]/img', time=3)  # SECOND: Bitcoin
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=3)  # Next button

    sleep(time)
    clicker(driver, '/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[4]/span', time=3)  # THIRD: Disply QR-code
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=3)  # Next button

    sleep(time)
    clicker(driver, '/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[1]/span', time=3)  # FOURTH: Assets page
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=2)  # Submit

    sleep(4)


def ninth_quiz(driver, time):
    take_quiz(driver, 'https://phemex.com/ru/learn-crypto/spot-trading/introduction')

    sleep(time)
    clicker(driver, "/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[2]/span", 3)  # FIRST: Transactions that settle...
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button', time=3)  # Next button

    sleep(time)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[3]/span', time=3)  # SECOND: Spot Market
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=3)  # Next button

    sleep(time)
    clicker(driver, '/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[1]/span', time=3)  # THIRD: Instantly Available
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=3)  # Next button

    sleep(time)
    clicker(driver, '/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[2]/span', time=3)  # FOURTH: Stock
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=2)  # Submit

    sleep(4)


def tenth_quiz(driver, time):
    take_quiz(driver, 'https://phemex.com/ru/learn-crypto/spot-trading/spot-limit-orders')

    sleep(time)
    sender(driver, "/html/body/div[2]/div/div/div[3]/div[1]/div/div[1]/input[1]", 'limit')  # FIRST:
    sender(driver, "/html/body/div[2]/div/div/div[3]/div[1]/div/div[1]/input[2]", 'price')  # FIRST:
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button', time=3)  # Next button

    sleep(time)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[1]/span', time=2)  # SECOND: Limit
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=3)  # Next button

    sleep(time)
    clicker(driver, '/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[4]/span', time=3)  # THIRD: Limit price...
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=3)  # Next button

    sleep(time)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[2]/span', time=3)  # FOURTH: . Order will automatically...
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=3)  # Next button

    sleep(time)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[1]/span', time=3)  # FIFTH: . Order will be...
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=3)  # Next button

    sleep(time)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[4]/span', time=3)  # SIXTH: . Order will be added...
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=3)  # Next button

    sleep(time)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[3]/span', time=3)  # SEVENTH: When the price of...
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=2)  # Submit

    sleep(4)


def eleventh_quiz(driver, time):
    take_quiz(driver, 'https://phemex.com/ru/learn-crypto/spot-trading/spot-market-orders')

    sleep(time)
    clicker(driver, '/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[3]/span', 3)
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button', time=3)  # Next button

    sleep(time)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[3]/span', time=3)
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=3)  # Next button

    sleep(time)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[1]/span', time=3)
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=2)  # Submit

    sleep(4)


def twelws_quiz(driver, time):
    take_quiz(driver, 'https://phemex.com/ru/learn-crypto/spot-trading/spot-conditional-orders')

    sleep(time)
    clicker(driver, "/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[1]/span", 3)
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button', time=3)  # Next button

    sleep(time)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[3]/span', time=2)
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=3)  # Next button

    sleep(time)
    clicker(driver, '/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[4]/span', time=3)
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=3)  # Next button

    sleep(time)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[2]/span', time=3)
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=3)  # Next button

    sleep(time)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[1]/span', time=3)
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=3)  # Next button

    sleep(time)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[1]/div/div[2]/div[4]/span', time=3)
    sleep(1)
    clicker(driver, xpath='/html/body/div[2]/div/div/div[3]/div[2]/button[2]', time=2)  # Submit

    sleep(4)
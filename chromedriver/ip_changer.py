from pyautogui import click
from time import sleep


def changer():

    click(x=975, y=435)

    sleep(6)

    click(x=975, y=435)


def main():
    while True:
        changer()
        sleep(180)


if __name__ == "__main__":
    main()
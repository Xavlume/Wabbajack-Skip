from pyautogui import locateOnScreen, center, click
from time import sleep
from configparser import ConfigParser

#Default values
delay_between_tries = 0.2
delay_after_succeding = 1

#If the config has values, use those instead
config = ConfigParser()
config.read('settings.ini')

if config.has_option("SETTINGS", "delay_between_tries"):
    delay_between_tries = float(config["SETTINGS"]["delay_between_tries"])

if config.has_option("SETTINGS", "delay_after_succeding"):
    delay_after_succeding = float(config["SETTINGS"]["delay_after_succeding"])

#Main loop
while True:
    sleep(delay_between_tries)

    download_location = locateOnScreen("reference.png")

    if download_location is None:
        #print("Cannot find download location")
        continue

    download_point_location = center(download_location)

    click(download_point_location.x, download_point_location.y)

    sleep(delay_after_succeding)
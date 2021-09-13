import sys
import time
import datetime
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

print('----------\nDeveloped by Hikko\nhttps://github.com/Hikk0o\n----------\n')
print('Файл с логами coef.txt будет находиться в корневой папке программы.\nЧтобы закрыть программу, нажмите Ctrl+C.\n')
options = webdriver.ChromeOptions()
options.headless = True
options.add_experimental_option('excludeSwitches', ['enable-logging'])
print('Создание браузера...')
driver = webdriver.Chrome('C:/Chrome/chromedriver.exe', options=options)
print('Подключение к сайту...')
driver.get("https://csgorun.pro/")
time.sleep(2)
print('Получение данных от сайта...')

last_cof = ""
last_num = ""

x = 1
try:
    while x:
        html = driver.find_element_by_class_name("graph-svg__counter")
        string = html.get_attribute('innerHTML')
        now_cof = string[len(string) - 1]
        if now_cof == "x":
            last_cof = now_cof
            last_num = string
        elif last_cof != now_cof and last_num != "" and now_cof == "s":
            print(f'{last_num}')
            last_cof = now_cof
            file = open("coef.txt", "a")
            now = datetime.datetime.now()
            file.write(f'[{now.strftime("%d-%m-%Y %H:%M")}] {last_num}\n')
            file.close()
        time.sleep(1)
except (KeyboardInterrupt, WebDriverException):
    x = 0
    driver.quit()

sys.exit()

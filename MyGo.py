
from asyncio import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import xlsxwriter
import numpy as np
import spacy
from spacy.lang.fr.examples import sentences
import numpy as np
from DataClass import Data
from nltk.tokenize import sent_tokenize
import pandas as pd
from os import getenv, path
import dotenv
import datetime

Now = datetime.datetime.now()


date_start = input(str("start (day/monthe/year) : "))
date_finish = input(str("finish (day/monthe/year) : "))
nlp = spacy.load("fr_core_news_sm")

filename = "MyGo"
workbook = xlsxwriter.Workbook('{}.xlsx'.format(str(filename)))

mygoagance = getenv('mygo_your_agance')
mygousername = getenv('mygo_username')
mygopassword = getenv('mygo_password')


options = webdriver.FirefoxOptions()
driverfx = webdriver.Firefox(
    options=options, executable_path="../code/chromedriver/geckodriver")

willayas = getenv('willayas')
willaya = willayas[0]
sheet = np.array([["names", "prix"]])
time.sleep(1)
driverfx.get("https://mygo.pro/")
time.sleep(1)
driverfx.find_element(By.NAME, "actor").send_keys(mygoagance)
time.sleep(1)
driverfx.find_element(By.NAME, "login").send_keys(mygousername)
time.sleep(1)
driverfx.find_element(By.NAME, "password").send_keys(mygopassword)
time.sleep(3)
submygo = driverfx.find_element(By.ID, "home-submit-btn")
time.sleep(3)
submygo.click()
time.sleep(4)
hotelbutt = driverfx.find_element(By.CLASS_NAME, "hotels")
time.sleep(4)
hotelbutt.click()
time.sleep(4)
driverfx.find_element(By.ID, "ESautocomplete").send_keys(willaya)
time.sleep(2)
driverfx.find_element(By.ID, "ESautocomplete").send_keys(Keys.ARROW_DOWN)
time.sleep(2)
driverfx.find_element(By.ID, "ESautocomplete").send_keys(Keys.ENTER)
time.sleep(2)

date1 = driverfx.find_element(
    By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div/div[3]/div[1]/div[2]/div/div[1]/div[1]/input[2]")
date1.click()
date1.send_keys(Keys.CONTROL + 'a')
date1.clear()
date1.send_keys(date_start)
date1.send_keys(Keys.ENTER)

time.sleep(2)
date2 = driverfx.find_element(
    By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div/div[3]/div[1]/div[2]/div/div[1]/div[2]/input[2]")
date2.send_keys(Keys.CONTROL + 'a')
date2.clear()
date2.send_keys(date_finish)
date2.send_keys(Keys.ENTER)


time.sleep(2)

driverfx.find_element(By.ID, "availBtn").click()
time.sleep(20)
driverfx.execute_script("window.scrollTo(0, document.body.scrollHeight);")
ContH = list(range(1, 10))
time.sleep(4)
for i in ContH:
    time.sleep(4)
    try:
        names = driverfx.find_element(
            By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[3]/div/div[5]/div[3]/div[2]/div[{}]".format(str(i)))
        time.sleep(3)
        fh = open("names.text", "w")
        # fh.write(names.text)
        fh.write(names.text.lower())
        fh.close()
        file = open("names.text", "r").read()
        text = [line for line in file.splitlines()]
        sheet = Data.ClassData_Mygo(text, willaya, sheet)

    except:
        pass

try:
    time.sleep(10)
    NextButt = driverfx.find_element(
        By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[3]/div/div[5]/div[1]/div[2]/div[2]/div[1]/div[1]/div[6]")
    time.sleep(3)
    NextButt.click()
    time.sleep(10)
    driverfx.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    ContH = list(range(1, 10))
    time.sleep(4)
    for i in ContH:
        try:
            names = driverfx.find_element(
                By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[3]/div/div[5]/div[3]/div[2]/div[{}]".format(str(i)))
            time.sleep(3)
            fh = open("names.text", "w")
            # fh.write(names.text)
            fh.write(names.text.lower())
            fh.close()
            file = open("names.text", "r").read()
            text = [line for line in file.splitlines()]
            sheet = Data.ClassData_Mygo(text, willaya, sheet)

        except:
            pass
except:
    pass

try:
    time.sleep(3)

    while (True):
        time.sleep(10)
        NextButt = driverfx.find_element(
            By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[3]/div/div[5]/div[1]/div[2]/div[2]/div[1]/div[1]/div[7]")
        time.sleep(3)
        NextButt.click()
        time.sleep(10)
        driverfx.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        ContH = list(range(1, 10))
        time.sleep(4)
        for i in ContH:
            try:
                names = driverfx.find_element(
                    By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[3]/div/div[5]/div[3]/div[2]/div[{}]".format(str(i)))
                time.sleep(3)
                fh = open("names.text", "w")
                # fh.write(names.text)
                fh.write(names.text.lower())
                fh.close()
                file = open("names.text", "r").read()
                text = [line for line in file.splitlines()]
                sheet = Data.ClassData_Mygo(text, willaya, sheet)
            except:
                pass
except:
    pass

willayas = willayas[1:]
try:
    for willaya in willayas:

        time.sleep(3)
        modifButt = driverfx.find_element(By.ID, "edit_search_btn")
        time.sleep(3)
        modifButt.click()
        time.sleep(2)
        searchbar = driverfx.find_element(By.ID, "ESautocomplete")
        time.sleep(3)
        searchbar.send_keys(Keys.CONTROL + 'a')
        time.sleep(3)
        searchbar.clear()
        time.sleep(3)
        searchbar.send_keys(willaya)
        time.sleep(2)
        searchbar.send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        searchbar.send_keys(Keys.ENTER)
        time.sleep(2)
        driverfx.find_element(By.ID, "availBtn").click()
        time.sleep(10)
        driverfx.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        ContH = list(range(1, 10))
        time.sleep(4)
        for i in ContH:
            time.sleep(4)
            try:

                names = driverfx.find_element(
                    By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[3]/div/div[5]/div[3]/div[2]/div[{}]".format(str(i)))
                time.sleep(3)
                fh = open("names.text", "w")
                # fh.write(names.text)
                fh.write(names.text.lower())
                fh.close()
                file = open("names.text", "r").read()
                text = [line for line in file.splitlines()]
                sheet = Data.ClassData_Mygo(text, willaya, sheet)

            except:
                pass

            try:
                time.sleep(10)
                NextButt = driverfx.find_element(
                    By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[3]/div/div[5]/div[1]/div[2]/div[2]/div[1]/div[1]/div[6]")
                time.sleep(3)
                NextButt.click()
                time.sleep(10)
                driverfx.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
                ContH = list(range(1, 10))
                time.sleep(4)
                for i in ContH:
                    try:
                        names = driverfx.find_element(
                            By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[3]/div/div[5]/div[3]/div[2]/div[{}]".format(str(i)))
                        time.sleep(3)
                        fh = open("names.text", "w")
                        # fh.write(names.text)
                        fh.write(names.text.lower())
                        fh.close()
                        file = open("names.text", "r").read()
                        text = [line for line in file.splitlines()]
                        sheet = Data.ClassData_Mygo(text, willaya, sheet)

                    except:
                        pass
            except:
                pass

            try:
                while (True):
                    time.sleep(10)
                    NextButt = driverfx.find_element(
                        By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[3]/div/div[5]/div[1]/div[2]/div[2]/div[1]/div[1]/div[7]")
                    time.sleep(3)
                    NextButt.click()
                    time.sleep(10)
                    driverfx.execute_script(
                        "window.scrollTo(0, document.body.scrollHeight);")
                    ContH = list(range(1, 10))
                    time.sleep(4)
                    for i in ContH:
                        try:
                            names = driverfx.find_element(
                                By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[3]/div/div[5]/div[3]/div[2]/div[{}]".format(str(i)))
                            time.sleep(3)
                            fh = open("names.text", "w")
                            # fh.write(names.text)
                            fh.write(names.text.lower())
                            fh.close()
                            file = open("names.text", "r").read()
                            text = [line for line in file.splitlines()]
                            sheet = Data.ClassData_Mygo(text, willaya, sheet)
                        except:
                            pass

            except:
                pass
            continue
except:
    pass

df = pd.DataFrame(sheet, columns=["names", "prix"])
df.to_csv(f'./comparison/MyGo{Now}.csv', index=False, header=False)

time.sleep(3)
driverfx.close()

from asyncio import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import xlsxwriter
import spacy
from spacy.lang.fr import French
# from __future__ import unicode_literals
import numpy as np
from DataClass import Data
from nltk.tokenize import sent_tokenize
import pandas as pd
from thefuzz import fuzz, process
from os import getenv, path
import dotenv
import datetime

Now = datetime.datetime.now()


nlp = spacy.load("fr_core_news_sm")
willayas = getenv('willayas')
willaya = willayas[0]

sheet = np.array([["names", "prix"]])
date_start = input(str("start (day/monthe/year) : "))
date_finish = input(str("finish (day/monthe/year) : "))


# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options, executable_path="/Users/mac/Desktop/iprobooking/code/chromedriver/chromedrivere")

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(
    options=options, executable_path="../chromedriver/geckodriver")


clicngousername = getenv('clicngo_username')
clicngopassword = getenv('clicngo_password')

hotellist = []
priceslist = []

driver.get("https://beta.clicngo.biz")
time.sleep(10)

user = driver.find_element(By.ID, "TextBox_Login")
time.sleep(4)
user.send_keys(clicngousername)
time.sleep(4)
passw = driver.find_element(By.ID, "TextBox_Password")
time.sleep(4)
passw.send_keys(clicngopassword)
time.sleep(4)
driver.find_element(By.XPATH, "//*[@id='Button_Login']").click()
time.sleep(10)
hotelbutt = driver.find_element(
    By.XPATH, "//*[@class='divshortcutbook']/div[2]")
time.sleep(4)
hotelbutt.click()

#########################################################################

citys = driver.find_elements(
    By.XPATH, "//div[@class='floatCultureLeft cr_cityWidth']")
time.sleep(4)
for city in citys:
    oldratio = int(90)
    butt = city.text.lower()
    ratio = int(fuzz.partial_ratio(butt, willaya))
    if ratio > oldratio:
        oldratio = ratio
        city.click()
        continue
    else:
        continue

dateArr = driver.find_element(By.XPATH, "//input[@id='TextBox_ArrivalDate']")
dateArr.send_keys(Keys.CONTROL + 'a')
dateArr.clear()
dateArr.send_keys(date_start)
dateArr.send_keys(Keys.ENTER)

time.sleep(2)

dateDep = driver.find_element(By.XPATH, "//input[@id='TextBox_DepartureDate']")
dateDep.send_keys(Keys.CONTROL + 'a')
dateDep.clear()
dateDep.send_keys(date_finish)
dateDep.send_keys(Keys.ENTER)

hotelbutt = driver.find_element(
    By.XPATH, "//input[@class='cr_button-book HtlwwButtonSearch']")
time.sleep(2)
hotelbutt.click()
time.sleep(20)
names = driver.find_elements(
    By.XPATH, "//*[@class='htlwwHotelDescription']/div/div/a")
for name in names:
    time.sleep(2)
    hotellist.append(name.text.lower())
time.sleep(2)
prices = driver.find_elements(By.XPATH, "//span[@class='priceContent']")
for price in prices:
    time.sleep(2)
    priceslist.append(price.text)


l = driver.find_elements(
    By.XPATH, "//tr[@class='cr_Grid1UnSelectedHeaderItem pagination']/td/a")
el = (len(l))
pages = list(range(1, el+1))
for i in pages:
    time.sleep(10)
    NextButt = driver.find_element(
        By.XPATH, "//tr[@class='cr_Grid1UnSelectedHeaderItem pagination']/td/a[{}]".format(str(i)))
    time.sleep(3)
    NextButt.click()
    time.sleep(10)
    names = driver.find_elements(
        By.XPATH, "//*[@class='htlwwHotelDescription']/div/div/a")
    for name in names:
        time.sleep(2)
        hotellist.append(name.text.lower())
    time.sleep(2)
    prices = driver.find_elements(By.XPATH, "//span[@class='priceContent']")
    for price in prices:
        time.sleep(2)
        priceslist.append(price.text)

time.sleep(2)
willayas = willayas[1:]
time.sleep(3)
try:
    for willaya in willayas:
        time.sleep(2)
        modifybut = driver.find_element(
            By.XPATH, "//*[@id='Button_Back_Bottom']")
        time.sleep(2)
        modifybut.click()

        citys = driver.find_elements(
            By.XPATH, "//div[@class='floatCultureLeft cr_cityWidth']")
        time.sleep(4)
        for city in citys:
            oldratio = int(90)
            butt = city.text.lower()
            ratio = int(fuzz.partial_ratio(butt, willaya))
            if ratio > oldratio:
                oldratio = ratio
                city.click()
                continue
            else:
                continue

        dateArr = driver.find_element(
            By.XPATH, "//input[@id='TextBox_ArrivalDate']")
        dateArr.send_keys(Keys.CONTROL + 'a')
        dateArr.clear()
        dateArr.send_keys(date_start)
        dateArr.send_keys(Keys.ENTER)

        time.sleep(2)

        dateDep = driver.find_element(
            By.XPATH, "//input[@id='TextBox_DepartureDate']")
        dateDep.send_keys(Keys.CONTROL + 'a')
        dateDep.clear()
        dateDep.send_keys(date_finish)
        dateDep.send_keys(Keys.ENTER)

        hotelbutt = driver.find_element(
            By.XPATH, "//input[@class='cr_button-book HtlwwButtonSearch']")
        time.sleep(2)
        hotelbutt.click()
        time.sleep(20)
        names = driver.find_elements(
            By.XPATH, "//*[@class='htlwwHotelDescription']/div/div/a")
        time.sleep(2)
        for name in names:
            time.sleep(2)
            hotellist.append(name.text.lower())
        time.sleep(2)
        prices = driver.find_elements(
            By.XPATH, "//span[@class='priceContent']")
        time.sleep(2)
        for price in prices:
            time.sleep(2)
            priceslist.append(price.text)

        l = driver.find_elements(
            By.XPATH, "//tr[@class='cr_Grid1UnSelectedHeaderItem pagination']/td/a")
        el = (len(l))
        pages = list(range(1, el+1))
        for i in pages:
            time.sleep(10)
            NextButt = driver.find_element(
                By.XPATH, "//tr[@class='cr_Grid1UnSelectedHeaderItem pagination']/td/a[{}]".format(str(i)))
            time.sleep(3)
            NextButt.click()
            time.sleep(10)
            names = driver.find_elements(
                By.XPATH, "//*[@class='htlwwHotelDescription']/div/div/a")
            time.sleep(2)
            for name in names:
                time.sleep(2)
                hotellist.append(name.text.lower())
                time.sleep(2)

            prices = driver.find_elements(
                By.XPATH, "//span[@class='priceContent']")
            time.sleep(2)
            for price in prices:
                time.sleep(2)
                priceslist.append(price.text)


except:
    pass


time.sleep(7)
print(len(hotellist), len(priceslist))
a = {"names": hotellist, "prix": priceslist}
df = pd.DataFrame.from_dict(a, orient='index')
df = df.transpose()
df.to_csv(f'./comparison/clicngo{Now}.csv', index=False, header=False)

time.sleep(3)
driver.close()

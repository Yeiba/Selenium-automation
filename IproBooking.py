
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
from os import getenv, path
import dotenv


nlp = spacy.load("fr_core_news_sm")
willayas = getenv('willayas')
willaya = willayas[0]

sheet = np.array([["names", "prix"]])
monthe = input(str("Month: "))
day_start = input(str("day start: "))
nights = input(str("nights: "))


# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options, executable_path="/Users/mac/Desktop/iprobooking/code/chromedriver/chromedrivere")

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(
    options=options, executable_path="../code/chromedriver/geckodriver")

email = getenv('ipro_email')
username = getenv('ipro_username')
password = getenv('ipro_password')


driver.get("https://www.ipro-booking.com/home2")
driver.find_element(By.ID, "emailagence").send_keys(email)
sleep(1)
driver.find_element(By.ID, "username").send_keys(username)
sleep(1)
driver.find_element(By.ID, "password").send_keys(password)
sleep(1)
sub = driver.find_element(
    By.XPATH, "/html/body/section/div[2]/div/div/div/div/div/div[2]/div/form/div/div[5]/button")
time.sleep(2)
sub.click()
time.sleep(2)
driver.find_element(By.ID, "property-title").send_keys(willaya)
time.sleep(3)
# driver.find_element(By.ID, "property-title").send_keys(Keys.ARROW_DOWN)
driver.find_element(By.ID, "property-title").send_keys(Keys.ENTER)
time.sleep(3)

driver.find_element(
    By.XPATH, "/html/body/div[2]/div[3]/div[2]/div/div/div/div/div[2]/form/div/div[1]/div[1]/div[2]/div/div/input").click()
time.sleep(2)
driver.find_element(
    By.XPATH, "/html/body/div[5]/div[1]/table/thead/tr[1]/th[2]").click()
time.sleep(2)
monthes = driver.find_element(
    By.XPATH, "/html/body/div[5]/div[2]/table/tbody/tr/td/span[{}]".format(str(monthe))).click()
time.sleep(2)
dayes = driver.find_elements(By.XPATH, "//td[@class='day']")
for day in dayes:
    try:
        if day.text == day_start:
            day.click()
            time.sleep(1)
        else:
            continue
    except:
        pass
    continue

time.sleep(5)
nighS = driver.find_element(
    By.XPATH, "/html/body/div[2]/div[3]/div[2]/div/div/div/div/div[2]/form/div/div[1]/div[1]/div[4]/div/div/input")
time.sleep(3)
nighS.click()
time.sleep(3)
nighS.send_keys(Keys.CONTROL + 'a')
time.sleep(3)
nighS.clear()
time.sleep(3)
nighS.send_keys(nights)
time.sleep(3)
searchButt = driver.find_element(
    By.XPATH, "/html/body/div[2]/div[3]/div[2]/div/div/div/div/div[2]/form/div/div[2]/div/div/div/button")
time.sleep(3)
searchButt.click()

time.sleep(30)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# driver.execute_script("window.scrollTo(0, Y)")
time.sleep(3)
l = driver.find_elements(By.CLASS_NAME, "hotel_div")
el = (len(l))
ContH = list(range(1, el+1))
for i in ContH:
    time.sleep(2)
    names = driver.find_element(
        By.XPATH, "/html/body/div[2]/section/div/div/div[3]/div/div[2]/div[{}]".format(str(i)))
    time.sleep(3)
    fh = open("names.text", "w")
    fh.write(names.text.lower())
    fh.close()
    file = open("names.text", "r").read()
    text = [line for line in file.splitlines()]
    sheet = Data.ClassData_Ipro(text, sheet)

time.sleep(2)
willayas = willayas[1:]
time.sleep(3)
try:
    for willaya in willayas:

        time.sleep(2)
        plusbutt = driver.find_element(
            By.XPATH, "/html/body/div[2]/div[4]/div/div[1]/div[1]/label/i")
        time.sleep(2)
        plusbutt.click()
        time.sleep(3)
        searchbar = driver.find_element(By.ID, "property-title")
        time.sleep(3)
        searchbar.send_keys(Keys.CONTROL + 'a')
        time.sleep(3)
        searchbar.clear()
        time.sleep(3)
        searchbar.send_keys(willaya)
        time.sleep(3)
        searchbar.send_keys(Keys.ENTER)
        time.sleep(3)
        serch = driver.find_element(
            By.XPATH, "/html/body/div[2]/div[4]/div/div[2]/div/form/div/div[3]/div/div/button")
        time.sleep(3)
        serch.click()
        time.sleep(30)
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        l = driver.find_elements(By.CLASS_NAME, "hotel_div")
        time.sleep(2)
        el = (len(l))
        ContH = list(range(1, el+1))
        for i in ContH:
            time.sleep(2)
            names = driver.find_element(
                By.XPATH, "/html/body/div[2]/section/div/div/div[3]/div/div[2]/div[{}]".format(str(i)))
            time.sleep(3)
            fh = open("names.text", "w")
            fh.write(names.text.lower())
            # fh.write(names.text)
            fh.close()
            file = open("names.text", "r").read()
            text = [line for line in file.splitlines()]
            sheet = Data.ClassData_Ipro(text, sheet)
except:
    pass


df = pd.DataFrame(sheet, columns=["names", "prix"])
df.to_csv('./ccomparison/Iprobooking.csv', index=False, header=False)

time.sleep(3)
driver.close()

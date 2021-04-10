from selenium import webdriver
import os
from bs4 import BeautifulSoup
import time
import urllib.parse
import urllib.request
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--disable-notifications")
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-sh-usage")
def initDriver():
    #driver = webdriver.Chrome()
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=op)
    driver.get("https://facebook.com")
    return driver
def layMp3(url):
    #if(chuoi.strip()==""): return False,"Không biết gì hết"
    #try:
    #url = "http://www.google.com.vn/search?hl=vi&safe=off&tbm=isch&q="+ urllib.parse.quote(chuoi)
    url2 = "https://www.klickaud.co/"
    driver2 = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=op)
    driver2.get(url2)
    htmlSource = driver2.page_source
    soup = BeautifulSoup(htmlSource, 'html.parser')
    print(soup.prettify())
    driver2.close()
    #return soup.prettify()
def layMp32(url):
    #if(chuoi.strip()==""): return False,"Không biết gì hết"
    #try:
    #url = "http://www.google.com.vn/search?hl=vi&safe=off&tbm=isch&q="+ urllib.parse.quote(chuoi)
    url2 = "https://sclouddownloader.net/"
    driver2 = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=op)
    driver2.get(url2)
    htmlSource = driver2.page_source
    soup = BeautifulSoup(htmlSource, 'html.parser')
    print(soup.prettify())
    driver2.close()
def layMp33(url):
    #if(chuoi.strip()==""): return False,"Không biết gì hết"
    #try:
    #url = "http://www.google.com.vn/search?hl=vi&safe=off&tbm=isch&q="+ urllib.parse.quote(chuoi)
    url2 = "https://soundcloudmp3.org/"
    driver2 = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=op)
    driver2.get(url2)
    htmlSource = driver2.page_source
    soup = BeautifulSoup(htmlSource, 'html.parser')
    print(soup.prettify())
    driver2.close()
def layMp34(url):
    #if(chuoi.strip()==""): return False,"Không biết gì hết"
    #try:
    #url = "http://www.google.com.vn/search?hl=vi&safe=off&tbm=isch&q="+ urllib.parse.quote(chuoi)
    url2 = "https://soundcloudtomp3.co/"
    driver2 = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=op)
    driver2.get(url2)
    htmlSource = driver2.page_source
    soup = BeautifulSoup(htmlSource, 'html.parser')
    print(soup.prettify())
    driver2.close()
def layMp35(url):
    #if(chuoi.strip()==""): return False,"Không biết gì hết"
    #try:
    #url = "http://www.google.com.vn/search?hl=vi&safe=off&tbm=isch&q="+ urllib.parse.quote(chuoi)
    url2 = "https://sctomp3.net/fr/"
    driver2 = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=op)
    driver2.get(url2)
    htmlSource = driver2.page_source
    soup = BeautifulSoup(htmlSource, 'html.parser')
    print(soup.prettify())
    driver2.close()
def layMp36(url):
    #if(chuoi.strip()==""): return False,"Không biết gì hết"
    #try:
    #url = "http://www.google.com.vn/search?hl=vi&safe=off&tbm=isch&q="+ urllib.parse.quote(chuoi)
    url2 = "https://soundcloudtomp3.app/"
    driver2 = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=op)
    driver2.get(url2)
    htmlSource = driver2.page_source
    soup = BeautifulSoup(htmlSource, 'html.parser')
    print(soup.prettify())
    driver2.close()
        # song_input = driver2.find_elements(By.XPATH,"//form/input")
        # song_input[0].send_keys(url)
        # song_input[0].send_keys(Keys.ENTER)
        # htmlSource = driver2.page_source
        # soup = BeautifulSoup(htmlSource, 'html.parser')
        # t = soup.find("td",{"class":"no-mobile1"}).find("a")
        # linkdown = t.get("href")
        # linkfile = os.getcwd()+"/nhac.mp3"
        # urllib.request.urlretrieve(linkdown,linkfile)
        # driver2.close()
        # return True,linkfile
    # except:
    #     driver2.close()
    #     return False,"Không thấy ảnh"

try:
    layMp3("https://soundcloud.com/den1305/den-x-justatee-di-ve-nha")
    print("soundclound 1 ok")
except:
    print("soundclound 1 err")
try:
    layMp32("https://soundcloud.com/den1305/den-x-justatee-di-ve-nha")
    print("soundclound 2 ok")
except:
    print("soundclound 2 err")
try:
    layMp33("https://soundcloud.com/den1305/den-x-justatee-di-ve-nha")
    print("soundclound 3 ok")
except:
    print("soundclound 3 err")
try:
    layMp34("https://soundcloud.com/den1305/den-x-justatee-di-ve-nha")
    print("soundclound 4 ok")
except:
    print("soundclound 4 err")
try:
    layMp35("https://soundcloud.com/den1305/den-x-justatee-di-ve-nha")
    print("soundclound 5 ok")
except:
    print("soundclound 5 err")
try:
    layMp36("https://soundcloud.com/den1305/den-x-justatee-di-ve-nha")
    print("soundclound 6 ok")
except:
    print("soundclound 6 err")

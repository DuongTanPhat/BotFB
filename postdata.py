from selenium import webdriver
import os
from bs4 import BeautifulSoup
import time
import urllib.parse
import urllib.request
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--disable-notifications")
# op.add_argument("--headless")
# op.add_argument("--no-sandbox")
# op.add_argument("--disable-dev-sh-usage")

def initDriver():
    #driver = webdriver.Chrome()
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=op)
    driver.get("https://facebook.com")
    return driver


def loginFacebookByCookie(cookie,driver):
    script = 'javascript:void(function(){ function setCookie(t) { var list = t.split("; "); console.log(list); for (var i = list.length - 1; i >= 0; i--) { var cname = list[i].split("=")[0]; var cvalue = list[i].split("=")[1]; var d = new Date(); d.setTime(d.getTime() + (7*24*60*60*1000)); var expires = ";domain=.facebook.com;expires="+ d.toUTCString(); document.cookie = cname + "=" + cvalue + "; " + expires; } } function hex2a(hex) { var str = ""; for (var i = 0; i < hex.length; i += 2) { var v = parseInt(hex.substr(i, 2), 16); if (v) str += String.fromCharCode(v); } return str; } setCookie("' + cookie + '"); location.href = "https://facebook.com"; })();'
    driver.execute_script(script)
def taisoundtext(chuoi):
    try:
        url2 = "https://soundoftext.com/"
        driver2 = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=op)
        driver2.get(url2)
        select = Select(driver2.find_element(By.TAG_NAME,"select"))
        select.select_by_value("vi-VN")
        text_input = driver2.find_elements(By.TAG_NAME,"textarea")
        text_input[0].send_keys(chuoi)
        button_input = driver2.find_elements(By.TAG_NAME,"input")
        button_input[0].click()
        time.sleep(2)
        htmlSource = driver2.page_source
        soup = BeautifulSoup(htmlSource, 'html.parser')
        t = soup.find("audio")
        linkdown = t.get("src")
        linkfile = os.getcwd()+"/voice.mp3"
        urllib.request.urlretrieve(linkdown,linkfile)
        driver2.close()
        return True,linkfile
    except:
        driver2.close()
        return False,"Không thấy ảnh"
driver=initDriver()
cookie = "Cookie: sb=-wcMYAhDOamLWDwHwY77XZou; wd=1536x754; datr=-wcMYPDx3VrPiedJg0g_b1TN; dpr=1.25; c_user=100062381025689; xs=39%3AGpT3KcyoUfiAdw%3A2%3A1611401222%3A-1%3A-1; fr=1rKiw7Qi2YOI9bgQm.AWXVOPG57-XE1fVyBjzcGuVwqFE.BgDAf7.5E.AAA.0.0.BgDAgG.AWV93ws_F9M; spin=r.1003214175_b.trunk_t.1611401223_s.1_v.2_"
#cookie = "Cookie: sb=AP4LYEGhRZihfZIzWg30w6WV; wd=1536x754; datr=AP4LYL6HzeVxbLEvd2e2ODmw; dpr=1.25; c_user=100062820608198; xs=4%3AgTXaUF7LuM_n9w%3A2%3A1611398698%3A-1%3A-1; fr=1uja14p0n1n4m47LZ.AWXmI1TgX1a3lF84PPqaafgRr50.BgC_4A.cg.AAA.0.0.BgC_4q.AWUyR_lWlWA; spin=r.1003214161_b.trunk_t.1611398700_s.1_v.2_"
#cookie ="Cookie: sb=RdkgYBNpxWuwGiIg-cYqPuLH; wd=1536x754; datr=RdkgYDu8QTumz7TnPO7U1pEF; dpr=1.25; c_user=100062820608198; xs=6%3Af9RhE9XkGyIXEw%3A2%3A1612765693%3A5602%3A12124; fr=1dfHNSUpS1dfj9SHL.AWXm3pDDs4cmxVj6WfdKBln9z1c.BgINlF.Uh.AAA.0.0.BgINn9.AWUHso4hzfg; spin=r.1003277527_b.trunk_t.1612765694_s.1_v.2_"
loginFacebookByCookie(cookie,driver)

def checkMess():
    htmlSource = driver.page_source
    soup = BeautifulSoup(htmlSource, 'html.parser')
    section = soup.find("section")
    listtext = section.find_all("span")
    for texts in listtext:
        tx = texts.text
        url = texts.parent.previous_sibling.contents[0].get("href")
        if(tx.startswith('.')):
            numstart = url.find("tid=") + 4
            numend=url.find("&")
            cid = url[numstart:numend]
            return 1,tx.lstrip('.'),cid
        elif(tx.startswith(',')):
            numstart = url.find("tid=") + 4
            numend=url.find("&")
            cid = url[numstart:numend]
            return 2,tx.lstrip(','),cid
        elif(tx.startswith('>')):
            numstart = url.find("tid=") + 4
            numend=url.find("&")
            cid = url[numstart:numend]
            return 3,tx.lstrip('>'),cid
        elif(tx.startswith('<')):
            numstart = url.find("tid=") + 4
            numend=url.find("&")
            cid = url[numstart:numend]
            return 4,tx.lstrip('<'),cid
    return 0,"",""
def layMp3(url):
    #if(chuoi.strip()==""): return False,"Không biết gì hết"
    try:
        url2 = "https://www.klickaud.co/"
        driver2 = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=op)
        driver2.get(url2)
        song_input = driver2.find_elements(By.XPATH,"//form/input")
        song_input[0].send_keys(url)
        song_input[0].send_keys(Keys.ENTER)
        htmlSource = driver2.page_source
        soup = BeautifulSoup(htmlSource, 'html.parser')
        t = soup.find("td",{"class":"no-mobile1"}).find("a")
        linkdown = t.get("href")
        linkfile = os.getcwd()+"/nhac.mp3"
        urllib.request.urlretrieve(linkdown,linkfile)
        driver2.close()
        return True,linkfile
    except:
        driver2.close()
        return False,"Không thấy ảnh"
def sendMp3(linkfile,cid):
    cidlist = cid.split(".")
    driver2 = initDriver()
    loginFacebookByCookie(cookie,driver2)
    if(cidlist[2].find("%3A")!=-1):
        cidlist2 = cidlist[2].split("%3A")
        cidlist[2] = cidlist2[0]
    driver2.get('https://www.facebook.com/messages/t/'+cidlist[2])
    time.sleep(2)
    htmlSource = driver2.page_source
    soup = BeautifulSoup(htmlSource, 'html.parser')
    file_input = driver2.find_elements(By.XPATH,"//form[input/@type='submit']/div/div[2]/div/input[2]")[0]
    file_input.send_keys(linkfile)
    file_input2 = driver2.find_elements(By.XPATH,"//form[input/@type='submit']/div/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div")[0]
    file_input2.send_keys(Keys.ENTER)
    check,a,b = checkMess()
    while(check==3 or check==4):
        time.sleep(4)
        driver.get('https://mbasic.facebook.com/messages/')
        check,a,b = checkMess()
    driver2.close()
# def convImgtoText(linkfile):
#     img = cv2.imread(linkfile, 0)
#     text = pytesseract.image_to_string(img,config="--psm 11")
#     return text

def layImgChat(cid):
    driver.get('https://mbasic.facebook.com/messages/read/?tid='+cid)
    htmlSource = driver.page_source
    soup = BeautifulSoup(htmlSource, 'html.parser')
    t = soup.find_all("div",attrs={"id":"fua"})
    linkfile = os.getcwd()+"/imagechat.jpg"
    
    try:
        linkimgtemp = t[0].find("img").get("src")
        urllib.request.urlretrieve(linkimgtemp,linkfile)
        return True,linkfile
    except:
        return False,"Không thấy ảnh"
def sendMessage(message,cid):
    #driver.get('https://mbasic.facebook.com/messages/compose/?ids[0]=' + '100004966056852')
    #driver.get('https://mbasic.facebook.com/messages/read/?tid=cid.g.1474408102624963')
    driver.get('https://mbasic.facebook.com/messages/read/?tid='+cid)
    
    text_input = driver.find_elements_by_tag_name('textarea')
    if (len(text_input) > 0):
        text_input[0].send_keys(message)
        driver.find_element_by_xpath('//*[@id="composer_form"]/table/tbody/tr/td[2]/input').click()
def layKetquaGoogle(chuoi):
    if(chuoi.strip()==""): return "Không biết gì hết"
    url = "http://www.google.com.vn/search?hl=vi&safe=off&q="+ urllib.parse.quote(chuoi)
    driver2 = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=op)
    driver2.get(url)
    htmlSource = driver2.page_source
    soup = BeautifulSoup(htmlSource, 'html.parser')
    t = soup.find("div",attrs={"class": "card-section"})
    try:
        if(len(t)!=0):
            a = t.find_all("span",attrs={"id": "cwos"})
        if(len(a)!=0):
            linkSend = a[0].text
            driver2.close()
            return(linkSend)
        else:
            a=soup.find_all("g-card")
            if(len(a)!=0):
                linkSend = a[0].find("div",attrs={"role": "heading"}).text
                driver2.close()
                return(linkSend)
            else:
                a=soup.find_all("div",attrs={"class": "dDoNo"})
                if(len(a)!=0):
                    linkSend = a[0].previous_sibling.text+" "
                    linkSend += a[0].text
                    driver2.close()
                    return(linkSend)
    except:
        a = 0
    g = soup.find_all("div",attrs={"id": "rhs"})
    if len(g[0].find_all("div"))==0:
        s = soup.find_all("div",attrs={"class": "g"})
        lin = s[0].find_all("a")
        i=0
        while(lin[i].get("href").find("http")!=0):
            i+=1
        linkSend = lin[i].get("href")
        driver2.close()
        return(linkSend)
    try:
        s = g[0].contents[2]
        if(len(list(s.children))>1):
            s=s.contents[1]
        else:
            s=s.contents[0].contents[0]
        listrow = s.find_all("div",{"class":"mod"})
        i = 0
        listrow = list(filter(lambda l : len(l["class"])==1, listrow))
        smes = ""
        for tx in listrow:
            if tx.text != "":
                smes += tx.text +"\n"
        driver2.close()
        print(smes)
        return(smes)
    except:
        s = soup.find_all("div",attrs={"class": "g"})
        lin = s[0].find_all("a")
        i=0
        while(lin[i].get("href").find("http")!=0):
            i+=1
        linkSend = lin[i].get("href")
        driver2.close()
        return(linkSend)

def layImgGoogle(chuoi):
    if(chuoi.strip()==""): return False,"Không biết gì hết"
    url = "http://www.google.com.vn/search?hl=vi&safe=off&tbm=isch&q="+ urllib.parse.quote(chuoi)
    driver2 = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=op)
    driver2.get(url)
    htmlSource = driver2.page_source
    soup = BeautifulSoup(htmlSource, 'html.parser')
    t = soup.find_all("img")
    linkimgtemp = t[0].get("src")
    # while(i<len(t)):
    codeimg = t[0].parent.parent.parent.get("data-tbnid")
    driver2.get(url+"#imgrc="+codeimg)
        #time.sleep(4)
    htmlSource = driver2.page_source
    soup = BeautifulSoup(htmlSource, 'html.parser')
    listu = soup.find("a",attrs={"role": "link"})
    linkimg = listu.contents[0].get("src")
    try:
        linkfile = os.getcwd()+"/image.jpg"
        urllib.request.urlretrieve(linkimg,linkfile)
        driver2.close()
        return True,linkfile
    except:
        try:
            linkfile = os.getcwd()+"/image.jpg"
            urllib.request.urlretrieve(linkimgtemp,linkfile)
            driver2.close()
            return True,linkfile
        except:
            driver2.close()
            return False,"Không thấy ảnh"

def sendImg(linkfile,cid):
    url = "https://mbasic.facebook.com/messages/photo/?tids[0]="+cid+"&cancel=https://mbasic.facebook.com/messages/read/?tid="+cid    
    driver.get(url)
    htmlSource = driver.page_source
    soup = BeautifulSoup(htmlSource, 'html.parser')
    t = soup.find_all("input",attrs={'type':'file'})
    uploadBtn = driver.find_element(By.NAME, "file1")
    uploadBtn.send_keys(linkfile)
    driver.find_element_by_xpath('//form/div[2]/input').click()


# layImgGoogle("hentai2")
# layKetquaGoogle("trấn thành")
# layKetquaGoogle("đồng là gì")

# layKetquaGoogle("yui hirasawa")
# layKetquaGoogle("emiri suzuhara")


while True:
    try:
        time.sleep(4)
        driver.get('https://mbasic.facebook.com/messages/')
        check,chuoi,cid = checkMess()
        if(check==1):
            mes = layKetquaGoogle(chuoi)
            sendMessage(mes,cid)
        elif(check==2):
            check2,linkfile = layImgGoogle(chuoi)
            if(check2==True):
                sendImg(linkfile,cid)
            else:
                sendMessage(linkfile,cid)
        elif(check==3):
            mes = layKetquaGoogle(chuoi+" soundcloud.com")
            check2,linkfile = layMp3(mes)
            if check2 == True:
                sendMp3(linkfile,cid)
        elif(check==4):
            check2,linkfile = taisoundtext(chuoi)
            if check2==True:
                sendMp3(linkfile,cid)
    except:
        print('err')
driver.close()
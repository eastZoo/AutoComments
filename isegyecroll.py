import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time 
import pyperclip

#드라이버 로딩 
driver = webdriver.Chrome('./chromedriver.exe') 
driver.maximize_window() # For maximizing window

##사용할 변수 선언 
##네이버 로그인 주소 

url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com' 
uid = 'dongju010' 
upw = 'shin20171537' 

#네이버 로그인 페이지로 이동 
driver.get(url) 
time.sleep(2) #로딩 대기 

#아이디 입력폼 
tag_id = driver.find_element_by_name('id') 

#패스워드 입력폼 
tag_pw = driver.find_element_by_name('pw') 

# id 입력 
# 입력폼 클릭 -> paperclip에 선언한 uid 내용 복사 -> 붙여넣기 
tag_id.click() 
pyperclip.copy(uid) 
tag_id.send_keys(Keys.CONTROL, 'v') 
time.sleep(1) 

# pw 입력 
# 입력폼 클릭 -> paperclip에 선언한 upw 내용 복사 -> 붙여넣기 
tag_pw.click() 
pyperclip.copy(upw) 
tag_pw.send_keys(Keys.CONTROL, 'v') 
time.sleep(1) 

#로그인 버튼 클릭 

login_btn = driver.find_element_by_id('log.login') 
login_btn.click() 

# btn_cancel = driver.find_element_by_id('new.dontsave') 
# btn_cancel.click() 

time.sleep(2)

# 내가 검색하려는 카페 주소 입력하기
baseurl = 'https://cafe.naver.com/steamindiegame/'
driver.get(baseurl)

# 이세돌 팬아트 게시판 클릭
ise_pan = driver.find_element_by_id('menuLink344') 
ise_pan.click()

time.sleep(3)
element = driver.find_element_by_id("cafe_main") #iframe 태그 엘리먼트 찾기
driver.switch_to.frame(element) #프레임 이동
time.sleep(3)

isegye_board = driver.find_element_by_xpath('//*[@id="main-area"]/ul[1]/li[9]')
isegye_board.click()

count = 1
for i in range(30):
    time.sleep(2)
    #스티커 버튼
    icon_button = driver.find_element_by_class_name('button_sticker') 
    icon_button.click()

    # 댓글 스티커 선택 버튼
    if count%3 == 0:
        time.sleep(1)
        try:
            sticker = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[5]/div[2]/div[2]/div[1]/div/div/div/div/ul/li[1]/div/ul/li[4]') 
            sticker.click()
            count+=1
        except:
            sticker = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[6]/div[2]/div[2]/div[1]/div/div/div/div/ul/li[1]/div/ul/li[4]') 
            sticker.click()
            count+=1
    elif count%3 == 1:
        time.sleep(1)
        try:
            sticker = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[5]/div[2]/div[2]/div[1]/div/div/div/div/ul/li[1]/div/ul/li[7]') 
            sticker.click()
            count+=1
        except:
            sticker = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[6]/div[2]/div[2]/div[1]/div/div/div/div/ul/li[1]/div/ul/li[7]') 
            sticker.click()
            count+=1
    elif count%3 == 2:
        time.sleep(1)
        try:
            sticker = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[5]/div[2]/div[2]/div[1]/div/div/div/div/ul/li[1]/div/ul/li[15]') 
            sticker.click()
            count+=1
        except:
            sticker = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[6]/div[2]/div[2]/div[1]/div/div/div/div/ul/li[1]/div/ul/li[15]') 
            sticker.click()
            count+=1

    # 댓글 확인버튼
    time.sleep(1)
    try:
        sticker = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[5]/div[2]/div[2]/div[2]/a') 
        sticker.click()
    except:
        sticker = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[6]/div[2]/div[2]/div[2]/a') 
        sticker.click()
    time.sleep(2)
    # 다음글
    next = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/a[2]') 
    next.click()
    # //*[@id="app"]/div/div/div[1]/div[2]/a[2] 다음글
    # //*[@id="app"]/div/div/div[1]/div[2]/a[1] 이전글
driver.close()
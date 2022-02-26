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

btn_cancel = driver.find_element_by_id('new.dontsave') 
btn_cancel.click() 

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

isegye_board = driver.find_element_by_xpath('//*[@id="main-area"]/ul[1]/li[1]')
isegye_board.click()

# li = isegye_board.find_elements_by_tag_name('li')
# aTag = li[0].find_element_by_tag_name('a')
# print(aTag)
# href = aTag.get_attribute('href')
# href.click()

# &search.menuid = : 게시판 번호
# &search.page = : 데이터 수집 할 페이지 번호
# &userDisplay = 50 : 한 페이지에 보여질 게시글 수

# clubid = 카페 클럽 ID 번호 입력
# menuid = 메뉴 ID 번호 입력
# pageNum = 1
# userDisplay = 50

# driver.get(
#     baseurl + 'ArticleList.nhn?search.clubid=' + str(clubid) + '&search.menuid=' + str(menuid) + '&search.page=' + str(
#         pageNum) + '&userDisplay=' + str(userDisplay))
        
# # iframe으로 접근
# driver.switch_to.frame('cafe_main') 


# soup = bs(driver.page_source, 'html.parser')

# print(str(soup))

# soup = soup.find_all(class_='article-board m-tcol-c')[1]

# # 네이버 카페 구조 확인후 게시글 내용만 가저오기

# # datas = soup.find_all('td', class_ = 'td_article')

# datas = soup.find_all(class_='td_article')
# dates = soup.find_all(class_='td_date')



# for data in datas:
#     article_title = data.find(class_='article')
#     link = article_title.get('href')
#     article_title = article_title.get_text().strip()

#     print(article_title)
#     print(baseurl + link)

# 	# 인코딩은 utf-8이 좋아 보임
    
#     f = open('craw.csv', 'a+', newline='',encoding='utf-8') 
   
#     wr = csv.writer(f)
#     wr.writerow([article_title, baseurl + link])
#     f.close()

# print('종료')


# driver.close()
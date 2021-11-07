from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import schedule

def daily_excel_maker(a):
    driver = webdriver.Chrome('C:/Users/yaegun/Desktop/asdf/chromedriver')
    url = 'https://www.bigkinds.or.kr/v2/news/index.do'
    driver.get(url)
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("")
    time.sleep(3)
    # 로그인
    driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div/button[1]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="login-user-id"]').send_keys('yaej@naver.com')
    driver.find_element_by_xpath('//*[@id="login-user-password"]').send_keys('osa_health2')
    driver.find_element_by_xpath('//*[@id="login-btn"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="collapse-step-1-body"]/div[3]/div/div[1]/div[1]/a').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="srch-tab1"]/div/div[1]/span[1]/label').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="collapse-step-1-body"]/div[3]/div/div[3]/div[1]/a').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="andKeyword1"]').send_keys(a)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="detailSrch1"]/div[7]/div/button[2]').click()
    time.sleep(1)
    # driver.execute_script("window.scrollTo(0,1998);")
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="collapse-step-3"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="analytics-data-download"]/div[3]/button/i').click()
    time.sleep(15)

    # 저장받는 경로는 C:\Users\yaegun\Desktop\Downloads
    # 저장받은 파일 이름은
    #NewsResult_2021mmdd - 2021mmdd     #질병
    #NewsResult_2021mmdd - 2021mmdd(1)  #건강
    #NewsResult_2021mmdd - 2021mmdd(2)  #코로나나for a in today_word_list:
    ##schedule.every().day.at("23:58").do(daily_excel_maker(a))

today_word_list = ['질병', '건강', '코로나']

for a in today_word_list:
    b = daily_excel_maker(a)
    b
    time.sleep(2)





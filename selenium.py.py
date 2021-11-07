from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('C:/Users/yaegun/Desktop/asdf/chromedriver')
url = 'https://www.bigkinds.or.kr/v2/news/index.do'
driver.get(url)
today_word_list = []
today_word_list.append('질병')

# options = webdriver.ChromeOptions()
# options.add_experimental_option("")
time.sleep(3)
#로그인
driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div/button[1]').click()
driver.find_element_by_xpath('//*[@id="login-user-id"]').send_keys('yaej@naver.com')
driver.find_element_by_xpath('//*[@id="login-user-password"]').send_keys('osa_health2')
driver.find_element_by_xpath('//*[@id="login-btn"]').click()
driver.find_element_by_xpath('//*[@id="collapse-step-1-body"]/div[3]/div/div[1]/div[1]/a').click()
driver.find_element_by_xpath('//*[@id="srch-tab1"]/div/div[1]/span[1]/label').click()
driver.find_element_by_xpath('//*[@id="collapse-step-1-body"]/div[3]/div/div[3]/div[1]/a').click()
driver.find_element_by_xpath('//*[@id="andKeyword1"]').send_keys(today_word_list[0])
driver.find_element_by_xpath('//*[@id="detailSrch1"]/div[7]/div/button[2]').click()
time.sleep(5)
# 특정 위치(좌표)까지만 내릴 경우

#driver.execute_script("window.scrollTo(0,1998);")
driver.find_element_by_xpath('//*[@id="collapse-step-3"]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="analytics-data-download"]/div[3]/button').click()
#저장받는 경로는 C:\Users\yaegun\Desktop\Downloads
#저장받은 파일 이름은 NewsResult_2021mmdd-2021mmdd
'''

driver.find_element_by_xpath('')
driver.find_element_by_xpath('')

'''
'''
driver.find_element_by_xpath('')
'''
'''
#뉴스 검색/분석
driver.find_element_by_xpath('//*[@id="header"]/div[2]/div[2]/div[1]/div/div[1]/div/ul/li[1]/a')
driver.find_element_by_xpath('//*[@id="header"]/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/ul/li[1]/a').click()
time.sleep(10)
#기간 지정
driver.find_element_by_xpath('//*[@id="collapse-step-1-body"]/div[3]/div/div[1]/div[1]/a').click()
driver.find_element_by_xpath('//*[@id="srch-tab1"]/div/div[1]/span[1]/label').click
time.sleep(10)
#통합 분류
driver.find_element_by_xpath('//*[@id="collapse-step-1-body"]/div[3]/div/div[2]/div[1]/a').click()
driver.find_element_by_xpath('//*[@id="srch-tab3"]/ul/li[3]/div/span[2]').click()
driver.find_element_by_xpath('//*[@id="srch-tab3"]/ul/li[3]/ul/li[1]/div/span[3]/label/span').click()
time.sleep(10)
#상세 검색
driver.find_element_by_xpath('//*[@id="collapse-step-1-body"]/div[3]/div/div[3]/div[1]/a').click()
#driver.find_element_by_xpath('//*[@id="andKeyword1"]').
driver.find_element_by_xpath('//*[@id="detailSrch1"]/div[7]/div/button[2]').click()
time.sleep(10)
#분석 결과 및 시각화
driver.find_element_by_xpath('//*[@id="collapse-step-3"]').click()
driver.find_element_by_xpath('//*[@id="analytics-preview-tab"]').click()
driver.find_element_by_xpath('//*[@id="analytics-data-download"]/div[3]/button').click()
time.sleep(10)
driver.quit()


'''
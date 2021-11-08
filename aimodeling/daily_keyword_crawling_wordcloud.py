from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import schedule
from wordcloud import WordCloud, STOPWORDS
from konlpy.tag import Okt
import pandas as pd
import nltk
from wordcloud import WordCloud, STOPWORDS
import numpy as np

def daily_excel_maker(a):
    driver = webdriver.Chrome('C:/Users/tlsgh/chromedriver')
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
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="collapse-step-3"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="analytics-data-download"]/div[3]/button/i').click()
    time.sleep(15)

    # 저장받는 경로는 C:\Users\yaegun\Desktop\Downloads
    # 저장받은 파일 이름은
    #NewsResult_2021mmdd - 2021mmdd     #질병
    #NewsResult_2021mmdd - 2021mmdd(1)  #건강
    #NewsResult_2021mmdd - 2021mmdd(2)  #코로나나

if __name__ == "__main__":
    # today_word_list = ['질병', '건강', '코로나']
    okt = Okt()
    # for a in today_word_list:
    #     daily_excel_maker(a)
    #     time.sleep(2)

    spwords = set(STOPWORDS)
    wl = ['등', '코로나', '것', '지난', '의', '이', '무엇', '원인', '후', '씨', '경우', '접종', '진자', '명', '기자', '세', '백신', '시작','기준', '수', '앵커', '확', '최근', '때문', '신규', '완료', '추가', '리포트', '단계', '지난', '관리', '코로나바이러스', '정부', '방송', '차','사람', '지역', '상황', '처음', '병원', '아스', '후', '날', '씨', '발생', '위해', '달', '은', '증', '사례', '이후', '화이자', '카','관련', '사망자', '예약', '얀', '지난', '당국', '중', '총', '확인', '전날', '를', '로', '텍스트', '연령', '지역', '확진', '모두', '증가','결과', '지난해', '의심', '생각', '관련', '추진단', '교수', '이상', '중', '가운데', '방역', '본주', '관리', '게시판', '집계', '대응','마스크', '사회', '지난달']
    for a in wl:
        spwords.add(a)

    url_list = ["C:/Users/tlsgh/Downloads/NewsResult_20211106-20211107.xlsx","C:/Users/tlsgh/Downloads/NewsResult_20211106-20211107 (1).xlsx","C:/Users/tlsgh/Downloads/NewsResult_20211106-20211107 (2).xlsx"]
    for idx, url in enumerate(url_list):
        temp = pd.read_excel(url)
        context = list(temp["본문"])
        noun_list = []
        wc = WordCloud(font_path='NanumGothic.ttf', background_color='white', width=512, height=512,
                       max_font_size=500, max_words=1000,stopwords=spwords)
        noun_list = []
        for text in context:
            os = okt.nouns(text)
            noun_list.append(os)
        noun_list = sum(noun_list,[])
        print(np.shape(noun_list))
        count_word = nltk.Text(noun_list)
        data = count_word.vocab().most_common(3000)
        wc.generate_from_frequencies(dict(data))
        wc.to_file("wordcloud_temp{}.jpg".format(idx))





#schedule.every().day.at("18:05").do(starting)
## d = schedule.every().day.at("18:03").do(starting)
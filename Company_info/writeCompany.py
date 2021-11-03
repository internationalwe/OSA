import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup
import csv



baseurl='https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query='
query = [
    'sk%ED%95%98%EC%9D%B4%EB%8B%89%EC%8A%A4', #sk하이닉스
    '%ED%83%9C%EC%98%81%EA%B1%B4%EC%84%A4', #태영건설
    '%ED%9C%A0%EB%9D%BC%EC%BD%94%EB%A6%AC%EC%95%84', #휠라코리아
    '%EC%97%94%EC%94%A8%EC%86%8C%ED%94%84%ED%8A%B8', #엔씨소프트
    '%EC%82%BC%EC%84%B1sdi', #삼성SDi
    'OCI', #oci
    'LG%ED%99%94%ED%95%99',#LG화학
    #'%EC%8B%A0%EC%84%B8%EA%B3%84', #신세계
    'LG', #LG
    '%ED%86%B1%ED%85%8D', #톱텍
    '%EC%B9%B4%EC%B9%B4%EC%98%A4', #카카오
    'LG%EC%A0%84%EC%9E%90', #LG전자
    '%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90', #삼성전자
    '%EC%82%BC%EC%84%B1%EC%A0%84%EA%B8%B0', #삼성전기
    #'%EA%B8%88%ED%98%B8%EC%84%9D%EC%9C%A0', #금호석유
    '%EB%A1%AF%EB%8D%B0%EC%BC%80%EB%AF%B8%EC%B9%BC', #롯데케미칼
    'kb%EA%B8%88%EC%9C%B5', #KB금융
    '%EC%82%BC%EC%84%B1sds', #삼성SDS
    '%EB%AF%B8%EB%9E%98%EC%97%90%EC%85%8B%EB%8C%80%EC%9A%B0', #미래에셋대우
    'nh%ED%88%AC%EC%9E%90%EC%A6%9D%EA%B6%8C', #NH투자증권
    'POSCO', #POSCO
    'SK', #SK
    '%EB%8C%80%ED%95%9C%ED%95%B4%EC%9A%B4', #대한해운
    'kg%EC%BC%80%EB%AF%B8%EC%B9%BC', #KG케미칼
    '%EB%A9%94%EB%A6%AC%EC%B8%A0%EA%B8%88%EC%9C%B5%EC%A7%80%EC%A3%BC', #메리츠금융지주
    '%EC%82%BC%EC%A7%80%EC%A0%84%EC%9E%90', #삼지전자
    'GS', #GS
    '%EB%8B%A4%EC%9A%B0%EB%8D%B0%EC%9D%B4%ED%83%80', #다우데이타
    'AK%ED%99%80%EB%94%A9%EC%8A%A4', #AK홀딩스
    '%EB%A9%94%EB%A6%AC%EC%B8%A0%ED%99%94%EC%9E%AC' #메리츠화재
]

data = []
data.append(['id', 'company_name', 'company_inderstry','company_sales','company_workers', 'company_explanatinos'])

for i in range(len(query)):
    url = baseurl + query[i]
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        cmp_explanations = soup.find_all(class_ = 'company_intro _ellipsis _detail')[0].find_all(class_ = '_text')[0].get_text()
        for j in range(0,1):
            cmp_name = (soup.find_all(class_ = 'company_info')[0].find_all(class_ = 'txt_info')[j].get_text())
        for j in range(4,5):
            cmp_inderstry = (soup.find_all(class_ = 'company_info')[0].find_all(class_ = 'txt_info')[j].get_text())
        for j in range(6,7):
            cmp_sales = (soup.find_all(class_ = 'company_info')[0].find_all(class_ = 'txt_info')[j].get_text())
        for j in range(7,8):
            cmp_workers = (soup.find_all(class_ = 'company_info')[0].find_all(class_ = 'txt_info')[j].get_text())
        data.append([i, cmp_name, cmp_inderstry, cmp_sales, cmp_workers, cmp_explanations])
    else:
        print("출력실패")


f = open('company_info.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(f)

for row in data:
    writer.writerow(row)

f.close()
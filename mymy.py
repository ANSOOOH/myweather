# -*- coding: utf-8 -*-
from urllib.request import urlopen, Request
import urllib
import bs4
import requests

location = '북아현동'
enc_location = urllib.parse.quote(location + '+날씨')

url = 'https://search.naver.com/search.naver?ie=utf8&query='+ enc_location

req = Request(url)
page = urlopen(req)
html = page.read()
soup = bs4.BeautifulSoup(html,'html.parser')
message1 = ('현재 ' + location + ' 날씨는 ' + soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text + '도 입니다.')

location = '서대문구'
enc_location = urllib.parse.quote(location + '+미세먼지')

url = 'https://search.naver.com/search.naver?ie=utf8&query='+ enc_location

req = Request(url)
page = urlopen(req)
html = page.read()
soup = bs4.BeautifulSoup(html,'html.parser')

myresult = int(soup.find('span', class_='figure').find('em', class_='main_figure').text)
def range(a):
    if a >= 0 and a <=30:
        return '좋음'
    elif a >= 31 and a <=50:
        return '보통'
    elif a >= 51 and a <=100:
        return '나쁨'
    else:
        return '매우 나쁨'

t = range(myresult)

message2 = ( '현재 ' + location + ' 미세먼지는 ' + str(t) + '입니다.')


#API 및 Token 정보

url = 'https://notify-api.line.me/api/notify'

token = {'Authorization' : 'Bearer 1fNgw0MPePRMlJgkNZ2UHyq7iID1sjuqE0RcGDyTA7U'}
#data = {}

parameter = {"message": '\n'+ message1 +'\n'+ message2, "stickerId":106, "stickerPackageId":1}
# parameter = {"message": message, "imageThumbnail":imageThumbnail ,"imageFullsize":imageFullsize}


#Response
response = requests.post(
    url, headers = token, data = parameter
)
print(response.text)

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
message = ('현재 ' + location + ' 날씨는 ' + soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text + '도 입니다.')




#API 및 Token 정보

url = 'https://notify-api.line.me/api/notify'

token = {'Authorization' : 'Bearer 1fNgw0MPePRMlJgkNZ2UHyq7iID1sjuqE0RcGDyTA7U'}
#data = {}

parameter = {"message": message, "stickerId":106, "stickerPackageId":1}
# parameter = {"message": message, "imageThumbnail":imageThumbnail ,"imageFullsize":imageFullsize}


#Response
response = requests.post(
    url, headers = token, data = parameter
)
print(response.text)
import requests
from bs4 import BeautifulSoup
import os

#파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('https://www.clien.net/service/board/sold')
req.encoding = 'utf-8'

html = req.text
soup = BeautifulSoup(html,'html.parser')
posts = soup.select('td.post_subject')
latest = list_title[1].text

with open(os.path.join(BASE_DIR,'latest.txt'),'w+') as f:
    f.write(latest)
#listTopForm > table > tbody > tr:nth-child(1) > td.title > div > span > a
# import telegram

# my_token = '783802387:AAF88HlaXrQE-bYVNmcrQkIiw2pfhTkooJo'

# bot = telegram.Bot(token = my_token)

# updates = bot.getUpdates()

# chat_id = bot.getUpdates()[0].message.chat.id

# bot.sendMessage(chat_id = chat_id, text='저는 봇입니다.')

# for u in updates:
#     print(u.message.chat.id)
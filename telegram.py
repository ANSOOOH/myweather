#soooh_bot
import requests
import telegram

token = '783802387:AAF88HlaXrQE-bYVNmcrQkIiw2pfhTkooJo'

bot = telegram.Bot(token = '783802387:AAF88HlaXrQE-bYVNmcrQkIiw2pfhTkooJo')
updates = token.getupdate()

for i in updates:
    print(i.message)
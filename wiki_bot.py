import telebot
import config
import wikipedia as wiki
from requests import get
from bs4 import BeautifulSoup as BS 

bot = telebot.TeleBot(config.TOCKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_photo(message.chat.id, get('https://vestikavkaza.ru/upload/2018-01-17/15161791305a5f0eba26c989.07783830.jpg').content)
	if message.from_user.username == None:
		bot.send_message(message.chat.id, 'Привет, я wikipedia-bot, напиши мне то, о чём ты хочешь узнать')
	else:
		bot.send_message(message.chat.id, f'Привет, {message.from_user.username}, я wikipedia-bot, напиши мне то, о чём ты хочешь узнать')
@bot.message_handler(content_types=['text'])
def send_text(message):
	try:
		page = get('https://yandex.ru/images/search?text=' + message.text)
		soup = BS(page.text, 'html.parser')
		img  = soup.find('img', {'class':'serp-item__thumb justifier__thumb'})
		img_src = 'http:' + img.get('src')
		bot.send_photo(message.chat.id, get(img_src).content)
	except:
		bot.send_photo(message.chat.id, get('https://creativebonito.com/wp-content/uploads/2019/03/404-error-page-not-found.png').content)

	try:
		wiki.set_lang('Ru')
		query = wiki.summary(message.text)
		bot.send_message(message.chat.id, query)
	except:
		bot.send_message(message.chat.id, 'К сожалению мы не ношли этого в Википедии')


bot.polling()
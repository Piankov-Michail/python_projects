from translate import Translator
import requests
import telebot
from telebot import types

translator= Translator(from_lang="russian",to_lang="english")

API_key = 'fae695686d7394eee9fcbd7a224c8878'
def url(city_name, API_key):
    return f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_key}&units=metric'

bot=telebot.TeleBot('5241948484:AAGqZC4JyFuiULxkKZZwhdXd57uPV96-6Po')

@bot.message_handler(commands=['start'])
def start_(message):
    bot.send_message(message.from_user.id,'Привет, этот бот поможет узнать погоду в вашем городе, напишите название своего города.')

@bot.message_handler(content_types=['text'])
def message_handler(message):
    try:
        city_name = translator.translate(message.text).lower()
        global response
        global API_key
        response = requests.get(url(city_name, API_key))
        response = response.json()
        if response['message']!='city not found':
            keyboard = types.InlineKeyboardMarkup()
            key_td = types.InlineKeyboardButton(text='Сегодня', callback_data='td')
            keyboard.add(key_td)
            key_tm = types.InlineKeyboardButton(text='Завтра', callback_data='tm')
            keyboard.add(key_tm)
            key_2d = types.InlineKeyboardButton(text='Послезавтра', callback_data='2d')
            keyboard.add(key_2d)
            key_3d = types.InlineKeyboardButton(text='Через 2 дня', callback_data='3d')
            keyboard.add(key_3d)
            key_4d = types.InlineKeyboardButton(text='Через 3 дня', callback_data='4d')
            keyboard.add(key_4d)
            key_5d = types.InlineKeyboardButton(text='Через 4 дня', callback_data='5d')
            keyboard.add(key_5d)
            bot.send_message(message.from_user.id, 'На какой день вы хотите узнать погоду', reply_markup=keyboard)
        else:
            bot.send_message(message.from_user.id, 'Такого города нет в базе данных')
    except Exception:
        bot.send_message(message.from_user.id, 'Такого города нет в базе данных')

def weather(n):
    all_data = response['list']
    result_info = []
    for i in range(3*(n-1), 3*n):
        time_txt = all_data[i]['dt_txt'][-8:]
        day_info = all_data[i]['main']
        temp = f'Температура: текущая: {day_info['temp']} ℃, мин: {day_info['temp_min']} ℃, макс: {day_info['temp_max']} ℃'
        pressure = f'Давление: {day_info['pressure']} мм рт. ст.'
        humidity = f'Влажность: {day_info['humidity']} %'
        wind = f'Скорость ветра: {all_data[i]['wind']['speed']} м/c'
        all_info = time_txt+'\n'+temp+'\n'+pressure+'\n'+humidity+'\n'+wind
        result_info.append(all_info)
    return '\n\n'.join(result_info)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data=='td':
        day=weather(1)
        bot.send_message(call.message.chat.id,'Cегодня:'+'\n'+day)
    elif call.data=='tm':
        day = weather(2)
        bot.send_message(call.message.chat.id,'Завтра:'+'\n'+day)
    elif call.data=='2d':
        day = weather(3)
        bot.send_message(call.message.chat.id,'Послезавтра:'+'\n'+day)
    elif call.data=='3d':
        day = weather(4)
        bot.send_message(call.message.chat.id,'Через 2 дня:'+'\n'+day)
    elif call.data=='4d':
        day = weather(5)
        bot.send_message(call.message.chat.id,'Через 3 дня:'+'\n'+day)
    elif call.data=='5d':
        day = weather(6)
        bot.send_message(call.message.chat.id,'Через 4 дня:'+'\n'+day)
bot.polling()

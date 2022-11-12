
import telebot
from telebot import apihelper
import openpyxl
import cv2
import xlrd
import xlwt
from openpyxl import Workbook
from openpyxl import load_workbook


token = '

bot = telebot.TeleBot(token)

links = openpyxl.load_workbook(("Ссылки.xlsx"))
sheet1 = links['list1']
maxRow = sheet1.max_row
#Определяем все авиакомпании какие есть
print(maxRow)

def Airlines (sheet1, maxRow):
    airlines = []
    i = 1
    while i < maxRow:
        al = sheet1.cell(row = i, column = 1).value
        if al in airlines:
            i = i + 1
        else:
            airlines.append(al)
            i += 1
    #print (airlines)
    return airlines

#Определяем категории
def Categorii(message, maxRow, sheet1):
    #c = input("Выбери АК: ")
    category = []
    i = 1
    while i < maxRow:
        cat = sheet1.cell(row = i, column = 2).value
        if message.text == sheet1.cell(row = i, column = 1).value:
            if (cat in category):
                i = i + 1
            else:
                category.append(cat)
                i += 1
        else: 
            i +=1
        ##print (category)
    return category

#print(Categorii('Аэрофлот', maxRow, sheet1))
#print(Airlines(sheet1, maxRow))



keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('')
i = 0
while i < len(Airlines(sheet1, maxRow)):
        keyboard2.add(telebot.types.InlineKeyboardButton(text=Airlines(sheet1, maxRow)[i]))
        i = i + 1
 
def category(message):
    markup = telebot.types.InlineKeyboardMarkup()
    i = 0
    while i < len(Categorii(message, maxRow, sheet1)):
        markup.add(telebot.types.InlineKeyboardButton(text=Categorii(message, maxRow, sheet1)[i], callback_data=i+1))
        i = i + 1
    bot.send_message(message.chat.id, 'Так, а теперь выбери категорию: ', reply_markup=markup)
    print(message.text)
    print(Categorii(message, maxRow, sheet1))

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я бот СОПП.', reply_markup=keyboard2)

@bot.message_handler(content_types=['text'])
def send_text(message):
    category (message)
# def Airlines(message):
#     markup = telebot.types.InlineKeyboardMarkup()
#     markup.add(telebot.types.InlineKeyboardButton(text='Аэрофлот', callback_data=3))
#     bot.send_message(message.chat.id, text="выбери авиакомпанию", reply_markup=markup)

# @bot.message_handler(content_types=['text'])
# def send_text(message):
#     if message.text.lower() == 'привет':
#         bot.send_message(message.chat.id, 'Привет! ззз')
#         Airlines(message)

@bot.callback_query_handler(func=lambda call: True)

def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Приятного времени ожидания!')                                                                                       
    answer = ''
    if call.data == '3': #AFL
        answer = 'link1'




bot.polling()





# def AirlinesTG(message):
#     markup = telebot.types.InlineKeyboardMarkup()
#     i = 0
#     while i < len(Airlines(sheet1, maxRow)):
#         markup.add(telebot.types.InlineKeyboardButton(text=Airlines(sheet1, maxRow)[i]))
#         i = i + 1
#     bot.send_message(message.chat.id, 'Выбери авиакомпанию: ', reply_markup=keyboard2)

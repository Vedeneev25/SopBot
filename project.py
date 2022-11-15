
import telebot
from telebot import apihelper
import openpyxl
import cv2
import xlrd
import xlwt
from openpyxl import Workbook
from openpyxl import load_workbook

token = '5397183960:AAH2WjLXtQGP9pTIpa3ggMyONSgPHwxq468'
bot = telebot.TeleBot(token)

#Работа с ексель файлом
links = openpyxl.load_workbook(("Ссылки.xlsx"))
sheet1 = links['list1']
maxRow = sheet1.max_row
print(maxRow)

#Определяем все авиакомпании какие есть в файле. Функция возвращает список
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

#Определяем категории. Функция принимает авиакомпанию, и возвращает список возможных ответов.
def Categorii(Airlinename, maxRow, sheet1):
    #c = input("Выбери АК: ")
    category = []
    i = 1
    while i < maxRow:
        cat = sheet1.cell(row = i, column = 2).value
        if AirlineName == sheet1.cell(row = i, column = 1).value:
            if (cat in category):
                i = i + 1
            else:
                category.append(cat)
                i += 1
        else: 
            i +=1
    return category

#Работа с ботом

AirlineName = ''
CategoryName = ''

# Say Hello to Bot
keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3.row('Привет! ')

#Формируем клавиатуру для первого сообщения, которую будем использовать в стартовом сообщении.
keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('')
i = 0
while i < len(Airlines(sheet1, maxRow)):
        keyboard2.add(telebot.types.InlineKeyboardButton(text=Airlines(sheet1, maxRow)[i]))
        i = i + 1

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, 'Привет, я бот СОПП', reply_markup=keyboard3)


@bot.message_handler(content_types=['text'])
def Get_airline(message):
    bot.send_message(message.from_user.id, 'Выбери авиакомпанию', reply_markup=keyboard2)
    bot.register_next_step_handler(message, category)

#На входе у метода уже есть название авиакомпании. Формируется список и клавиатура из всех возможных ответов. 
def category(message):
    global AirlineName
    AirlineName = message.text
    keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard1.row('')
    i = 0
    while i < len(Categorii(AirlineName, maxRow, sheet1)):
        keyboard1.add(telebot.types.InlineKeyboardButton(text=Categorii(message, maxRow, sheet1)[i]))
        i = i + 1
    keyboard1.add(telebot.types.InlineKeyboardButton(text="Другая авиакомпания"))
    bot.send_message(message.from_user.id, 'Так, а теперь выбери категорию: ', reply_markup=keyboard1)
    bot.register_next_step_handler(message, send_text)


def send_text(message):
    global CategoryName
    CategoryName = message.text
    if CategoryName == "Другая авиакомпания":
        bot.send_message(message.from_user.id, 'Перевыбери авиакомпанию', reply_markup=keyboard2)
        bot.register_next_step_handler(message, category)     
    else:
        i=1
        while (i < maxRow):
            if (AirlineName == sheet1.cell(row = i, column = 1).value and CategoryName == sheet1.cell(row = i, column = 2).value):
                answer = sheet1.cell(row = i, column = 3).value
                break
            else:
                i += 1
        bot.send_message(message.from_user.id, "вот ссылка на ответ: " + answer)
        bot.send_message(message.from_user.id, 'Выбери авиакомпанию', reply_markup=keyboard2)
        bot.register_next_step_handler(message, category)  
        
        
bot.polling()



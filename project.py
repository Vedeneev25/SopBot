
import telebot
from telebot import apihelper
import openpyxl

token = ''

bot = telebot.TeleBot(token)

#keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
#keyboard.row('/маршрут','/ассортимент и меню')
keyboard2.row('', 'Магазины','Parcking','ZSO') #Перечень авиакомпаний


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Выбери авиакомпанию', reply_markup=keyboard2)

def FB(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Шоколадница ВВЛ', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='Борт 17/93', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(text='Babooshka', callback_data=5))
    markup.add(telebot.types.InlineKeyboardButton(text='KFC', callback_data=9))
    markup.add(telebot.types.InlineKeyboardButton(text='Жигулево', callback_data=10))
    markup.add(telebot.types.InlineKeyboardButton(text='Macaroni', callback_data=11))
    markup.add(telebot.types.InlineKeyboardButton(text='Шоколадница Веранда', callback_data=12))
    markup.add(telebot.types.InlineKeyboardButton(text='Tiger Bar', callback_data=13))
    markup.add(telebot.types.InlineKeyboardButton(text='Coffee+', callback_data=14))
    markup.add(telebot.types.InlineKeyboardButton(text='Burger', callback_data=15))
    markup.add(telebot.types.InlineKeyboardButton(text='Craft', callback_data=16))
    markup.add(telebot.types.InlineKeyboardButton(text='Zoom', callback_data=17))
    bot.send_message(message.chat.id, text="выбери рестик", reply_markup=markup)

def Retail(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Хорошие новости СЗ', callback_data=6))
    markup.add(telebot.types.InlineKeyboardButton(text='Цветы', callback_data=7))
    markup.add(telebot.types.InlineKeyboardButton(text='Craft', callback_data=16))
    markup.add(telebot.types.InlineKeyboardButton(text='Моя станица', callback_data=18))
    markup.add(telebot.types.InlineKeyboardButton(text='Кубанские сувениры', callback_data=19))
    markup.add(telebot.types.InlineKeyboardButton(text='The store', callback_data=20))
    markup.add(telebot.types.InlineKeyboardButton(text='Аптека', callback_data=21))
    markup.add(telebot.types.InlineKeyboardButton(text='Olymp Beauty', callback_data=22))
    markup.add(telebot.types.InlineKeyboardButton(text='TOY', callback_data=23))
    markup.add(telebot.types.InlineKeyboardButton(text='Оренбургский пузовой платок', callback_data=24))
    markup.add(telebot.types.InlineKeyboardButton(text='Souvenirs', callback_data=25))
    markup.add(telebot.types.InlineKeyboardButton(text='Billfinch', callback_data=26))
    markup.add(telebot.types.InlineKeyboardButton(text='Хорошие новости ОЗ', callback_data=27))
    bot.send_message(message.chat.id, text="выбери магазин", reply_markup=markup)
  
def ZSO(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='ЗСО', callback_data=28))
    
    
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'кафе и рестораны':
        FB(message)
        
    elif message.text.lower() == 'магазины':
        Retail(message)
    else:
        start_message(message)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(callback_query_id=call.id, text='Приятного времени ожидания!')                                                                                       
    answer = ''
    if call.data == '3': #Shoko VVL
        answer = 'Кофейня «Шоколадница» предлагает широкий ассортимент напитков, закусок, горячих блюд, которые не только радуют глаз своим внешним видом, но и изобилием вкусов. Здесь вы сможете приятно провести время за чашкой ароматного кофе и попробовать наши фирменные десерты, взять полноценный горячий обед или быстро перекусить по пути на самолет. Быстрое и качественное обслуживание, уютная атмосфера, самые качественные продукты — наш приоритет.'
        pic = open('1.png','rb')
        pic2 = open('3.png','rb')
        menu = open('2.pdf','rb')
    elif call.data == '4': #Bort
        answer = 'Кафе «Борт 17/93» предлагает посетителям легкие закуски, сэндвичи, бургеры, круглосуточные завтраки, десерты, а также большой выбор напитков: кофе, чай, лимонады, смузи. Мы собрали коллекцию пива высшего качества зарубежных сортов, большой ассортимент вина Кубанских виноделен.'
        pic = open('Bort.png','rb')
        pic2 = open('Bort_place.png','rb')
        #menu = open('2.pdf','rb')
    elif call.data == '5': #Babooshka
        answer = 'Домашние завтраки и обеды по приятным ценам. Всегда в меню супы, салаты, холодные и горячие закуски, мороженное, десерты и свежая выпечка, а также напитки: морсы, соки, чай, кофе, вино и шампанское.'
        pic = open('Babooshka.png','rb')
        pic2 = open('Babooshka_place.png','rb')
        #menu = open('Baboosha_menu.pdf','rb')
    elif call.data == '6': #Good news Airside
        answer = 'В Федеральной Сети Минимаркетов «Хорошие Новости» Вы всегда можете приобрести новинки книжной продукции на любой жанр, свежую периодическую продукцию (газеты, журналы, сканворды, судоку), свежие и на любой вкус продукты питания и напитки, гигиена в дорогу, сувениры, товары для путешествия, подарки.'
        pic = open('GN_airside.png','rb')
        pic2 = open('GN_airside_place.png','rb')
        #menu = open('Baboosha_menu.pdf','rb')
    elif call.data == '7': #Klumba
        answer = 'Цветы и букеты на любой вкус, а также опытный флорист соберёт букет по Вашему желанию быстро и качественно, проконсультирует как сохранить красоту и свежесть букета или цветка как можно дольше. Каждому покупателю внимательное отношение и хорошее настроение обеспечено!'
        pic = open('Klumba.png','rb')
        pic2 = ' '
        #menu = open('Baboosha_menu.pdf','rb')
    elif call.data == '18': #Moya stanica
        answer = 'Фирменный магазин «Моя Станица» предлагает покупателям 100 % натуральные продукты родной Кубани. Под брендом «Моя Станица» выпускаются охлажденные мясные изделия, свежие колбасы и молочная продукция с уникальной формулой А2 — легко усваивается и усиливает защитные функции организма. Порадуйте натуральными деликатесами «Моя Станица» себя и близких!'
        pic = open('Stanica.png','rb')
        pic2 = open('Stanica_place.png','rb')
        #menu = open('Baboosha_menu.pdf','rb')
    elif call.data == '9': #KFC
        answer = 'KFC — международный ресторанный бренд с многолетней историей достижений и инноваций, специализирующийся на блюдах из курицы. История бренда началась с полковника Харланда Сандерса, более 75 лет назад создавшего уникальный рецепт приготовления курицы с применением 11 трав и специй. Этот рецепт был записан на обратной стороне двери в его кухню.Сегодня KFC по-прежнему следует формуле успеха, созданной полковником Сандерсом, — курица панируется и готовится вручную специально обученными поварами более чем в 22 000 ресторанах KFC в 136 странах мира. Дополнительную информацию вы сможете найти на сайте www.kfc.ru.'
        pic = open('kfc.png','rb')
        #menu = open('2.pdf','rb')
        pic2=' '
    elif call.data == '10': #Zhigulevo
        answer = 'Интерьер выполнен в стиле «Советский курорт»: лёгкая мебель, фитостена, центр притяжения - барная стойка, выполненная из светлого дерева. Лёгкая веселая атмосфера поддерживается музыкальным сопровождением. Основа меню - фирменное пиво «Жигули», которое варится по особому рецепту с 1968 года. Также в меню представлены горячие закуски к пиву, салаты, бутерброды с краковской колбасой, курицей, лососем, пельмени и другие горячие блюда, десерты.'
        pic = open('Zhigulevo.png','rb')
        #menu = open('2.pdf','rb')
        pic2= open('Zhigulevo_place.png','rb')
    elif call.data == '11': #Macaroni
        answer = 'Яркое, расслабляющее, располагающее к путешествиям – это итальянское бистро Macaroni в аэропорту Краснодара. Приглашаем всех, кто хочет получить удовольствие от любого путешествия.Круассаны, панини – чтобы позавтракать в любое время суток. Салаты и горячие блюда – для сытного обеда. Паста на любой вкус здесь для всех гостей – даже если ваш самолет направляется не в Италию. Блюда любимой и понятной русской кухни в меню тоже есть!В Macaroni вы можете насладиться чашкой настоящего итальянского эспрессо, или же выбрать кофейный напиток с молоком и десерт к нему, а также скоротать время в ожидании рейса за бокалом вина.Спокойно накормить детей перед полетом или завершить рабочие дела с ноутбуком – для всех дел перед рейсом есть душевное бистро Macaroni.'
        pic = open('Macaroni.png','rb')
        #menu = open('2.pdf','rb')
        pic2= open('Zhigulevo_place.png','rb')
    elif call.data == '12': #Shokoladnica veranda
        answer = 'Кофейня «Шоколадница» предлагает широкий ассортимент напитков, закусок, горячих блюд, которые не только радуют глаз своим внешним видом, но и изобилием вкусов. Здесь вы сможете приятно провести время за чашкой ароматного кофе и попробовать наши фирменные десерты, взять полноценный горячий обед или быстро перекусить по пути на самолет. Быстрое и качественное обслуживание, уютная атмосфера, самые качественные продукты — наш приоритет.'
        pic = open('Shokoveranda.png','rb')
        pic2 = ' '
        #menu = open('2.pdf','rb')
    elif call.data == '13': #Tiger
        answer = 'Всегда для Вас свежее разливное пиво от лучших отечественных и импортных производителей, безалкогольные коктейли и лимонады, горячие и холодные закуски. Вы сможете приятно провести время в ожидании рейса в кафе на летней терассе.'
        pic = open('Tiger.png','rb')
        pic2 = open('Tiger_place.png','rb')
        #menu = open('2.pdf','rb')
    elif call.data == '14': #Coffee+
        answer = 'После длительного перелета предлагаем нашим гостям бодрящий КОФЕ+ мороженое, сэндвичи, домашние блинчики, десерты и большой выбор напитков: свежевыжатый сок, смузи, молочный коктейль, витаминный чай.'
        pic = open('Coffee+.png','rb')
        pic2 = open('Coffee+_place.png','rb')
        #menu = open('2.pdf','rb')
    elif call.data == '15': #Burger
        answer = 'Бургерная B&D- предлагает одно самых популярных блюд в мире -Бургеры, который готовят на ваших глазах, а также другие прекрасные закуски. Еще вам предложат эксклюзивные сорта крафтового пива из отечественных пивоварен и пиво известных зарубежных марок.'
        pic = open('Burger.png','rb')
        pic2 = open('Burger_place.png','rb')
        #menu = open('2.pdf','rb')
    elif call.data == '16': #Craft
        answer = 'Craft Store|Wine bar — это совершенно новая концепция, новое слово в сегменте «эко, био, фрэш» продукции. Попробуйте эксклюзивные сорта крафтового пива из лучших пивоварен России, мясные деликатесы, широкий ассортимент местных сыров, произведенных на частных эко-фермах. Также в ассортименте Craft представлены орехи, сухофрукты, специи, чай, масла, а также мед и джем — яркий вкус природы.'
        pic = open('Craft.png','rb')
        pic2 = open('Craft_place.png','rb')
        #menu = open('2.pdf','rb')
    elif call.data == '17': #Zoom
        answer = 'Небольшая уютная кофейня, где можно в ожидании прилетающих или своего самолета в комфортной обстановке с ароматным кофе и вкуснейшим сэндвичем провести время.'
        pic = open('Zoom.png','rb')
        pic2 = ' '
        #menu = open('2.pdf','rb')
    elif call.data == '19': #Kubanskie suveniry
        answer = 'Не знаете, где найти подарок, отражающий колорит южного региона? Декоративные тарелки, сувенирные доски, магниты, обереги, оригинальные изделия народного промысла придутся по вкусу и коллегам, и близким. Эксклюзивные керамические изделия, созданные вручную по эскизам местного мастера Елены Лысенко, наполнят уютом любой офис и подчеркнут гармонию домашнего очага.'
        pic = open('Kub.png','rb')
        pic2 = open('Kub_place.png','rb')
        #menu = open('Baboosha_menu.pdf','rb')
    elif call.data == '20': #The store
        answer = 'Все товары исключительно оригинального производства и высочайшего качества. Элитная парфюмерия и косметика от ведущих мировых производителей, стильные ювелирные изделия, часы, очки, сумки, багаж и аксессуары, а также продукты питания. Каждому клиенту гарантирован высокий уровень сервиса и консультации профессионалов. Все товары сертифицированы и поставляются из Европы!'
        pic = open('Store.png','rb')
        pic2 = open('Store_place.png','rb')
        #menu = open('Baboosha_menu.pdf','rb')
    elif call.data == '21': #Apteka
        answer = 'В аптеке Лаки Фарма Вы найдете необходимые медикаменты и средства гигиены, чтобы Ваше путешествие всегда было комфортным.'
        pic = open('Apteka.png','rb')
        pic2 = open('Apteka_place.png','rb')
        #menu = open('Baboosha_menu.pdf','rb')
    elif call.data == '22': #Olymp Beauty
        answer = 'Селективная парфюмерия от лучших парфюмерных домов Франции, Италии, Великобритании, Арабских Эмиратов и Швеции. Большой выбор солнцезащитных очков от известных брендов. Подиумные модели последних коллекций. Здесь всегда рады помочь Вам сделать правильный выбор!'
        pic = open('Olymp.png','rb')
        pic2 = open('Olymp_place.png','rb')
        #menu = open('Baboosha_menu.pdf','rb')
    elif call.data == '23': #TOY
        answer = 'В детском магазине Toy вы с легкостью найдете то, чем порадовать ребенка, ведь здесь представлены развивающие игры и игрушки для разных возрастных групп.'
        pic = open('TOY.png','rb')
        pic2 = open('TOY_place.png','rb')
        #menu = open('Baboosha_menu.pdf','rb')
    elif call.data == '24': #OPP
        answer = 'Изделия из пуха и шерсти, платки, палантины, одежда, детская одежда и эксклюзивные изделия ручной работы.'
        pic = open('OPP.png','rb')
        pic2 = open('OPP_place.png','rb')
        #menu = open('Baboosha_menu.pdf','rb')
    elif call.data == '25': #Souvenirs
        answer = 'Широкий ассортимент товаров на любой вкус: сувенирная продукция, сопутствующие товары для путешествия, кожгалантерея известных брендов, украшения, элитные чаи, мёд, большой выбор сладостей. Здесь всегда рады гостям.'
        pic = open('Souvenirs.png','rb')
        pic2 = open('Souvenirs_place.png','rb')
        #menu = open('Baboosha_menu.pdf','rb')
    elif call.data == '26': #BullFinch
        answer = '«BULLFINCH» — футболки отличного качество с уникальными принтами от наших дизайнеров станут необычным подарком для друзей, коллег или второй половинки. Вы сможете выбрать принт, подходящую именно вам, вашему хобби и работе, или напоминающую о забавном случае из жизни.'
        pic = open('BF.png','rb')
        pic2 = open('BF_place.png','rb')
        #menu = open('Baboosha_menu.pdf','rb')
    elif call.data == '27': #GoodNews Landside
        answer = 'В Федеральной Сети Минимаркетов «Хорошие Новости» Вы всегда можете приобрести новинки книжной продукции на любой жанр, свежую периодическую продукцию (газеты, журналы, сканворды, судоку), свежие и на любой вкус продукты питания и напитки, гигиена в дорогу, сувениры, товары для путешествия, подарки.'
        pic = open('GN_landside.png','rb')
        pic2 = open('GN_landside_place.png','rb')
        #menu = open('Baboosha_menu.pdf','rb')
    elif call.data == '28': #ZSO
        answer = 'Уходи от сюда, нищеброд'
        pic = open('GN_landside.png','rb')
        pic2 = open('GN_landside_place.png','rb')
        #menu = open('Baboosha_menu.pdf','rb')
    else:
        answer = '  '

        
    #bot.send_photo(call.message.chat.id, menu)
    bot.send_photo(call.message.chat.id, pic)
    if pic2 != ' ':
        bot.send_photo(call.message.chat.id, pic2)
    bot.send_message(call.message.chat.id, answer, reply_markup=keyboard2)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)




bot.polling()

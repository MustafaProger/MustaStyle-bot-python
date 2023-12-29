import telebot
from telebot import TeleBot, types
from functions import func_for_watch_descr, show_prices



TOKEN = "6556679332:AAGd4ZDmpWh1O9luTfeUKSGXUjdAAzEPiJ4"
bot = telebot.TeleBot(TOKEN)

HELP_COMMAND = """
/help - список комманд 
/start - начать работу с ботом
/about - о нас
"""

@bot.message_handler(commands=[ 'help'])
def help_command(message) :
    bot.send_message(message.chat.id, HELP_COMMAND)


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Русский 🇷🇺')
    btn2 = types.KeyboardButton('English 🇬🇧')
    markup.add (btn1, btn2)
    send_mess = f'Привет, {message.from_user.first_name}.'
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
    bot.send_message(message.chat.id, 'Выберите язык.')


@bot.message_handler(commands=['about'])
def about_handler(message):
    bot.send_message(message.chat.id, f'MustaStyle — ваш надежный проводник в мире элегантности и точности времени. Наша компания, основанная студентом-программистом Мустафой, сочетает в себе страсть к инновациям, высокому стилю и уважению к времени.\n\nМы специализируемся на продаже часов, которые не только служат функциональным измерителем времени, но и становятся неотъемлемой частью вашего стиля. В ассортименте MustaStyle вы найдете коллекции, вдохновленные последними трендами моды, классическим дизайном и инновационными технологиями.\n\nНаша цель - не просто предоставлять товар, а создавать уникальный опыт для наших клиентов. Мы стремимся удовлетворить запросы даже самых требовательных ценителей часов. Каждая модель внимательно отобрана и прошла тщательный контроль качества, чтобы удовлетворить ожидания даже самых искушенных покупателей.\n\nMustaStyle гордится своей преданностью качеству и предоставлению беспрецедентного уровня обслуживания. Наши сотрудники обладают глубокими знаниями в области часового искусства и всегда готовы поделиться своими знаниями, чтобы помочь вам сделать правильный выбор.\n\nПокупка часов в MustaStyle - это не просто приобретение аксессуара, но и инвестиция в свой стиль и уникальность. Доверьтесь нам, и мы сделаем ваш выбор часов незабываемым и приятным моментом.\n\nВыберите MustaStyle — выберите стиль, выберите качество, выберите надежность. Мы заботимся о вашем времени, чтобы вы могли наслаждаться каждым моментом в стиле MustaStyle.')


@bot.message_handler(func=lambda message: message.text == 'Русский 🇷🇺')
def select_watch(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    select_watch = "Теперь выберите фирму часов, которую бы вы хотели приобрести."
    btn0 = types.KeyboardButton('MystaStyle')
    btn1 = types.KeyboardButton('Rolex')
    btn2 = types.KeyboardButton('Omega')
    btn3 = types.KeyboardButton('Patek Philippe')
    btn4 = types.KeyboardButton('Audemars Piguet')
    btn5 = types.KeyboardButton('Tag Heuer')
    btn6 = types.KeyboardButton('Seiko')
    btn7 = types.KeyboardButton('Casio')
    btn8 = types.KeyboardButton('Fossil')
    btn9 = types.KeyboardButton('Citizen')
    btn10 = types.KeyboardButton('Timex')
    btn11 = types.KeyboardButton('Swatch')
    btn12 = types.KeyboardButton('Tissot')
    btn13 = types.KeyboardButton('Bulova')
    btn14 = types.KeyboardButton('Michael Kors')
    btn15 = types.KeyboardButton('Apple (Apple Watch)')
    btn16 = types.KeyboardButton('Garmin')
    btn17 = types.KeyboardButton('Hublot')
    btn18 = types.KeyboardButton('Cartier')
    btn19 = types.KeyboardButton('Breitling')
    btn20 = types.KeyboardButton('Vacheron Constantin')
    btn21 = types.KeyboardButton('Longines')
    btn22 = types.KeyboardButton('Jaeger-LeCoultre')
    btn23 = types.KeyboardButton('Panerai')
    btn24 = types.KeyboardButton('IWC Schaffhausen')
    btn25 = types.KeyboardButton('Chopard')
    btn26 = types.KeyboardButton('Blancpain')
    btn27 = types.KeyboardButton('Ulysse Nardin')
    btn28 = types.KeyboardButton('Rado')
    btn29 = types.KeyboardButton('Oris')
    btn30 = types.KeyboardButton('Bell & Ross')
    btn31 = types.KeyboardButton('Maurice Lacroix')
    btn32 = types.KeyboardButton('Baume & Mercier')
    btn33 = types.KeyboardButton('Raymond Weil')
    btn34 = types.KeyboardButton('Girard-Perregaux')
    btn35 = types.KeyboardButton('Sinn')
    btn36 = types.KeyboardButton('Montblanc')
    btn37 = types.KeyboardButton('Victorinox')
    btn38 = types.KeyboardButton('Breguet')
    btn39 = types.KeyboardButton('Zenith')
    btn40 = types.KeyboardButton('Alpina')
    btn41 = types.KeyboardButton('Bulgari')
    btn42 = types.KeyboardButton('Frederique Constant')
    btn43 = types.KeyboardButton('Nomos Glashütte')
    btn44 = types.KeyboardButton('Piaget')
    btn45 = types.KeyboardButton('H. Moser & Cie')
    btn46 = types.KeyboardButton('Richard Mille')
    btn47 = types.KeyboardButton('HYT')
    btn48 = types.KeyboardButton('Corum')
    btn49 = types.KeyboardButton('Shinola')
    btn50 = types.KeyboardButton('DIOR')
    
    markup.add(btn0, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16, btn17, btn18, btn19, btn20, btn21, btn22, btn23, btn24, btn25, btn26, btn27, btn28, btn29, btn30, btn31, btn32, btn33, btn34, btn35, btn36, btn37, btn38, btn39, btn40, btn41, btn42, btn43, btn44, btn45, btn46, btn47, btn48, btn49, btn50)
    bot.send_message(message.chat.id, select_watch, parse_mode='html', reply_markup=markup)

#MustaStyle
    @bot.message_handler(func=lambda message: message.text == btn0.text)
    def models(message):
        bot.send_message(message.chat.id, 'Ух ты, MustaStyle — твой выбор! Мы с удовольствием предложим тебе уникальные часы, соответствующие твоему вкусу, цветовой гамме и бюджету. Просто расскажи нам о том, какие часы ты предпочитаешь, оставив заявку на нашем сайте, и мы обязательно свяжемся с тобой в самое ближайшее время. Доверь нам создание твоего идеального аксессуара времени!')

#Rolex
    @bot.message_handler(func=lambda message: message.text == btn1.text)
    def models(message):
        func_for_watch_descr('Rolex', 
                                'Rolex Submariner',
                                'Rolex Datejust',
                                'Rolex Day-Date',
                                'Rolex GMT-Master II',
                                'Rolex Explorer',
                                'Rolex Yacht-Master',
                                'Rolex Sea-Dweller',
                                'Rolex Daytona',
                                'Rolex Milgauss',
                                'Rolex Oyster Perpetual',
                                'Узнать цены часов', 
                                message)
        @bot.message_handler(func=lambda message: message.text.lower() == 'узнать цены часов')
        def prices(message):
            show_prices('Rolex Submariner','600,000 - 2,700,000 руб.',
                        'Rolex Datejust', '525,000 - 3,750,000 руб.',
                        'Rolex Day-Date', '1,875,000 - 7,500,000 руб', 
                        'Rolex GMT-Master II', '675,000 - 3,750,000 руб.',
                        'Rolex Explorer', '450,000 - 1,875,000 руб.',
                        'Rolex Yacht-Master', '825,000 - 3,750,000 руб',
                        'Rolex Sea-Dweller', '825,000 - 1,500,000 руб.',
                        'Rolex Daytona', '975,000 - 6,000,000 руб',
                        'Rolex Milgauss', '600,000 - 1,500,000 руб.',
                        'Rolex Oyster Perpetual', '375,000 - 1,500,000 руб.',
                        message)
   
#Omega
    @bot.message_handler(func=lambda message: message.text == btn2.text)
    def models(message):
        func_for_watch_descr('Omega',
                            'Omega Seamaster',
                            'Omega Speedmaster',
                            'Omega Constellation',
                            'Omega De Ville',
                            'Omega Aqua Terra',
                            'Omega Globemaster',
                            'Omega Railmaster',
                            'Omega Seamaster Diver 300M',
                            'Omega Seamaster Planet Ocean',
                            'Omega Speedmaster Moonwatch',
                            'Узнать цены часов',
                            message)

        @bot.message_handler(func=lambda message: message.text.lower() == 'узнать цены часов')
        def prices(message):
            show_prices('Omega Seamaster', '30,000 - 500,000 руб.',
                        'Omega Speedmaster', '40,000 - 600,000 руб.',
                        'Omega Constellation', '25,000 - 400,000 руб.',
                        'Omega De Ville', '20,000 - 350,000 руб.',
                        'Omega Aqua Terra', '30,000 - 550,000 руб.',
                        'Omega Globemaster', '50,000 - 800,000 руб.',
                        'Omega Railmaster', '40,000 - 650,000 руб.',
                        'Omega Seamaster Diver 300M', '35,000 - 600,000 руб.',
                        'Omega Seamaster Planet Ocean', '45,000 - 700,000 руб.',
                        'Omega Speedmaster Moonwatch', '40,000 - 650,000 руб.',
                        message)

#Patek Philippe
    @bot.message_handler(func=lambda message: message.text == btn3.text)
    def models(message):
        func_for_watch_descr('Patek Philippe', 
                            'Patek Philippe Calatrava',
                            'Patek Philippe Nautilus',
                            'Patek Philippe Aquanaut',
                            'Patek Philippe Grand Complications',
                            'Patek Philippe Twenty-4',
                            'Patek Philippe Complications',
                            'Patek Philippe Golden Ellipse',
                            'Patek Philippe Gondolo',
                            'Patek Philippe World Time',
                            'Patek Philippe Sky Moon Tourbillon',
                            'Узнать цены часов', 
                            message)
                            
        @bot.message_handler(func=lambda message: message.text.lower() == 'узнать цены часов')
        def prices(message):
            show_prices('Patek Philippe Calatrava', '1,500,000 - 3,750,000 руб.',
                        'Patek Philippe Nautilus', '2,250,000 - 22,500,000 руб.',
                        'Patek Philippe Aquanaut', '3,000,000 - 15,000,000 руб.',
                        'Patek Philippe Grand Complications', '7,500,000 - многомиллионные руб.',
                        'Patek Philippe Twenty-4', '750,000 - 3,750,000 руб.',
                        'Patek Philippe Complications', '3,750,000 - 37,500,000 руб.',
                        'Patek Philippe Golden Ellipse', '1,500,000 - 7,500,000 руб.',
                        'Patek Philippe Gondolo', '1,500,000 - 7,500,000 руб.',
                        'Patek Philippe World Time', '3,750,000 - 15,000,000 руб.',
                        'Patek Philippe Sky Moon Tourbillon', '75,000,000 - многомиллионные руб.',
                        message)

#Audemars Piguet
    @bot.message_handler(func=lambda message: message.text == btn4.text)
    def models(message):
        func_for_watch_descr('Audemars Piguet',
                            'Audemars Piguet Royal Oak',
                            'Audemars Piguet Royal Oak Offshore',
                            'Audemars Piguet Royal Oak Concept',
                            'Audemars Piguet Millenary',
                            'Audemars Piguet Jules Audemars',
                            'Audemars Piguet Haute Joaillerie',
                            'Audemars Piguet Code 11.59',
                            'Audemars Piguet Edward Piguet',
                            'Audemars Piguet Tradition',
                            'Audemars Piguet Royal Oak Tourbillon',
                            'Узнать цены часов',
                            message)

        @bot.message_handler(func=lambda message: message.text.lower() == 'узнать цены часов')
        def prices(message):
            show_prices('Audemars Piguet Royal Oak', '1,000,000 - 20,000,000 руб.',
                        'Audemars Piguet Royal Oak Offshore', '1,500,000 - 25,000,000 руб.',
                        'Audemars Piguet Royal Oak Concept', '3,000,000 - 30,000,000 руб.',
                        'Audemars Piguet Millenary', '750,000 - 10,000,000 руб.',
                        'Audemars Piguet Jules Audemars', '1,200,000 - 15,000,000 руб.',
                        'Audemars Piguet Haute Joaillerie', '5,000,000 - многомиллионные руб.',
                        'Audemars Piguet Code 11.59', '2,000,000 - 25,000,000 руб.',
                        'Audemars Piguet Edward Piguet', '1,500,000 - 18,000,000 руб.',
                        'Audemars Piguet Tradition', '800,000 - 12,000,000 руб.',
                        'Audemars Piguet Royal Oak Tourbillon', '3,500,000 - 40,000,000 руб.',
                        message)

#Tag Heuer
    @bot.message_handler(func=lambda message: message.text == btn5.text)
    def models(message):
        func_for_watch_descr('Tag Heuer',
                            'Tag Heuer Carrera',
                            'Tag Heuer Monaco',
                            'Tag Heuer Aquaracer',
                            'Tag Heuer Formula 1',
                            'Tag Heuer Connected',
                            'Tag Heuer Autavia',
                            'Tag Heuer Link',
                            'Tag Heuer Kirium',
                            'Tag Heuer Carrera Heuer 02',
                            'Tag Heuer Carrera Calibre 16',
                            'Узнать цены часов',
                            message)

        @bot.message_handler(func=lambda message: message.text.lower() == 'узнать цены часов')
        def prices(message):
            show_prices('Tag Heuer Carrera', '50,000 - 500,000 руб.',
                        'Tag Heuer Monaco', '60,000 - 600,000 руб.',
                        'Tag Heuer Aquaracer', '40,000 - 400,000 руб.',
                        'Tag Heuer Formula 1', '30,000 - 300,000 руб.',
                        'Tag Heuer Connected', '70,000 - 700,000 руб.',
                        'Tag Heuer Autavia', '55,000 - 550,000 руб.',
                        'Tag Heuer Link', '45,000 - 450,000 руб.',
                        'Tag Heuer Kirium', '40,000 - 400,000 руб.',
                        'Tag Heuer Carrera Heuer 02', '65,000 - 650,000 руб.',
                        'Tag Heuer Carrera Calibre 16', '60,000 - 600,000 руб.',
                        message)

#Seiko
    @bot.message_handler(func=lambda message: message.text == btn6.text)
    def models(message):
        func_for_watch_descr('Seiko',
                            'Seiko Presage',
                            'Seiko Prospex',
                            'Seiko Astron',
                            'Seiko 5',
                            'Seiko Premier',
                            'Seiko Velatura',
                            'Seiko Recraft',
                            'Seiko Ananta',
                            'Seiko Brightz',
                            'Seiko Lukia',
                            'Узнать цены часов',
                            message)

        @bot.message_handler(func=lambda message: message.text.lower() == 'узнать цены часов')
        def prices(message):
            show_prices('Seiko Presage', '20,000 - 200,000 руб.',
                        'Seiko Prospex', '30,000 - 300,000 руб.',
                        'Seiko Astron', '50,000 - 500,000 руб.',
                        'Seiko 5', '10,000 - 100,000 руб.',
                        'Seiko Premier', '40,000 - 400,000 руб.',
                        'Seiko Velatura', '25,000 - 250,000 руб.',
                        'Seiko Recraft', '15,000 - 150,000 руб.',
                        'Seiko Ananta', '60,000 - 600,000 руб.',
                        'Seiko Brightz', '45,000 - 450,000 руб.',
                        'Seiko Lukia', '35,000 - 350,000 руб.',
                        message)

#Casio
    @bot.message_handler(func=lambda message: message.text == btn7.text)
    def models(message):
        func_for_watch_descr('Casio',
                            'Casio G-Shock',
                            'Casio Edifice',
                            'Casio Pro Trek',
                            'Casio Vintage',
                            'Casio Baby-G',
                            'Casio Wave Ceptor',
                            'Casio Illuminator',
                            'Casio Databank',
                            'Casio Beside',
                            'Casio Sheen',
                            'Узнать цены часов',
                            message)

        @bot.message_handler(func=lambda message: message.text.lower() == 'узнать цены часов')
        def prices(message):
            show_prices('Casio G-Shock', '5,000 - 50,000 руб.',
                        'Casio Edifice', '10,000 - 100,000 руб.',
                        'Casio Pro Trek', '15,000 - 150,000 руб.',
                        'Casio Vintage', '3,000 - 30,000 руб.',
                        'Casio Baby-G', '4,000 - 40,000 руб.',
                        'Casio Wave Ceptor', '7,000 - 70,000 руб.',
                        'Casio Illuminator', '2,000 - 20,000 руб.',
                        'Casio Databank', '2,500 - 25,000 руб.',
                        'Casio Beside', '6,000 - 60,000 руб.',
                        'Casio Sheen', '8,000 - 80,000 руб.',
                        message)

#Fossil
    @bot.message_handler(func=lambda message: message.text == btn8.text)
    def models(message):
        func_for_watch_descr('Fossil',
                            'Fossil Gen 6',
                            'Fossil Hybrid HR HR Collider',
                            'Fossil Solar',
                            'Fossil The Carlyle HR',
                            'Fossil Monroe',
                            'Fossil Nate',
                            'Fossil Machine',
                            'Fossil Forrester',
                            'Fossil The Minimalist',
                            'Fossil Neutra',
                            'Узнать цены часов',
                            message)

        @bot.message_handler(func=lambda message: message.text.lower() == 'узнать цены часов')
        def prices(message):
            show_prices('Fossil Gen 6', '15,000 - 35,000 руб.',
                        'Fossil Hybrid HR Collider', '10,000 - 25,000 руб.',
                        'Fossil Solar', '12,000 - 30,000 руб.',
                        'Fossil The Carlyle HR', '14,000 - 40,000 руб.',
                        'Fossil Monroe', '7,000 - 20,000 руб.',
                        'Fossil Nate', '9,000 - 22,000 руб.',
                        'Fossil Machine', '8,000 - 18,000 руб.',
                        'Fossil Forrester', '10,000 - 24,000 руб.',
                        'Fossil The Minimalist', '6,000 - 15,000 руб.',
                        'Fossil Neutra', '5,000 - 12,000 руб.',
                        message)

#Citizen
    @bot.message_handler(func=lambda message: message.text == btn9.text)
    def models(message):
        func_for_watch_descr('Citizen',
                            'Citizen Eco-Drive',
                            'Citizen Promaster',
                            'Citizen Chandler',
                            'Citizen L',
                            'Citizen Satellite Wave',
                            'Citizen Signature Collection',
                            'Citizen Corso',
                            'Citizen Paradigm',
                            'Citizen Brycen',
                            'Citizen Nighthawk',
                            'Узнать цены часов',
                            message)

        @bot.message_handler(func=lambda message: message.text.lower() == 'узнать цены часов')
        def prices(message):
            show_prices('Citizen Eco-Drive', '10,000 - 30,000 руб.',
                        'Citizen Promaster', '15,000 - 50,000 руб.',
                        'Citizen Chandler', '7,000 - 20,000 руб.',
                        'Citizen L', '20,000 - 60,000 руб.',
                        'Citizen Satellite Wave', '25,000 - 70,000 руб.',
                        'Citizen Signature Collection', '30,000 - 80,000 руб.',
                        'Citizen Corso', '12,000 - 40,000 руб.',
                        'Citizen Paradigm', '18,000 - 50,000 руб.',
                        'Citizen Brycen', '15,000 - 45,000 руб.',
                        'Citizen Nighthawk', '20,000 - 55,000 руб.',
                        message)

#Timex
    @bot.message_handler(func=lambda message: message.text == btn10.text)
    def models(message):
        func_for_watch_descr('Timex',
                            'Timex Expedition',
                            'Timex Weekender',
                            'Timex Ironman',
                            'Timex Fairfield',
                            'Timex Metropolitan',
                            'Timex Waterbury',
                            'Timex Marlin',
                            'Timex Standard',
                            'Timex Allied',
                            'Timex Navi',
                            'Узнать цены часов',
                            message)

        @bot.message_handler(func=lambda message: message.text.lower() == 'узнать цены часов')
        def prices(message):
            show_prices('Timex Expedition', '3,000 - 10,000 руб.',
                        'Timex Weekender', '2,000 - 7,000 руб.',
                        'Timex Ironman', '4,000 - 15,000 руб.',
                        'Timex Fairfield', '3,000 - 12,000 руб.',
                        'Timex Metropolitan', '5,000 - 20,000 руб.',
                        'Timex Waterbury', '6,000 - 25,000 руб.',
                        'Timex Marlin', '8,000 - 30,000 руб.',
                        'Timex Standard', '4,000 - 18,000 руб.',
                        'Timex Allied', '5,000 - 22,000 руб.',
                        'Timex Navi', '7,000 - 28,000 руб.',
                        message)

#Swatch
    @bot.message_handler(func=lambda message: message.text == btn11.text)
    def models(message):
            func_for_watch_descr('Swatch',
                                'Swatch Sistem51',
                                'Swatch Originals',
                                'Swatch Irony',
                                'Swatch Skin',
                                'Swatch Scuba Libre',
                                'Swatch Big Bold',
                                'Swatch X 007',
                                'Swatch X You',
                                'Swatch Art Specials',
                                'Swatch POP',
                                'Узнать цены часов',
                                message)

            @bot.message_handler(func=lambda message: message.text.lower() == 'узнать цены часов')
            def prices(message):
                show_prices('Swatch Sistem51', '5,000 - 15,000 руб.',
                            'Swatch Originals', '3,000 - 10,000 руб.',
                            'Swatch Irony', '4,000 - 12,000 руб.',
                            'Swatch Skin', '6,000 - 18,000 руб.',
                            'Swatch Scuba Libre', '7,000 - 20,000 руб.',
                            'Swatch Big Bold', '8,000 - 25,000 руб.',
                            'Swatch X 007', '10,000 - 30,000 руб.',
                            'Swatch X You', '6,000 - 15,000 руб.',
                            'Swatch Art Specials', '7,000 - 18,000 руб.',
                            'Swatch POP', '3,000 - 10,000 руб.',
                            message)

#Tissot
    @bot.message_handler(func=lambda message: message.text == btn12.text)
    def models(message):
        func_for_watch_descr('Tissot',
                            'Tissot Le Locle',
                            'Tissot T-Touch',
                            'Tissot Visodate',
                            'Tissot PRS 516',
                            'Tissot V8',
                            'Tissot Carson',
                            'Tissot Couturier',
                            'Tissot Tradition',
                            'Tissot Heritage',
                            'Tissot Seastar 1000',
                            'Узнать цены часов',
                            message)

        @bot.message_handler(func=lambda message: message.text.lower() == 'узнать цены часов')
        def prices(message):
            show_prices('Tissot Le Locle', '15,000 - 40,000 руб.',
                        'Tissot T-Touch', '30,000 - 80,000 руб.',
                        'Tissot Visodate', '20,000 - 50,000 руб.',
                        'Tissot PRS 516', '25,000 - 60,000 руб.',
                        'Tissot V8', '18,000 - 45,000 руб.',
                        'Tissot Carson', '22,000 - 55,000 руб.',
                        'Tissot Couturier', '28,000 - 70,000 руб.',
                        'Tissot Tradition', '12,000 - 35,000 руб.',
                        'Tissot Heritage', '40,000 - 100,000 руб.',
                        'Tissot Seastar 1000', '35,000 - 90,000 руб.',
                        message)

#Bulova
    @bot.message_handler(func=lambda message: message.text == btn13.text)
    def models(message):
        func_for_watch_descr('Bulova',
                            'Bulova Precisionist',
                            'Bulova Marine Star',
                            'Bulova Lunar Pilot',
                            'Bulova Curv',
                            'Bulova Accutron',
                            'Bulova Sutton',
                            'Bulova Wilton',
                            'Bulova Maquina',
                            'Bulova Computron',
                            'Bulova Aerojet',
                            'Узнать цены часов',
                            message)

        @bot.message_handler(func=lambda message: message.text.lower() == 'узнать цены часов')
        def prices(message):
            show_prices('Bulova Precisionist', '25,000 - 60,000 руб.',
                        'Bulova Marine Star', '30,000 - 70,000 руб.',
                        'Bulova Lunar Pilot', '40,000 - 90,000 руб.',
                        'Bulova Curv', '35,000 - 80,000 руб.',
                        'Bulova Accutron', '50,000 - 100,000 руб.',
                        'Bulova Sutton', '20,000 - 45,000 руб.',
                        'Bulova Wilton', '15,000 - 35,000 руб.',
                        'Bulova Maquina', '10,000 - 25,000 руб.',
                        'Bulova Computron', '25,000 - 55,000 руб.',
                        'Bulova Aerojet', '18,000 - 40,000 руб.',
                        message)

#Michael Kors
    @bot.message_handler(func=lambda message: message.text == btn14.text)
    def models(message):
        func_for_watch_descr('Michael Kors',
                            'Michael Kors Access Runway',
                            'Michael Kors Lexington',
                            'Michael Kors Parker',
                            'Michael Kors Bradshaw',
                            'Michael Kors Sofie',
                            'Michael Kors Pyper',
                            'Michael Kors Darci',
                            'Michael Kors Jaryn',
                            'Michael Kors Blair',
                            'Michael Kors Mini Slim Runway',
                            'Узнать цены часов',
                            message)

        @bot.message_handler(func=lambda message: message.text.lower() == 'узнать цены часов')
        def prices(message):
            show_prices('Michael Kors Access Runway', '15,000 - 35,000 руб.',
                        'Michael Kors Lexington', '18,000 - 40,000 руб.',
                        'Michael Kors Parker', '12,000 - 30,000 руб.',
                        'Michael Kors Bradshaw', '20,000 - 50,000 руб.',
                        'Michael Kors Sofie', '25,000 - 60,000 руб.',
                        'Michael Kors Pyper', '10,000 - 25,000 руб.',
                        'Michael Kors Darci', '22,000 - 55,000 руб.',
                        'Michael Kors Jaryn', '14,000 - 35,000 руб.',
                        'Michael Kors Blair', '28,000 - 70,000 руб.',
                        'Michael Kors Mini Slim Runway', '18,000 - 45,000 руб.',
                        message)

#DIOR
    @bot.message_handler(func=lambda message: message.text == btn15.text)
    def models(message):
        func_for_watch_descr('DIOR',
                            'DIOR VIII Montaigne',
                            'DIOR VIII Grand Bal',
                            'DIOR Chiffre Rouge',
                            'La D de DIOR',
                            'DIOR Grand Soir',
                            'DIOR Christal',
                            'DIOR Vortex',
                            'DIOR Inversé',
                            'DIOR Mini D',
                            'La Mini D de DIOR',
                            'Узнать цены часов',
                            message)

        @bot.message_handler(func=lambda message: message.text.lower() == 'узнать цены часов')
        def prices(message):
            show_prices('DIOR VIII Montaigne', '100,000 - 1,000,000 руб.',
                        'DIOR VIII Grand Bal', '150,000 - 2,000,000 руб.',
                        'DIOR Chiffre Rouge', '80,000 - 800,000 руб.',
                        'La D de DIOR', '120,000 - 1,200,000 руб.',
                        'DIOR Grand Soir', '200,000 - 2,500,000 руб.',
                        'DIOR Christal', '90,000 - 1,000,000 руб.',
                        'DIOR Vortex', '180,000 - 2,000,000 руб.',
                        'DIOR Inversé', '150,000 - 1,500,000 руб.',
                        'DIOR Mini D', '70,000 - 800,000 руб.',
                        'La Mini D de DIOR', '60,000 - 700,000 руб.',
                        message)


bot.polling(none_stop=True)

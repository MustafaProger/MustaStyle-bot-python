import telebot
from telebot import TeleBot, types

TOKEN = "6556679332:AAGd4ZDmpWh1O9luTfeUKSGXUjdAAzEPiJ4"
bot = telebot.TeleBot(TOKEN)

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


@bot.message_handler(func=lambda message: message.text == 'Rolex')
def modal_watch_handler(message):
    def func_for_watch_descr(choose_watch, model_1, model_2, model_3, model_4, model_5, model_6, model_7, model_8, model_9, model_10, about_price):
        bot.send_message(message.chat.id,  f'Отлично, {message.from_user.first_name}, ваш выбор пал на фирму {choose_watch}.')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton(model_1)
        btn2 = types.KeyboardButton(model_2)
        btn3 = types.KeyboardButton(model_3)
        btn4 = types.KeyboardButton(model_4)
        btn5 = types.KeyboardButton(model_5)
        btn6 = types.KeyboardButton(model_6)
        btn7 = types.KeyboardButton(model_7)
        btn8 = types.KeyboardButton(model_8)
        btn9 = types.KeyboardButton(model_9)
        btn10 = types.KeyboardButton(model_10)
        btn11 = types.KeyboardButton(about_price)
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)
        bot.send_message(message.chat.id, 'Теперь выберите модель часов.',  parse_mode='html', reply_markup=markup)

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
                            'Узнать цены часов')
    
    def price_modal(modal, price):
        modal = types.KeyboardButton(modal)
        price = types.KeyboardButton(price)
        

    @bot.message_handler(func=lambda message: message.text.lower() == 'узнать цены часов')
    def show_prices(message):
        rolex_watch_models = f"Rolex Submariner - 600,000 - 2,700,000 руб.\nRolex Datejust - 525,000 - 3,750,000 руб.\nRolex Day-Date - 1,875,000 - 7,500,000 руб.\nRolex GMT-Master II - 675,000 - 3,750,000 руб.\nRolex Explorer - 450,000 - 1,875,000 руб.\nRolex Yacht-Master - 825,000 - 3,750,000 руб.\nRolex Sea-Dweller - 825,000 - 1,500,000 руб.\nRolex Daytona - 975,000 - 6,000,000 руб.\nRolex Milgauss - 600,000 - 1,500,000 руб.\nRolex Oyster Perpetual - 375,000 - 1,500,000 руб.\n"
        bot.send_message(message.chat.id, rolex_watch_models)


bot.polling(none_stop=True)
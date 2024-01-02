import telebot
import random
from telebot import types
from base_watches import base_watches

TOKEN = "6556679332:AAGd4ZDmpWh1O9luTfeUKSGXUjdAAzEPiJ4"
bot = telebot.TeleBot(TOKEN)

HELP_COMMAND = """
/help - список комманд 
/start - начать работу с ботом
/about - о нас
"""

user_language = {} 

def btn_company(message, select_wat, back_lang):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
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
    btn15 = types.KeyboardButton('DIOR')

    markup.add(btn0, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, back_lang)
    bot.send_message(message.chat.id, select_wat, parse_mode='html', reply_markup=markup)


def create_company_handler(company, models):
    @bot.message_handler(func=lambda message, comp=company: message.text == comp)
    def handle_company(message):
        language = user_language.get(message.chat.id, 'russian')  
        if language == 'russian':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            buttons = [types.KeyboardButton(model) for model in models]
            back_btn = types.KeyboardButton('← Назад')
            back_lang_btn = types.KeyboardButton('← Другой язык')
            markup.add(*buttons, back_btn)

            url_markup =  types.InlineKeyboardMarkup()
            url_btns = types.InlineKeyboardButton('ОФОРМИТЬ', url='https://mustafapulse.ru/')
            url_markup.add(url_btns)

            bot.send_message(message.chat.id, f'Отлично, {message.from_user.first_name}, ваш выбор пал на фирму {company}.')
            bot.send_message(message.chat.id, 'Теперь выберите модель часов.', parse_mode='html', reply_markup=markup)
            def show_prices(message, company, models):
                formatted_prices = "\n".join(f"<b>{i + 1}. {model}</b>\n    <i>{price}</i>" for i, (model, price) in enumerate(models.items(), start=0))
                bot.send_message(message.chat.id, f"Цены на часы от {company}:\n{formatted_prices}", parse_mode='html')
            show_prices(message, company, models)

            @bot.message_handler(func=lambda message, comp=company, mods=models: message.text in [model for model in mods])
            def send_mess(message, comp=company, mods=models):
                chosen_model = next((model for model in mods if message.text == model), None)
                if chosen_model:
                    price_range = mods[chosen_model]
                    bot.send_message(message.chat.id, f"Прекрасно! Ваш выбор пал на модель часов {chosen_model}, стоимостью в пределах {price_range} в зависимости от комплектации. Хотите оформить заказ сейчас?)", reply_markup=url_markup)

            @bot.message_handler(func=lambda message: message.text.lower() == '← назад')
            def back_to_company_selection(message):
                companies = ['MystaStyle', 'Rolex', 'Omega', 'Patek Philippe', 'Audemars Piguet', 'Tag Heuer', 'Seiko',
                        'Casio', 'Fossil', 'Citizen', 'Timex', 'Swatch', 'Tissot', 'Bulova', 'Michael Kors', 'DIOR']
                random_company = random.choice(companies)
                select_watch = f"Может рассмотрим часы от {random_company}?"
                btn_company(message, select_watch, back_lang_btn)

                for company, models in base_watches.items():
                    create_company_handler(company, models)

        elif language == 'english':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            buttons = [types.KeyboardButton(model) for model in models]
            back_btn = types.KeyboardButton('← Back')
            back_lang_btn = types.KeyboardButton('← Another language')
            markup.add(*buttons, back_btn)

            url_markup =  types.InlineKeyboardMarkup()
            url_btns = types.InlineKeyboardButton('PLACE AN ORDER', url='https://mustafapulse.ru/')
            url_markup.add(url_btns)

            bot.send_message(message.chat.id, f'Great, {message.from_user.first_name}, your choice fell on the company {company}.')
            bot.send_message(message.chat.id, 'Now select the watch model.', parse_mode='html', reply_markup=markup)

            def show_prices(message, company, models):
                formatted_prices = "\n".join(f"<b>{i + 1}. {model}</b>\n    <i>{price}</i>" for i, (model, price) in enumerate(models.items(), start=0))
                bot.send_message(message.chat.id, f"Prices for watches from {company}:\n{formatted_prices}", parse_mode='html')
            show_prices(message, company, models)

            @bot.message_handler(func=lambda message, comp=company, mods=models: message.text in [model for model in mods])
            def send_mess(message, comp=company, mods=models):
                chosen_model = next((model for model in mods if message.text == model), None)
                if chosen_model:
                    price_range = mods[chosen_model]
                    bot.send_message(message.chat.id, f"Perfectly! Your choice fell on the watch model {chosen_model}, cost within the limits of {price_range} depending on the configuration. Do you want to place an order now?)", reply_markup=url_markup)

            @bot.message_handler(func=lambda message: message.text.lower() == '← back')
            def back_to_company_selection(message):
                companies = ['MystaStyle', 'Rolex', 'Omega', 'Patek Philippe', 'Audemars Piguet', 'Tag Heuer', 'Seiko',
                        'Casio', 'Fossil', 'Citizen', 'Timex', 'Swatch', 'Tissot', 'Bulova', 'Michael Kors', 'DIOR']
                random_company = random.choice(companies)
                select_watch = f"Maybe consider a watch from {random_company}?"
                btn_company(message, select_watch, back_lang_btn)

                for company, models in base_watches.items():
                    create_company_handler(company, models)


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, HELP_COMMAND)

@bot.message_handler(commands=['about'])
def about_handler(message):
    bot.send_message(message.chat.id, f'MustaStyle — ваш надежный проводник в мире элегантности и точности времени. Наша компания, основанная студентом-программистом Мустафой, сочетает в себе страсть к инновациям, высокому стилю и уважению к времени.\n\nМы специализируемся на продаже часов, которые не только служат функциональным измерителем времени, но и становятся неотъемлемой частью вашего стиля. В ассортименте MustaStyle вы найдете коллекции, вдохновленные последними трендами моды, классическим дизайном и инновационными технологиями.\n\nНаша цель - не просто предоставлять товар, а создавать уникальный опыт для наших клиентов. Мы стремимся удовлетворить запросы даже самых требовательных ценителей часов. Каждая модель внимательно отобрана и прошла тщательный контроль качества, чтобы удовлетворить ожидания даже самых искушенных покупателей.\n\nMustaStyle гордится своей преданностью качеству и предоставлению беспрецедентного уровня обслуживания. Наши сотрудники обладают глубокими знаниями в области часового искусства и всегда готовы поделиться своими знаниями, чтобы помочь вам сделать правильный выбор.\n\nПокупка часов в MustaStyle - это не просто приобретение аксессуара, но и инвестиция в свой стиль и уникальность. Доверьтесь нам, и мы сделаем ваш выбор часов незабываемым и приятным моментом.\n\nВыберите MustaStyle — выберите стиль, выберите качество, выберите надежность. Мы заботимся о вашем времени, чтобы вы могли наслаждаться каждым моментом в стиле MustaStyle.')

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Русский 🇷🇺')
    btn2 = types.KeyboardButton('English 🇬🇧')
    markup.add(btn1, btn2)
    send_mess = f'Привет, {message.from_user.first_name}.'
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
    bot.send_message(message.chat.id, 'Выберите язык.')


@bot.message_handler(func=lambda message: message.text == 'Русский 🇷🇺')
def select_watch_russian(message):
    user_language[message.chat.id] = 'russian'
    select_watch = "Теперь выберите фирму часов, которую бы вы хотели приобрести."
    back_lang_btn = types.KeyboardButton('← Другой язык')
    btn_company(message, select_watch, back_lang_btn)

    @bot.message_handler(func=lambda message: message.text.lower() == '← другой язык')
    def back(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Русский 🇷🇺')
        btn2 = types.KeyboardButton('English 🇬🇧')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, 'Выберите язык.', parse_mode='html', reply_markup=markup)


    for company, models in base_watches.items():
        create_company_handler(company, models)

    @bot.message_handler(func=lambda message: message.text.lower() == 'mystastyle')
    def models(message):

        url_markup =  types.InlineKeyboardMarkup()
        url_btns = types.InlineKeyboardButton('ОФОРМИТЬ', url='https://mustafapulse.ru/')
        url_markup.add(url_btns)

        bot.send_message(message.chat.id, 'Ух ты, MustaStyle — твой выбор! Мы с удовольствием предложим тебе уникальные часы, соответствующие твоему вкусу, цветовой гамме и бюджету. Просто расскажи нам о том, какие часы ты предпочитаешь, оставив заявку на нашем сайте, и мы обязательно свяжемся с тобой в самое ближайшее время. Доверь нам создание твоего идеального аксессуара времени!', reply_markup=url_markup)








@bot.message_handler(func=lambda message: message.text == 'English 🇬🇧')
def select_watch_english(message):
    user_language[message.chat.id] = 'english'
    select_watch = "Now select the watch company that you would like to purchase."
    back_lang_btn = types.KeyboardButton('← Another language')
    btn_company(message, select_watch, back_lang_btn)

    @bot.message_handler(func=lambda message: message.text.lower() == '← another language')
    def back(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Русский 🇷🇺')
        btn2 = types.KeyboardButton('English 🇬🇧')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, 'Выберите язык.', parse_mode='html', reply_markup=markup)

    
    for company, models in base_watches.items():
        create_company_handler(company, models)

    @bot.message_handler(func=lambda message: message.text.lower() == 'mystastyle')
    def models(message):

        url_markup =  types.InlineKeyboardMarkup()
        url_btns = types.InlineKeyboardButton('PLACE AN ORDER', url='https://mustafapulse.ru/')
        url_markup.add(url_btns)

        bot.send_message(message.chat.id, 'Wow, MustaStyle is your choice! We will be happy to offer you a unique watch that suits your taste, color scheme and budget. Just tell us which watch you prefer by leaving a request on our website, and we will contact you as soon as possible. Trust us to create your perfect time accessory!', reply_markup=url_markup)


bot.polling(none_stop=True)
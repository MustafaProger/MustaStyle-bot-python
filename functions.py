import telebot
from telebot import TeleBot, types

TOKEN = "6556679332:AAGd4ZDmpWh1O9luTfeUKSGXUjdAAzEPiJ4"
bot = telebot.TeleBot(TOKEN)

def func_for_watch_descr(choose_watch, model_1, model_2, model_3, model_4, model_5, model_6, model_7, model_8, model_9, model_10, about_price, message):
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

def show_prices(model_1, price_1, model_2, price_2, model_3, price_3, model_4, price_4, model_5, price_5, model_6, price_6, model_7, price_7, model_8, price_8, model_9, price_9, model_10, price_10, message):
    models_and_price = f"<b>1. {model_1}</b>\n    <i>{price_1}</i>\n<b>2. {model_2}</b>\n    <i>{price_2}</i>\n<b>3. {model_3}</b>\n    <i>{price_3}</i>\n<b>4. {model_4}</b>\n    <i>{price_4}</i>\n<b>5. {model_5}</b>\n    <i>{price_5}</i>\n<b>6. {model_6}</b>\n    <i>{price_6}</i>\n<b>7. {model_7}</b>\n    <i>{price_7}</i>\n<b>8. {model_8}</b>\n    <i>{price_8}</i>\n<b>9. {model_9}</b>\n    <i>{price_9}</i>\n<b>10. {model_10}</b>\n    <i>{price_10}</i>\n"
    bot.send_message(message.chat.id, models_and_price,  parse_mode='html')

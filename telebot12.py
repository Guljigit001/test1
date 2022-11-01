import telebot
from config import token
from telebot import types


bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1 = types.KeyboardButton('Выбрать модель...')
    item2 = types.KeyboardButton('Тест-Драйв')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Добрый день!. Рады приветсвовать вас в нашем автосалоне "Audi"', reply_markup=markup)
    bot.send_message(message.chat.id, 'С чем вам помочь?', reply_markup=markup)
@bot.message_handler(content_types = ['text'])
def bot_message(message):
        if message.text == 'Выбрать модель...':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            bot.send_message(message.chat.id, 'Пожалуйста, выберите категорию автомобиля.' )
            n1 = types.KeyboardButton('Audi A3 Sedan year 2021')
            n2 = types.KeyboardButton('Audi Q7')
            n3 = types.KeyboardButton('Audi S')
            markup.add(n1, n2, n3)
            bot.send_message(message.chat.id, 'Выбрите авто', reply_markup=markup)

        elif message.text == 'Audi A3 Sedan year 2021':
            bot.send_message(message.chat.id, 'Audi A3 Sedan 2021 создан,  чтобы дарить удовольствие от езды, удивлять, привлекать внимание окружающих. Каждая деталь стильного, динамичного и маневренного автомобиля указывает на его принадлежность к премиум-классу. Инновационные решения гарантируют комфорт управления и беспрецедентную безопасность.')
            photo = open('111.jpeg', 'rb')
            photo2 = open('222.jpeg', 'rb')
            photo3 = open('333.jpeg', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_photo(message.chat.id, photo2)
            bot.send_photo(message.chat.id, photo3)
            back = types.KeyboardButton('назад')
            markup.add(back)
        elif message.text == 'Audi Q7':
            bot.send_message(message.chat.id, 'Новый Audi Q7 2020 года создан разрушать \
            границы путешествий, дарить полную свободу комфорта. Автомобиль каждой деталью излучает\
            мощь и динамику, при этом поражает изысканной элегантностью. Он прекрасен не только снаружи, \
            но и внутри, обеспечивая максимум условий для наслаждения любым мгновением поездки.\
            1 Бездорожье является его стихией, о чем свидетельствует большой дорожный просвет в сочетании с полным приводом.\
            В то же время, благодаря расширенному набору опциональных настроек, внедорожник отлично приспособлен к городским условиям.\
            Узнайте больше о возможностях и новых технологиях.')
            photo = open('q7.jpeg', 'rb')
            photo2 = open('q.webp', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_photo(message.chat.id, photo2)
            back = types.KeyboardButton('назад')
            markup.add(back)
        elif message.text == 'назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('Выбрать модель...')
            item2 = types.KeyboardButton('Тест-Драйв')
            bot.send_message
bot.polling(none_stop = True)



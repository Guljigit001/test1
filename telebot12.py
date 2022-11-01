
import telebot
from config import token
from telebot import types

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton('Выбрать модель...')
    # item2 = types.KeyboardButton('Тест-Драйв')
    markup.add(item1)
    bot.send_message(message.chat.id, 'Добрый день!. Рады приветсвовать вас в нашем автосалоне "Audi"', reply_markup=markup)
    bot.send_message(message.chat.id, 'С чем вам помочь?', reply_markup=markup)
@bot.message_handler(content_types = ['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Выбрать модель...':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            bot.send_message(message.chat.id, 'Пожалуйста, выберите категорию автомобиля.' )
            n1 = types.KeyboardButton('Audi A3 Sedan year 2021')
            n2 = types.KeyboardButton('Audi Q7')
            n3 = types.KeyboardButton('Audi S3')
            back = types.KeyboardButton('Назад')
            markup.add(n1, n2, n3, back)
            bot.send_message(message.chat.id, 'Выберите  автомобиль.', reply_markup = markup)
        elif message.text == 'Audi A3 Sedan year 2021':
            bot.send_message(message.chat.id, 'У Audi A3 Sedan великолепно сбалансированная усиленная подвеска, которая обеспечивает плавный ход, выдерживает высокие нагрузки.\
            Ее жесткость можно регулировать путем установки специальных амортизаторов.\
            Автомобиль комплектуется мотором объемом 1,4 литра мощностью 150 л. с. с крутящим моментом 150 Нм.\
            Разгон с места до 100 км/ч занимает 8,7 секунды.')
            photo = open('111.jpeg', 'rb')
            photo2 = open('222.jpeg', 'rb')
            photo3 = open('333.jpeg', 'rb')
            bot.send_photo(message.chat.id, photo, '100000000 som')
            bot.send_photo(message.chat.id, photo2)
            bot.send_photo(message.chat.id, photo3)
            bot.send_message(message.chat.id, 'Audi A3 Sedan year 2021', reply_markup = markup)
        elif message.text == 'Audi Q7':
            bot.send_message(message.chat.id, 'Двигатель: турбированный дизель V6, 249 л.с.\
            АКПП: 8-ступенчатая, tiptronic.\
            Скорость, км\ч: 225.\
            Разгон до 100км/ч, с: 6,9.\
            Бак, л: 75.\
            Полный вес, кг: 3015.\
            Привод: полный привод quattro')
            photo = open('q7.jpeg', 'rb')
            photo2 = open('q.webp', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_photo(message.chat.id, photo2)
            # bot.send_message(message.chat.id, 'Audi Q7', reply_markup = markup)
        elif message.text == 'Audi S3':
            bot.send_message(message.chat.id, 'Двигатель TFSI мощностью 290 л. с.\
            позволяет Audi S3 Sedan развивать максимальную скорость 250 км/ч и быть лидером на трассе.\
            Крутящий момент 400 Н·м обеспечивает захватывающую динамику: до 100 км/ч автомобиль разгоняется всего за 4,8 с.')  
            photo = open('231.jpeg', 'rb')
            photo2 = open('2021.png', 'rb')
            photo3 = open('32.jpeg', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_photo(message.chat.id, photo2) 
            bot.send_photo(message.chat.id, photo3)

            # bot.send_message(message.chat.id, 'Audi S3', reply_markup = markup)
        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('Выбрать модель...')
            # item2 = types.KeyboardButton('Тест-Драйв')
            markup.add(item1)
            
            bot.send_message(message.chat.id, 'Вы вернулись назад', reply_markup = markup)
        else:
            bot.send_message(message.chat.id, 'К сожалению под ваш запрос нет такого автомобиля')
            back = types.KeyboardButton('Назад')
bot.polling(none_stop = True)


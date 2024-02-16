Для создания ботов для Telegram используются различные библиотеки, которые берут на себя взаимодействие с серверами Telegram и прочую
служебную функциональность, оставляя пользователю написание логики ответа на сообщения. Таких библиотек для Python множество, мы будем использовать
telebot https://github.com/eternnoir/pyTelegramBotAPI.

# ВАРИАНТ1
---------------------------------------------------------------------

import telebot                                            # в Pythonanywhere команда pip3 install --user pytelegrambotapi


token = ''                                                # Помещаем токен, который получили ранее, в переменную

bot = telebot.TeleBot(token)                              # переменная bot - ключевая во всей программе. Это объект. Внутри него уже есть функции, которые мы будем вызывать.


@bot.message_handler(content_types=["text"])              # Зарегистрировать def echo, как обработчик для каких-либо сообщений типа text (в данном случае -- всех сообщений, которые приходят).
                                                            Специальный синтаксис, который указывает, какие именно сообщения будет обрабатывать определяемая дальше функция.
    
def echo(message):                                        # Определение функции echo, принимающей один параметр - сообщение (на которое мы и будем отвечать).
    bot.send_message(message.chat.id, message.text)       # Тело функции. Отправляем сообщение в тот же чат, откуда получили (message.chat.id) с тем же текстом (message.text).


bot.polling(none_stop=True)                               # функция, polling ПОСТОЯННО ОБРАЩАЕТСЯ К СЕРВЕРАМ ТЕЛЕГРАМ - начинает отправку запросов серверам Телеграм, используя токен, и спрашивает есть ли сообщения.
                                                            Если есть обращается к обработке - def echo.



# ВАРИАНТ2
---------------------------------------------------------------------
import telebot

token = ''

bot = telebot.TeleBot(token)

my_name = 'Дима'


@bot.message_handler(content_types=["text"])
def echo(message):
    if my_name in message.text:
        text = 'Ба! Знакомые все лица'
    else:
        text = message.text
    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)

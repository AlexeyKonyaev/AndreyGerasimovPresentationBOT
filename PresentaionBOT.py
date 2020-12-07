import telebot
from telebot import types
tema = ''
istoki = ''
objom = ''
data = ''
contact = ''

bot = telebot.TeleBot("1457228435:AAG0pEUdEVx5wkJL_hdpIUeKKsyp52DXzUk")

keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row('Моё Портфолио', 'Цены на Услуги')
keyboard.row('Обо Мне', 'Заказать Презентацию')

def send(id, text):
    bot.send_message(id, text, reply_markup = keyboard)

@bot.message_handler(content_types = ['text'])
def main(message):
    id = message.chat.id
    msg = message.text

    if msg == '/start':
        send(id, 'Привет, меня зовут Андрей и я делаю крутые презентации! Пожалуйста выберите из меню ниже то, что Вы хотели бы узнать:')
    elif msg == 'Моё Портфолио':
        send(id, 'Примеры моих работ в группе: ✔https://vk.com/club194363569✔')
    elif msg == 'Цены на Услуги':
        send(id, 'ПРИМЕР РАССЧЁТА ЦЕНЫ:\r\n\r\n№1) Найти текст, вставить в презентацию, сделать нужный шрифт и его размер, напишу название каждого слайда = 200 руб. Всё это занимает 1,5-3 часа : информацию собираю с 2-4 сайтов, поэтому так долго.\r\n\r\n№1.1) Если текст надо переписать из 1,5 часовой видеолекции, то по времени это займёт 12,5 часов (1250 руб) и + 30 мин (50 руб) - поиск и вставка схем. = всего 1300 руб.\r\n\r\n№2) Сокращение текста до сути (без лишней "воды") - занимает не более 1-2 часа. (Не распространяется на №1.1). = 100 - 200 руб соответственно.\r\n\r\n№3) Проверка и подстройка текста на антиплагиат - занимает обычно от 1 до 4 дней. (Не распространяется на №1.1) = 500 руб (не по таблице).\r\n\r\n1 и 2) Основа презентации и правка текста 350руб. Найти текст, вставить в презентацию, сделать нужный шрифт и его размер, напишу название каждого слайда + Сокращение до сути (без лишней "воды"). Занимает 2-4 часа.\r\n\r\n2 и 3) Основа презентации и правка текста + проверка на антиплагиат 850руб. Найти текст, вставить в презентацию, сделать нужный шрифт и его размер, напишу название каждого слайда + Сокращение до сути (без лишней "воды") + проверка и под стройка текста на антиплагиат. Занимает обычно от 2 до 4 дней.')
    elif msg == 'Обо Мне':
        send(id, 'Я Андрей делаю презентации на заказ')
    elif msg == 'Заказать Презентацию':
        bot.send_message(message.from_user.id, 'Если вы хотите получить крутую работу, то напишите тему презентации')
        bot.register_next_step_handler(message, reg_tema)

def reg_tema(message):
    global tema
    tema = message.text
    bot.send_message(message.from_user.id, 'Рекомендованные преподавателем источники информации:')
    bot.register_next_step_handler(message, reg_istoki)

def reg_istoki(message):
    global istoki
    istoki = message.text
    bot.send_message(message.from_user.id, 'Объём работы:')
    bot.register_next_step_handler(message, reg_objom)

def reg_objom(message):
    global objom
    objom = message.text
    bot.send_message(message.from_user.id, 'Сроки выполнения работы:')
    bot.register_next_step_handler(message, reg_data)

def reg_data(message):
    global data
    data = message.text
    bot.send_message(message.from_user.id, 'Как вас зовут и ваши контактные данные:')
    bot.register_next_step_handler(message, reg_contact)



def reg_contact(message):
    global contact
    contact = message.text
    bot.send_message(message.from_user.id, 'Заявка успешно отправлена!')
    bot.send_message(chat_id = -490711905, text = "НОВАЯ ЗАЯВКА ОТ БОТА ПРЕЗЕНТАЦИЙ: " + "Тема презентации: " + tema + "; Источники информации: " + istoki + "; Объём работы: " + objom + "; Срок Выполнени: " + data + "; Клиент: "+ contact + ";")
    




bot.polling(none_stop = True)




#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telebot
from random import randrange
from os import listdir
import time

token = '501746167:AAF-pjn3bonN7EtzbpR3oi1-EYj5yTxg2Y8'
bot = telebot.TeleBot(token)
point_help = 'Выбери пункт из меню, вся информация там, комманды вводить не нужно'
contact = 'Связаться📱'
resources = 'Полезные ресурсы🔗'
d_telegram = 'Telegram: @dinarsafin'
rdsh_yt = 'https://www.youtube.com/channel/UCyuuPhmfYvyl4ly-ufSHvRw'
isSMI = False
SMI_id = 0
stickers = ['CAADAgAD9gEAAqJ7CRAVIyugSISHCQI', 'CAADAgADJAADZHFtEij6kQ-YhTDzAg']
presentation_ids = {'Гражданская активность': 'BQADAgAD4gADyodBSB8KCn37N5zTAg',
                    'Инфомационно-медийное направление': 'BQADAgAD4wADyodBSNSdzrX-cb46Ag',
                    'Личностное развитие': 'BQADAgAD3wADyodBSCXzJIEMB6xmAg',
                    'Всеросийская медиашкола РДШ': 'BQADAgAD4AADyodBSPiIexZzFppRAg'}

markup = telebot.types.ReplyKeyboardMarkup()
markup_contact = telebot.types.ReplyKeyboardMarkup()
markup_resources = telebot.types.ReplyKeyboardMarkup()
markup_presentation = telebot.types.ReplyKeyboardMarkup()

markup.row(contact)
markup.row(resources)
markup.row('Брендбук РДШ📚')
markup.row('Рабочий материал📝')

markup_contact.row('Региональный координатор РДШ РТ')
markup_contact.row('Руководитель информационно-медийного направления РДШ РТ')
markup_contact.row('Председатель РДШ РТ')
markup_contact.row('Разработчик бота')
markup_contact.row('Назад в главное меню 📝')

markup_resources.row('Официальный сайт')
markup_resources.row('YouTube', 'VK', 'Instagram')
markup_resources.row('Назад в главное меню 📝')

markup_presentation.row('Гражданская активность')
markup_presentation.row('Инфомационно-медийное направление')
markup_presentation.row('Личностное развитие')
markup_presentation.row('Всеросийская медиашкола РДШ')
markup_presentation.row('Назад в главное меню 📝')


@bot.message_handler(commands=['test'])
def find_file_ids(message):
    f = open('IM.pdf', 'rb')
    msg = bot.send_document(message.chat.id, f, None)
    bot.send_message(message.chat.id, msg.document.file_id, reply_to_message_id=msg.message_id)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, 'Для получения информации выберите пункт из меню.', reply_markup=markup)

        print(message)
    if message.text == '/help':
        bot.send_message(message.chat.id, point_help, reply_markup=markup)

        print(message)
    pass


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    global isSMI, SMI_id
    puti = '/root/telebot/RDSHa/'
    ids_file = open(puti + 'ids.txt')
    ids_file_append = open(puti + 'ids.txt', 'a')
    ids = list(map(int, ids_file.readline().split()))

    if message.chat.id not in ids:
        ids.append(message.chat.id)
        ids_file_append.write(str(ids[-1]) + " ")
    elif isSMI and message.chat.id == SMI_id:
        for id in ids:
            bot.send_message(id, message.text)
            isSMI = False

    if message.text == contact:
        bot.send_message(message.chat.id, 'Выберите с кем хотите связаться.', reply_markup=markup_contact)

    elif message.text == 'Назад в главное меню 📝':
        bot.send_message(message.chat.id, 'Для получения информации выберите пункт из меню.', reply_markup=markup)

    elif message.text == 'Региональный координатор РДШ РТ':
        bot.send_message(message.chat.id, 'Кропотина Мария Сергеевна' + '\n' + 'Тел.: +79274988892')

    elif message.text == 'Руководитель информационно-медийного направления РДШ РТ':
        bot.send_message(message.chat.id, 'Сафин Динар Рузелевич' + '\n' + 'Тел.: +79991574216' + '\n' + d_telegram)

    elif message.text == 'Председатель РДШ РТ':
        bot.send_message(message.chat.id, 'Галиев Салават Фанавиевич' + '\n' + 'Тел.: +79872966636')

    elif message.text == 'Разработчик бота':
        bot.send_message(message.chat.id, 'Фаттахов Марат Русланович' + '\n' + 'Telegram: @MRFattahov')

    elif message.text == resources:
        bot.send_message(message.chat.id, 'Выберите информациооный ресурс.', reply_markup=markup_resources)

    elif message.text == 'Официальный сайт':
        bot.send_message(message.chat.id, 'рдш.рф')

    elif message.text == 'YouTube':
        bot.send_message(message.chat.id, rdsh_yt)

    elif message.text == 'VK':
        bot.send_message(message.chat.id, 'vk.com/rdshrt')

    elif message.text == 'Instagram':
        bot.send_message(message.chat.id, 'https://www.instagram.com/rdshrt/?hl=ru')

    elif message.text == 'Брендбук РДШ📚':
        bot.send_message(message.chat.id, 'https://yadi.sk/d/CbSncvCi39KLVk')

    elif message.text == 'Рабочий материал📝':
        bot.send_message(message.chat.id, 'Выберете презентацию', reply_markup=markup_presentation)

    elif message.text in presentation_ids.keys():
        bot.send_document(message.chat.id, presentation_ids[message.text], None)

    elif message.text == 'ясми':
        isSMI = True
        SMI_id = message.chat.id

    elif message.chat.id == 246327179:
        bot.send_message(message.chat.id, 'Amir hohland')

    elif message.text == 'MvT':
        bot.send_message(message.chat.id, '👑Марат Русланович величественнее🤜🏼 Тимербулата Рашидовича')

    elif 'валентина сергеевна' in message.text.lower():
        bot.send_message(message.chat.id, 'Валентина Сергеевна лучший орагиназотар')

    else:
        bot.send_message(message.chat.id, 'Для получения информации выберите пункт из меню.', reply_markup=markup)

    print(message)
    print(len(ids))
    ids_file.close()
    ids_file_append.close()


@bot.message_handler(content_types=["sticker"])
def repeat_all_messages(message):
    bot.send_sticker(message.chat.id, stickers[randrange(2)])
    print(message.sticker.file_id)


bot.polling(none_stop=True, interval=0)

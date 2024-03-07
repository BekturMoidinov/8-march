from aiogram import types, Dispatcher
from config import bot,chat_id
from time import sleep



async def group_send_message(m: types.Message):
    while m.text != 'stop':
        while True:
            try:
                sleep(1)
                await bot.send_message(
                    chat_id=chat_id,
                    text='Поздравляем вас с 8-мартом!!!!!!!'
                )
            except Exception as e:
                pass

def register_group_filter(dp: Dispatcher):
    dp.register_message_handler(group_send_message, lambda message: message.chat.id==int(chat_id))


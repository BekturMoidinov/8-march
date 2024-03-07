from aiogram import Bot, Dispatcher
from decouple import config
PROXY_URL = "http://proxy.server:3128"
token=config('TOKEN')

chat_id=config('GROUP')

bot=Bot(token=token,proxy=PROXY_URL)
dp = Dispatcher(bot=bot)
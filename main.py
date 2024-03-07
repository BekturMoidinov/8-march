
from config import dp
from aiogram import executor, Dispatcher

from handlers import group

group.register_group_filter(dp=dp)







if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
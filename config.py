from aiogram import Bot, Dispatcher, types

TOKEN_API = "6781243626:AAF05GPR4Y1rS2Brm42kjN97tNx0UhRrC0I"
DATA_BASE = "data.db"
#1144499287 #854903492

# Инициализация бота и диспетчера
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

users = {} #Словаь юзеров

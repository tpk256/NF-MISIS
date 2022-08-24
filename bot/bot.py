from auth_data import token
import asyncio
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, OpenLink, Location, EMPTY_KEYBOARD, API, PhotoMessageUploader

bot = Bot(token = token)

photo_upd = PhotoMessageUploader(bot.api)

@bot.on.message(text = 'Начать')
@bot.on.message(payload = {'cmd': 'menu'})
async def keyboard_menu(message: Message):
	#Меню
	keyboard_menu = Keyboard()
	keyboard_menu.add(Text('Расписание', {'cmd': 'timetable'}))
	keyboard_menu.add(Text('Помощь', {'cmd': 'help'}))
	keyboard_menu = keyboard_menu.get_json()

	await message.answer('.', keyboard = keyboard_menu)

@bot.on.message(payload = {'cmd': 'timetable'})
async def keyboard_timetable(message: Message):
	#расписание
	keyboard_timetable = Keyboard()
	keyboard_timetable.add(Text('1 курс', {'cmd': 'kurs1'}))
	keyboard_timetable.add(Text('2 курс', {'cmd': 'kurs2'}))
	keyboard_timetable.row()
	keyboard_timetable.add(Text('3 курс', {'cmd': 'kurs3'}))
	keyboard_timetable.add(Text('4 курс', {'cmd': 'kurs4'}))
	keyboard_timetable.row()
	keyboard_timetable.add(Text('Назад', {'cmd': 'menu'}), color = KeyboardButtonColor.PRIMARY)
	keyboard_timetable = keyboard_timetable.get_json()

	await message.answer('.', keyboard = keyboard_timetable)

@bot.on.message(payload = {'cmd': 'kurs1'})
async def answerer_kurs1(message: Message):
	photo = await photo_upd.upload('KURS1.jpg')
	photo1 = await photo_upd.upload('KURS1_1.jpg')
	await message.answer(attachment = [photo, photo1])

@bot.on.message(payload = {'cmd': 'kurs2'})
async def answerer_kurs2(message: Message):
	photo = await photo_upd.upload('KURS2.jpg')
	photo1 = await photo_upd.upload('KURS2_1.jpg')
	await message.answer(attachment = [photo, photo1])

@bot.on.message(payload = {'cmd': 'kurs3'})
async def answerer_kurs3(message: Message):
	photo = await photo_upd.upload('KURS3.jpg')
	photo1 = await photo_upd.upload('KURS3_1.jpg')
	await message.answer(attachment = [photo, photo1])

@bot.on.message(payload = {'cmd': 'kurs4'})
async def answerer_kurs4(message: Message):
	photo = await photo_upd.upload('KURS4.jpg')
	photo1 = await photo_upd.upload('KURS4_1.jpg')
	await message.answer(attachment = [photo, photo1])

@bot.on.message(text = 'Помощь')
@bot.on.message(payload = {'cmd': 'help'})
async def help(message: Message):
	await message.answer('Если возникли проблемы, обратитесь к @vladik.kravchenko или @xpestilent')

bot.run_forever()
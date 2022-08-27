from auth_data import token, token_old
import asyncio, glob
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, OpenLink, Location, EMPTY_KEYBOARD, API, PhotoMessageUploader
from typing import Tuple
from mailing_db import *
from photo_server_upload import *
import random

#авторизация
bot = Bot(token = token)

#для загрузки фото
photo_upd = PhotoMessageUploader(bot.api)

#подгрузка блупринтов(других файлов)
#for bp in load_blueprints_from_package('blueprints'):
#	bp.load(bot)

#словарь с idшниками фото
#photos_db = fetch_photo_kurs()

#ответ на нажатие кнопки "Начать", создание клавиатуры и пейлоад меню
@bot.on.message(text = 'Начать')
@bot.on.message(payload = {'cmd': 'menu'})
async def keyboard_menu(message: Message):
	#получаю id пользователя
	user = await bot.api.users.get(message.from_id)
	user_id = user[0].id
	#добавляю пользователя в бд
	upload_user(user_id)
	#Меню
	keyboard_menu = Keyboard()
	keyboard_menu.add(Text('Расписание', {'cmd': 'timetable'}))
	keyboard_menu.add(Text('Помощь', {'cmd': 'help'}))
	keyboard_menu.row()
	keyboard_menu.add(Text('Рассылка', {'cmd': 'mailing'}))
	keyboard_menu.add(Text('Авторы', {'cmd': 'author'}))
	keyboard_menu = keyboard_menu.get_json()

	await message.answer('Меню', keyboard = keyboard_menu)

#ответ на нажатие на кнопку "Расписание"
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

	await message.answer('Выберите курс', keyboard = keyboard_timetable)

#ответ на нажатие на кнопку "рассылка"
@bot.on.message(payload = {'cmd': 'mailing'})
async def mailing_menu(message = Message):
	#создаю клавиатуру
	mailing_menu_keyboard = Keyboard()
	mailing_menu_keyboard.add(Text('Подписаться', {'cmd': 'mailing_subscribe'}))
	mailing_menu_keyboard.add(Text('Отписаться', {'cmd': 'mailing_unsubscribe'}))
	mailing_menu_keyboard.row()
	mailing_menu_keyboard.add(Text('Назад', {'cmd': 'menu'}), color = KeyboardButtonColor.PRIMARY)

	await message.answer('Вы хотите подписаться на рассылку или отписаться от рассылки?', keyboard = mailing_menu_keyboard)

#ответ на нажатие на кнопку "подписаться"
@bot.on.message(payload = {'cmd': 'mailing_subscribe'})
async def mailing_handler(message = Message):
	#создаю клавиатуру
	mailing_keyboard_sub = Keyboard()
	mailing_keyboard_sub.add(Text('1 курс', {'cmd': 'kurs1_mailing_sub'}))
	mailing_keyboard_sub.add(Text('2 курс', {'cmd': 'kurs2_mailing_sub'}))
	mailing_keyboard_sub.row()
	mailing_keyboard_sub.add(Text('3 курс', {'cmd': 'kurs3_mailing_sub'}))
	mailing_keyboard_sub.add(Text('4 курс', {'cmd': 'kurs4_mailing_sub'}))
	mailing_keyboard_sub.row()
	mailing_keyboard_sub.add(Text('Назад', {'cmd': 'mailing'}), color = KeyboardButtonColor.PRIMARY)

	await message.answer('Нажмите на курс, на рассылку которого хотите подписаться', keyboard = mailing_keyboard_sub)

#ответ на нажатие на кнопку "отписаться"
@bot.on.message(payload = {'cmd': 'mailing_unsubscribe'})
async def mailing_handler(message = Message):
	#создаю клавиатуру
	mailing_keyboard_unsub = Keyboard()
	mailing_keyboard_unsub.add(Text('1 курс', {'cmd': 'kurs1_mailing_unsub'}))
	mailing_keyboard_unsub.add(Text('2 курс', {'cmd': 'kurs2_mailing_unsub'}))
	mailing_keyboard_unsub.row()
	mailing_keyboard_unsub.add(Text('3 курс', {'cmd': 'kurs3_mailing_unsub'}))
	mailing_keyboard_unsub.add(Text('4 курс', {'cmd': 'kurs4_mailing_unsub'}))
	mailing_keyboard_unsub.row()
	mailing_keyboard_unsub.add(Text('Назад', {'cmd': 'mailing'}), color = KeyboardButtonColor.PRIMARY)

	await message.answer('Нажмите на курс, на от рассылку которого хотите отписаться', keyboard = mailing_keyboard_unsub)



#ответ на нажатие на кнопку подписки на рассылку первого курса
@bot.on.message(payload = {'cmd': 'kurs1_mailing_sub'})
async def kurs1_mailing_handler(message = Message):
	topic = 'topic1'
	#нахожу id пользователя
	user = await bot.api.users.get(message.from_id)
	user_id = user[0].id
	#добавляю подписку на первый курс пользователю
	message_answer = update_user_topics(user_id = user_id, topic = topic)
	await message.answer(f'{message_answer}')

#ответ на нажатие на кнопку подписки на рассылку второго курса
@bot.on.message(payload = {'cmd': 'kurs2_mailing_sub'})
async def kurs1_mailing_handler(message = Message):
	topic = 'topic2'
	#нахожу id пользователя
	user = await bot.api.users.get(message.from_id)
	user_id = user[0].id
	#добавляю подписку на второй курс пользователю
	message_answer = update_user_topics(user_id = user_id, topic = topic)
	await message.answer(f'{message_answer}')

#ответ на нажатие на кнопку подписки на рассылку тертьего курса
@bot.on.message(payload = {'cmd': 'kurs3_mailing_sub'})
async def kurs1_mailing_handler(message = Message):
	topic = 'topic3'
	#нахожу id пользователя
	user = await bot.api.users.get(message.from_id)
	user_id = user[0].id
	#добавляю подписку на третий курс пользователю
	message_answer = update_user_topics(user_id = user_id, topic = topic)
	await message.answer(f'{message_answer}')

#ответ на нажатие на кнопку подписки на рассылку четвёртого курса
@bot.on.message(payload = {'cmd': 'kurs4_mailing_sub'})
async def kurs1_mailing_handler(message = Message):
	topic = 'topic4'
	#нахожу id пользователя
	user = await bot.api.users.get(message.from_id)
	user_id = user[0].id
	#добавляю подписку на четвёртый курс пользователю
	message_answer = update_user_topics(user_id = user_id, topic = topic)
	await message.answer(f'{message_answer}')



#ответ на нажатие на кнопку отписки на рассылку первого курса
@bot.on.message(payload = {'cmd': 'kurs1_mailing_unsub'})
async def kurs1_mailing_handler(message = Message):
	topic = 'topic1'
	#нахожу id пользователя
	user = await bot.api.users.get(message.from_id)
	user_id = user[0].id
	#добавляю подписку на первый курс пользователю
	message_answer = delete_user_topics(user_id = user_id, topic = topic)
	await message.answer(f'{message_answer}')

#ответ на нажатие на кнопку отписки на рассылку второго курса
@bot.on.message(payload = {'cmd': 'kurs2_mailing_unsub'})
async def kurs1_mailing_handler(message = Message):
	topic = 'topic2'
	#нахожу id пользователя
	user = await bot.api.users.get(message.from_id)
	user_id = user[0].id
	#добавляю подписку на второй курс пользователю
	message_answer = delete_user_topics(user_id = user_id, topic = topic)
	await message.answer(f'{message_answer}')

#ответ на нажатие на кнопку отписки на рассылку тертьего курса
@bot.on.message(payload = {'cmd': 'kurs3_mailing_unsub'})
async def kurs1_mailing_handler(message = Message):
	topic = 'topic3'
	#нахожу id пользователя
	user = await bot.api.users.get(message.from_id)
	user_id = user[0].id
	#добавляю подписку на третий курс пользователю
	message_answer = delete_user_topics(user_id = user_id, topic = topic)
	await message.answer(f'{message_answer}')

#ответ на нажатие на кнопку отписки на рассылку четвёртого курса
@bot.on.message(payload = {'cmd': 'kurs4_mailing_unsub'})
async def kurs1_mailing_handler(message = Message):
	topic = 'topic4'
	#нахожу id пользователя
	user = await bot.api.users.get(message.from_id)
	user_id = user[0].id
	#добавляю подписку на четвёртый курс пользователю
	message_answer = delete_user_topics(user_id = user_id, topic = topic)
	await message.answer(f'{message_answer}')



#ответ на нажатие на кнопку "авторы"
@bot.on.message(payload = {'cmd': 'author'})
async def author(message: Message):
	await message.answer('Авторы: [vladik.kravchenko|Влад Кравченко]. \n Авторы старого бота: [val_kd|Валентин Казанцев] и [vladdd183|Влад Сухов]')


#ответ на нажатие на кнопку "курс 1"
@bot.on.message(payload = {'cmd': 'kurs1'})
async def answerer_kurs1(message: Message):
	#словарь с idшниками фото
	photos_db = fetch_photo_kurs()
	photos = photos_db['1']
	await message.answer(attachment = photos)

#ответ на нажатие на кнопку "курс 2"
@bot.on.message(payload = {'cmd': 'kurs2'})
async def answerer_kurs2(message: Message):
	#словарь с idшниками фото
	photos_db = fetch_photo_kurs()
	photos = photos_db['2']
	await message.answer(attachment = photos)

#ответ на нажатие на кнопку "курс 3"
@bot.on.message(payload = {'cmd': 'kurs3'})
async def answerer_kurs3(message: Message):
	#словарь с idшниками фото
	photos_db = fetch_photo_kurs()
	photos = photos_db['3']
	await message.answer(attachment = photos)

#ответ на нажатие на кнопку "курс 4"
@bot.on.message(payload = {'cmd': 'kurs4'})
async def answerer_kurs4(message: Message):
	#словарь с idшниками фото
	photos_db = fetch_photo_kurs()
	photos = photos_db['4']
	await message.answer(attachment = photos)
	#код ниже это бекап такой
	#kurs4 = file_finder(4, 'C:\\Users\\Vladik\\Downloads\\photo_files\\*')
	#kurs_dict = {}
	#photos = []
	#for i in range(len(kurs4)):
	#	kurs_dict[i] = await photo_upd.upload(f'{kurs4[i]}')
	#for i in range(len(kurs4)):	
	#	photos.append(kurs_dict[i])
	#await message.answer(attachment = photos)


#ответ на нажатие на кнопку "Помощь"
@bot.on.message(text = 'Помощь')
@bot.on.message(payload = {'cmd': 'help'})
async def help(message: Message):
	await message.answer('Если возникли проблемы, обратитесь к [vladik.kravchenko|Владу Кравченко] или [xpestilent|Мише Ермакову]')

#рассылка
@bot.on.message(text = '/mailing')
async def mailing_handler(message: Message):
	#кортеж топиков
	topics = ('topic1;', 'topic2;', 'topic3;', 'topic4;')
	#получаю id пользователя
	user = await bot.api.users.get(message.from_id)
	user_id = user[0].id
	random_number = random.randint(1, 900000000)
	if user_id == 188529333 or user_id == 461222890:
		try:
			#получаю информацию о пользователях, пользующихся ботом
			users_info = fetchall()
			#нахожу пользователей, подписанных на рассылку
			users_with_topics = []
			for user in users_info:
				if len(user[1]) > 1 and user[1] != 'подписки':
					users_with_topics.append(user)
			for user in users_with_topics:
				user_id = user[0]
				user_topics = fetch_topics(user_id)
				for user_topic in user_topics:
					if user_topic == topics[0]:
						#словарь с idшниками фото
						photos_db = fetch_photo_kurs()
						photos = photos_db['1']
						await bot.api.messages.send(user_id = user_id, attachment = photos, message = 'Рассылка!', random_id = random_number)
					if user_topic == topics[1]:
						#словарь с idшниками фото
						photos_db = fetch_photo_kurs()
						photos = photos_db['2']
						await bot.api.messages.send(user_id = user_id, attachment = photos, message = 'Рассылка!', random_id = random_number)
					if user_topic == topics[2]:
						#словарь с idшниками фото
						photos_db = fetch_photo_kurs()
						photos = photos_db['3']
						await bot.api.messages.send(user_id = user_id, attachment = photos, message = 'Рассылка!', random_id = random_number)
					if user_topic == topics[3]:
						#словарь с idшниками фото
						photos_db = fetch_photo_kurs()
						photos = photos_db['4']
						await bot.api.messages.send(user_id = user_id, attachment = photos, message = 'Рассылка!', random_id = random_number)							
		except Exception as ex:
			print(f'\n\n\nОшибка: {ex}\n\n\n')
	else:
		await message.answer('У вас нет доступа к этой команде')

#path = 'C:\\Users\\Vladik\\Downloads\\photo_files\\*'
#поиск всех фото
@bot.on.message(text = '/photos')
async def photo_upload(message: Message):
	#получаю id пользователя
	user = await bot.api.users.get(message.from_id)
	user_id = user[0].id
	if user_id == 188529333 or user_id == 461222890:
		kurs1 = file_finder(1, 'C:\\Users\\Vladik\\Downloads\\photo_files\\*')
		kurs2 = file_finder(2, 'C:\\Users\\Vladik\\Downloads\\photo_files\\*')
		kurs3 = file_finder(3, 'C:\\Users\\Vladik\\Downloads\\photo_files\\*')
		kurs4 = file_finder(4, 'C:\\Users\\Vladik\\Downloads\\photo_files\\*')
		kurses = [kurs1, kurs2, kurs3, kurs4]
		kurs_dict = {}
		photos = []
		delete_photos()
		for kurs in kurses:
			try:
				kurs_number = kurses.index(kurs) + 1
				for i in range(len(kurs)):
					kurs_dict[i] = await photo_upd.upload(f'{kurs[i]}')
				for i in range(len(kurs)):	
					photos.append(kurs_dict[i])
				upload_photo(photos, kurs_number)
				await message.answer(f'Фото для курса {kurs_number} загружены на сервер.')
			except Exception as ex:
				print(f'Ошибка: {ex}')
	else:
		await message.answer('У вас нет доступа к этой команде')

#запуск бота
bot.run_forever()
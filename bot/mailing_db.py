import sqlite3 as sql
import glob2, os

TOPIC_TRANSLATOR = {
		'topic1': 'первого',
		'topic2': 'второго',
		'topic3': 'третьего',
		'topic4': 'четвёртого'
}

#создание базы данных
def create_db():
	try:
		with sql.connect('mailing.db') as con:
			cursor = con.cursor()
			cursor.execute('''CREATE TABLE IF NOT EXISTS SUBSCRIPTIONS(
				"user_id" INTEGER NOT NULL DEFAULT 0,
				"user_topics" TEXT NOT NULL DEFAULT 'подписки')
				''')
			con.commit()
			cursor.close()
	except Exception as ex:
		print(f'Ошибка: {ex}')
	finally:
		if con:
			con.close()

#добавление пользователя в базу данных
def upload_user(user_id):
	try:
		con = sql.connect('mailing.db')
		cursor = con.cursor()
		upload_request = '''INSERT INTO SUBSCRIPTIONS ("user_id", "user_topics") VALUES (?, ?)'''
		users_id = fetch_ids()
		#проверяю нет ли такого пользователя в бд
		if user_id not in users_id:
			data = (user_id, '')
			cursor.execute(upload_request, data)
			con.commit()
			print('Пользователь добавлен')
		else:
			print('Пользователь с таким id уже есть в бд')
		cursor.close()
	except Exception as ex:
		print(f'Ошибка: {ex}')
	finally:
		if con:
			con.close()

#удаление пользователя из базы данных
def delete_user(user_id):
	try:
		con = sql.connect('mailing.db')
		cursor = con.cursor()
		delete_request = '''DELETE from SUBSCRIPTIONS where user_id = ?'''
		users_id = fetch_ids()
		#проверяю есть ли такой пользователь в бд
		if user_id in users_id:
			cursor.execute(delete_request, (user_id, ))
			con.commit()
			print('Пользователь удалён')
		else:
			print('Пользователя с таким id нет в базе данных')
		cursor.close()
	except Exception as ex:
		print(f'Ошибка: {ex}')
	finally:
		if con:
			con.close()

#редактирование подписок пользователя
def update_user_topics(user_id, topic):
	message = 'Подписки обновлены.'
	try:
		con = sql.connect('mailing.db')
		cursor = con.cursor()
		update_request = '''UPDATE SUBSCRIPTIONS SET user_topics = ? WHERE user_id = ?'''
		user_topics = fetch_topics(user_id)
		user_topics = user_topics[0][:-1].split(';')
		#вычисление topic_finally, то есть обновлённого списка подписок пользователя на курсы
		if str(type(topic)) == "<class 'str'>":
			topics_finally = (';').join(user_topics) + ';' + topic + ';'
			if topic in user_topics:
				message = 'Вы уже подписаны на этот курс!'
				topics_finally = (';').join(user_topics) + ';'
		topics_finally = topics_finally.lstrip(';')
		data = (topics_finally, user_id)
		cursor.execute(update_request, data)
		con.commit()
		#информация о курсах, на которые подписан user
		user_topics_check = fetch_topics(user_id)
		if user_topics_check != ['']:
			message += ' Теперь вы подписаны на рассылку'
			topics = topics_finally.split(';')[:-1]
			for i in range(len(topics_finally[:-1].split(';'))):
				if i == len(topics_finally[:-1].split(';')) - 1:
					message += f' {TOPIC_TRANSLATOR[topics[i]]} курса(-ов)'
					break
				message += f' {TOPIC_TRANSLATOR[topics[i]]},'
		else:
			message += ' Теперь вы не подписаны ни на одну рассылку.'
		cursor.close()
	except Exception as ex:
		print(f'Ошибка: {ex}')
	finally:
		if con:
			con.close()
	return message

#удаление топика пользователя
def delete_user_topics(user_id, topic):
	message = 'Подписки обновлены'
	try:
		con = sql.connect('mailing.db')
		cursor = con.cursor()
		update_request = '''UPDATE SUBSCRIPTIONS SET user_topics = ? WHERE user_id = ?'''
		user_topics_check = fetch_topics(user_id)
		if len(user_topics_check) > 0:
			user_topics = fetch_topics(user_id)
			user_topics = user_topics[0][:-1].split(';')
			#вычисление topic_finally, то есть обновлённого списка подписок пользователя на курсы
			if str(type(topic)) == "<class 'str'>":
				if topic in user_topics:
					user_topics.remove(topic)
					topics_finally = (';').join(user_topics) + ';'
				else:
					topics_finally = (';').join(user_topics) + ';'
					message = 'Вы не подписаны на рассылку этого курса'
		else:
			topics_finally = ''
			message = 'Вы не подписаны на рассылку этого курса'
		if len(topics_finally) == 1:
			topics_finally = ''
		data = (topics_finally, user_id)
		cursor.execute(update_request, data)
		con.commit()
		#информация о курсах, на которые подписан user
		user_topics_check = fetch_topics(user_id)
		if user_topics_check != ['']:
			message += '. Теперь вы подписаны на рассылку'
			topics = topics_finally.split(';')[:-1]
			for i in range(len(topics_finally[:-1].split(';'))):
				if i == len(topics_finally[:-1].split(';')) - 1:
					message += f' {TOPIC_TRANSLATOR[topics[i]]} курса(-ов)'
					break
				message += f' {TOPIC_TRANSLATOR[topics[i]]},'
		else:
			message += '. Теперь вы не подписаны ни на одну рассылку'
		cursor.close()
	except Exception as ex:
		print(f'Ошибка: {ex}')
	finally:
		if con:
			con.close()
	return message

#получение данных таблицы. Возвращает списов кортежей
def fetchall():
	try:
		con = sql.connect('mailing.db')
		cursor = con.cursor()
		fetchall_request = '''SELECT * from SUBSCRIPTIONS'''
		cursor.execute(fetchall_request)
		data = cursor.fetchall()
		con.commit()
		cursor.close()
	except Exception as ex:
		print(f'Ошибка: {ex}')
	finally:
		if con:
			con.close()
	return data

#извлечение id пользователей из таблицы. Возвращает список айдишников
def fetch_ids():
	data = fetchall()
	ids = []
	for record in data:
		ids.append(record[0])
	return ids

#извлечение топиков пользователя из таблицы. Возвращает список топиков
def fetch_topics(user_id):
	data = fetchall()
	topics = []
	for record in data:
		if user_id == record[0]:
			topics.append(record[1])
	return topics

#функция-поиск файлов
def file_finder(kurs_number):
	path = r"C:\Users\tpk25\Downloads\photo_files\*"
	print('\n')
	print(path)
	print('\n')
	files = glob2.glob(path)
	print('\n')
	print(f'Файлы: {files}')
	kurs = []
	path2 = path.rstrip('*')
	for file in files:
		if file[len(path2):-4][:-4] == f'KURS{kurs_number}':
			kurs.append(file)
	return kurs
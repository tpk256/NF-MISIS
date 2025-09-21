import json

from vkbottle.bot import Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, OpenLink, Location, EMPTY_KEYBOARD, Bot, PhotoMessageUploader
from vkbottle.dispatch.rules.base import TextRule, CommandRule, PayloadRule, StateRule

from config import labeler as global_labeler, BOT, db_conn
from keyboards import menu_keyboard, timetable_keyboard, parity_keyboard
from rules import CourseRule
from states import MenuStates, ScheduleStates
from utils import get_current_parity
from db import get_schedule_info, Schedule


bot: Bot = BOT.bot


@global_labeler.private_message(TextRule("Начать", ignore_case=True))
@global_labeler.private_message(PayloadRule({'cmd': 'menu'}))
async def show_menu(message: Message):

	await bot.state_dispenser.set(message.peer_id, MenuStates.MAIN_STATE, value=1)

	print(await bot.state_dispenser.get(message.peer_id))
	await message.answer('Меню', keyboard=menu_keyboard)


@global_labeler.private_message(PayloadRule({'cmd': 'timetable'}), StateRule(MenuStates.MAIN_STATE))
async def show_timetable(message: Message, ):
	await bot.state_dispenser.set(message.peer_id, ScheduleStates.WAIT_COURSE_STATE)
	await message.answer('Выберите курс', keyboard=timetable_keyboard)


@global_labeler.private_message(TextRule("Помощь", ignore_case=True))
@global_labeler.private_message(PayloadRule({'cmd': 'help'}))
async def help(message: Message):
	await message.answer('Если возникли проблемы, обратитесь к [vladik.kravchenko|Владу Кравченко] или [xpestilent|Мише Ермакову]')


@global_labeler.private_message(PayloadRule({'cmd': 'author'}))
async def authors(message: Message):
	await message.answer('Авторы: [vladik.kravchenko|Влад Кравченко]. \n Авторы старого бота: [val_kd|Валентин Казанцев] и [vladdd183|Влад Сухов]')


@global_labeler.private_message(PayloadRule({'cmd': 'mailing'}))
async def mailing_menu(message: Message):
	await message.answer('Данный функционал пока недоступен, так как переходим на telegram, по всем вопросам https://t.me/uuuuwxj')


@global_labeler.private_message(CourseRule(), StateRule(ScheduleStates.WAIT_COURSE_STATE))
async def wait_parity(message: Message):

	await bot.state_dispenser.set(
		message.peer_id,
		ScheduleStates.WAIT_PARITY_STATE,
		course=message.get_payload_json().get('course')
	)
	parity_text = "Нечетная" if get_current_parity() else "Четная"

	await message.answer(
		f"Выберите, пожалуйста, четность расписания, сейчас четность: {parity_text}",
		keyboard=parity_keyboard
	)


@global_labeler.private_message(StateRule(ScheduleStates.WAIT_PARITY_STATE))
async def get_parity(message: Message):

	parity = message.get_payload_json().get('parity')
	course = message.state_peer.payload.get('course')

	try:
		cursor = db_conn.cursor()
		schedule = get_schedule_info(
			course=course,
			parity=parity,
			cur=cursor
		)
	finally:
		cursor.close()

	if not schedule:
		await message.answer(message="Нет расписания данной четности!")
		return

	await message.answer(attachment=schedule.files_id)


@global_labeler.private_message()
async def anything(message: Message):
	await message.answer("Не понимаю вас, пожалуйста, напишите 'Начать' без кавычек")







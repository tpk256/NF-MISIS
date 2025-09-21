from vkbottle import Keyboard, KeyboardButtonColor, Text

from utils import get_current_parity


def create_menu_keyboard():
    keyboard_menu = Keyboard()
    keyboard_menu.add(Text('Расписание', {'cmd': 'timetable'}))
    keyboard_menu.add(Text('Помощь', {'cmd': 'help'}))
    keyboard_menu.row()
    keyboard_menu.add(Text('Рассылка', {'cmd': 'mailing'}))
    keyboard_menu.add(Text('Авторы', {'cmd': 'author'}))
    return keyboard_menu.get_json()


def create_timetable_keyboard():
    keyboard_timetable = Keyboard()
    keyboard_timetable.add(Text('1 курс', {'course': 1}))
    keyboard_timetable.add(Text('2 курс', {'course': 2}))
    keyboard_timetable.row()
    keyboard_timetable.add(Text('3 курс', {'course': 3}))
    keyboard_timetable.add(Text('4 курс', {'course': 4}))
    keyboard_timetable.row()
    keyboard_timetable.add(Text('Назад в меню', {'cmd': 'menu'}), color=KeyboardButtonColor.PRIMARY)
    return keyboard_timetable.get_json()


def create_parity_keyboard():
    keyboard_timetable = Keyboard()
    keyboard_timetable.add(Text('Четная неделя', {'parity': 0}))
    keyboard_timetable.add(Text('Нечетная неделя', {'parity': 1}))
    keyboard_timetable.row()
    keyboard_timetable.add(Text('Назад в меню', {'cmd': 'menu'}), color=KeyboardButtonColor.PRIMARY)
    return keyboard_timetable.get_json()


menu_keyboard = create_menu_keyboard()
timetable_keyboard = create_timetable_keyboard()
parity_keyboard = create_parity_keyboard()
from datetime import date, datetime
from calendar import monthrange

#сегодняшняя дата
week = f'{date.today()}'
week = week.split('-')

#нахожу количество дней в месяце
that_year = datetime.now().year
month = int(week[1])
days_in_month = monthrange(that_year, month)[1]

#перевожу в нужную форму
that_week = f'{week[2]}.{week[1]}.{week[0]}'

#следующий день (т.к. расписание заливается в воскресенье)
beg_week_day = int(week[2][1:]) + 1
end_week_day = beg_week_day + 5

#перевод в нужный формат
if beg_week_day < 10:
	beg_week_day = f'0{beg_week_day}'

#проверяю количество дней и перевожу на следующий месяц при необходимости
if int(beg_week_day) > days_in_month:
	number = beg_week_day - days_in_month
	beg_week_day = f'0{number}'
	beg_month = f'0{int(week[1]) + 1}'
else:
	beg_month = week[1]

if int(end_week_day) > days_in_month:
	number = end_week_day - days_in_month
	end_week_day = f'0{number}'
	end_month = f'0{int(week[1]) + 1}'
else:
	end_month = week[1]

#формирование даты начала учебной недели
beg_date = f'{beg_week_day}.{beg_month}.{week[0]}'

#формирование даты конца учебной недели
end_date = f'{end_week_day}.{end_month}.{week[0]}'
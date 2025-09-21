from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random, time
from misis_data import login, password
from date_finder import beg_date, end_date

#если нужно использовать другой user agent
#from fake_useragent import UserAgent

#ссылка на сайт нф ниту мисис, там качается excel файл с расписанием
url = 'http://nf.misis.ru/index.php/component/users/index.php?option=com_users&view=login'

#если нужно использовать другой user agent
#useragent = UserAgent()

#опции, могут и не понадобиться
options = webdriver.ChromeOptions()
#выключение webdriver
options.add_argument('--disable-blink-features=AutomationControlled')
#если нужно использовать другой user agent
#options.add_argument(f'user-agent={useragent.random}')

#создание класса Chrome(), можно использовать другие браузеры, но придётся поменять код
driver = webdriver.Chrome(
	options = options
)

#цикл загрузки excel файла
try:
	#запуск сайта
	driver.get(url = url)
	time.sleep(1)

	#авторизация на сайт
	#ввод логина
	login_input = driver.find_element(By.CLASS_NAME, 'validate-username')
	login_input.clear()
	login_input.send_keys(login)
	time.sleep(1)
	#ввод пароля
	password_input = driver.find_element(By.ID, 'password')
	password_input.clear()
	password_input.send_keys(password)
	time.sleep(1)
	#подтверждение(нажимаем на клавишу 'login')
	password_input.send_keys(Keys.ENTER)
	time.sleep(5)


	#переход на вкладку "очного расписания"
	driver.get('https://nf.misis.ru/schedule/ochnaya-forma')
	time.sleep(1)

	#скачивание excel файлов с расписанием
	#первый курс
	try:
		k1 = driver.find_element(By.XPATH, "//div[contains(@class, 'uk-panel') and contains(@class, 'uk-margin')]/p[14]/a[1]")
		k1.click()
		time.sleep(1)
	except:
		print('не могу найти расписание для первого курса')
	#второй курс
	try:
		k2 = driver.find_element(By.XPATH, "//div[@class='art-article']/p[15]/a[1]")
		k2.click()
		time.sleep(1)
	except:
		print('не могу найти расписание для второго курса')
	#третий курс
	try:
		k3 = driver.find_element(By.XPATH, "//div[@class='art-article']/p[16]/a[1]")
		k3.click()
		time.sleep(1)
	except:
		print('не могу найти расписание для третьего курса')
	#четвёртый курс
	try:
		k4 = driver.find_element(By.XPATH, "//div[@class='art-article']/p[17]/a[1]")
		k4.click()
		time.sleep(1)
	except:
		print('расписание для четвёртого курса отсутствует')

except Exception as ex:
	print(ex)
finally:
	driver.close()
	driver.quit()
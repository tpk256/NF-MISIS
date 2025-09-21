from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, random, glob, shutil
from xls_file_mover import xls_mover
from pdf_file_mover import pdf_mover
from jpg_file_mover import unarchive, jpg_renamer

# #ссылка на сайт-конвертатор excel to pdf
# url = 'https://www.ilovepdf.com/ru/excel_to_pdf'
# #ссылка на сайт-конвертатор pdf to jpg
# url2 = 'https://www.ilovepdf.com/ru/pdf_to_jpg'
#
# #перемещаю xls файлы в нужную папку
# # xls_mover()
#
# #нахожу файлы, которые нужно конвертировать
# xls_files = glob.glob('C:\\Users\\tpk25\\Downloads\\xls_files\\*')
# print(xls_files)
# #цикл конвертации excel файла в pdf файл
# for file in xls_files:
#
# 	#если нужно использовать другой user agent
# 	#user_agent = UserAgent()
#
# 	#опции
# 	options = webdriver.ChromeOptions()
#
# 	#изменение user agent
# 	#options.add_argument(f'user-agent={user_agent.random}')
#
# 	#выключение webdriver
# 	options.add_argument('--disable-blink-features=AutomationControlled')
#
# 	#создание класса Chrome(), можно использовать другие браузеры, но придётся поменять код
# 	#в executable_path нужно указать путь к вашему chrome драйверу
# 	driver = webdriver.Chrome(
# 		options = options,
# 	)
#
# 	#функция, которая загружает файл на сайт
# 	try:
# 		#запуск сайта
# 		driver.get(url = url)
# 		time.sleep(1)
#
# 		#нахожу поле для загрузки файла на сайте
# 		convert_field = driver.find_element(By.CSS_SELECTOR, 'input[type=file]')
#
# 		#загружаю файлы на сайт
# 		convert_field.send_keys(file)
# 		time.sleep(3)
#
# 		#нахожу кнопку конвертации
# 		convert_button_start = driver.find_element(By.XPATH, "//button[@id='processTask']")
# 		convert_button_start.click()
# 		time.sleep(5)
#
# 		#скачиваю pdf файл
# 		converted_file_download = driver.find_element(By.XPATH, "//a[@class='downloader__btn active']")
# 		converted_file_download.click()
# 		time.sleep(3)
#
# 	except Exception as ex:
# 		print(ex)
# 	finally:
# 		driver.close()
# 		driver.quit()

#перемещаю pdf файлы в нужную папку
# pdf_mover()
#
# #нахожу файлы, которые нужно конвертировать в фото
# pdf_files = glob.glob(r'C:\Users\tpk25\Downloads\pdf_files\*')
#
# #цикл конвертации pdf файла в jpg файлы
# for file in pdf_files:
#
# 	#если нужно использовать другой user agent
# 	#user_agent = UserAgent()
#
# 	#опции
# 	options = webdriver.ChromeOptions()
#
# 	#изменение user agent
# 	#options.add_argument(f'user-agent={user_agent.random}')
#
# 	#выключение webdriver
# 	options.add_argument('--disable-blink-features=AutomationControlled')
#
# 	#создание класса Chrome(), можно использовать другие браузеры, но придётся поменять код
# 	#в executable_path нужно указать путь к вашему chrome драйверу
# 	driver = webdriver.Chrome(
# 		options = options,
# 	)
#
# 	#функция, которая загружает файл на сайт
# 	try:
# 		#запуск сайта
# 		driver.get(url = url2)
# 		time.sleep(1)
#
# 		#нахожу поле для загрузки файла на сайте
# 		convert_field = driver.find_element(By.CSS_SELECTOR, 'input[type=file]')
#
# 		#загружаю файлы на сайт
# 		convert_field.send_keys(file)
# 		time.sleep(3)
#
# 		#нахожу кнопку конвертации
# 		convert_button_start = driver.find_element(By.XPATH, "//button[@id='processTask']")
# 		convert_button_start.click()
# 		time.sleep(5)
#
# 		#скачиваю pdf файл
# 		converted_file_download = driver.find_element(By.XPATH, "//a[@class='downloader__btn active']")
# 		converted_file_download.click()
# 		time.sleep(3)
#
# 	except Exception as ex:
# 		print(ex)
# 	finally:
# 		driver.close()
# 		driver.quit()
#
# unarchive()

jpg_renamer()

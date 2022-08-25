from selenium import webdriver
import time
import random
from fake_useragent import UserAgent
from multiprocessing import Pool

#url = 'https://www.ilovepdf.com/ru/excel_to_pdf'

#список user_agents
#user_agents_list = [
#	'HelloWorld:)',
#	'Hello~World',
#	'hello___world',
#	'HeLlO_WoRlD'
#]

useragent = UserAgent()

#объект опций
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')

#change useragent
#options.add_argument('user-agent=HelloWorld:)')
#options.add_argument(f'user-agent={random.choice(user_agents_list)}')
#options.add_argument(f'user-agent={useragent.random}')

#set proxy (нужно арендовать)
#options.add_argument('--proxy-server=176.9.113.53:7777')

#urls_list = ['https://vk.com/feed', 'https://www.youtube.com/', 'https://www.ilovepdf.com/ru/excel_to_pdf']
#
#def get_data(url):
#
#	try:
#		driver = webdriver.Chrome(
#			executable_path = 'K:\\python\\python\\selenium\\chromedriver\\chromedriver.exe',
#			options = options
#		)
#
#		driver.get(url = url)
#		time.sleep(5)
#		driver.get_screenshot_as_file(f'K:/python/python/selenium/excel_file/{url.lstrip("https://").replace("/", "")}.png')
#	except Exception as ex:
#		print(ex)
#	finally:
#		driver.close()
#		driver.quit()
#
#if __name__ == '__main__':
#	p = Pool(processes = 3)
#	p.map(get_data, urls_list)

urls_list = ['https://vk.com/feed', 'https://www.youtube.com/', 'https://www.ilovepdf.com/ru/excel_to_pdf']

def get_data(url):

	try:
		driver = webdriver.Chrome(
			executable_path = 'K:\\python\\python\\selenium\\chromedriver\\chromedriver.exe',
			options = options
		)

		driver.get(url = url)
		time.sleep(5)

	except Exception as ex:
		print(ex)
	finally:
		driver.close()
		driver.quit()

if __name__ == '__main__':
	p = Pool(processes = 3)
	p.map(get_data, urls_list)
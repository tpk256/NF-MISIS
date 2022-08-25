import glob, shutil, os

def xls_mover():
	#удаляю все файлы в папке photo_files(страховка)
	files = glob.glob('C:\\Users\\Vladik\\Downloads\\xls_files\\*')
	for file in files:
		try:
			os.remove(file)
		except Exception as ex:
			print(f'Невозможно удалить файл: {file}. Причина: {ex}')
	#можно поменять под твой пк (папка с фото) или так и оставить эту папку в загрузках
	path_destination = 'C:\\Users\\Vladik\\Downloads\\xls_files'
	files_xls = glob.glob('C:\\Users\\*\\Downloads\\*.xls')
	for file in files_xls:
		shutil.move(file, path_destination)

import glob, shutil, zipfile, os

correct_names = ['ilovepdf_pages-to-jpg', 'ilovepdf_pages-to-jpg (1)', 'ilovepdf_pages-to-jpg (2)', 'ilovepdf_pages-to-jpg (3)']

def unarchive():
	#удаляю все файлы в папке photo_files(страховка)
	files = glob.glob('C:\\Users\\Vladik\\Downloads\\photo_files\\*')
	for file in files:
		try:
			os.remove(file)
		except Exception as ex:
			print(f'Невозможно удалить файл: {file}. Причина: {ex}')
	#нахожу адреса нужных zip архивы
	path_destination = 'C:\\Users\\Vladik\\Downloads\\photo_files'
	zip_files = glob.glob('C:\\Users\\Vladik\\Downloads\\*.zip')
	for file in zip_files:
		if file.split('\\')[-1][:-4] not in correct_names:
			zip_files.remove(file)
	#перемещаю zip архивы в папку photo_files
	for file in zip_files:
		shutil.move(file, path_destination)
	#разархивация
	zip_files_new = glob.glob('C:\\Users\\Vladik\\Downloads\\photo_files\\*.zip')
	for file in zip_files_new:
		zip_file = zipfile.ZipFile(file)
		zip_file.extractall('C:\\Users\\Vladik\\Downloads\\photo_files')
		zip_file.close()
		os.remove(file)

def jpg_renamer():
	#можно поменять под твой пк (папка с фото) или так и оставить эту папку в загрузках
	path_destination = 'C:\\Users\\Vladik\\Downloads\\photo_files'
	#нахожу адреса всех файлов в папке
	jpg_files = glob.glob('C:\\Users\\Vladik\\Downloads\\photo_files\\*.jpg')
	#переименовываю фото
	path = 'C:\\Users\\Vladik\\Downloads\\photo_files\\'
	for file in jpg_files:
		photo_number = file.split('\\')[-1][:-4][-2:]
		kurs = file.split('\\')[-1][:-4][:2]
		new_filename = path + f'{kurs}_{photo_number}.jpg'
		os.rename(file, new_filename)
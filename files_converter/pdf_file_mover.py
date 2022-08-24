import glob, shutil, os

def pdf_mover():
	#удаляю все файлы в папке pdf_files(страховка)
	files = glob.glob('C:\\Users\\Vladik\\Downloads\\pdf_files\\*')
	for file in files:
		try:
			os.remove(file)
		except Exception as ex:
			print(f'Невозможно удалить файл: {file}. Причина: {ex}')
	#можно поменять под твой пк (папка с файлами) или так и оставить эту папку в загрузках
	path_destination = 'C:\\Users\\Vladik\\Downloads\\pdf_files'
	files_xls = glob.glob('C:\\Users\\Vladik\\Downloads\\xls_files\\*.xls')
	filenames_xls = list(map(lambda x: x.split('\\')[-1][:-4], files_xls))
	files_pdf = glob.glob('C:\\Users\\*\\Downloads\\*.pdf')
	i = 0
	for file in files_pdf:
		if i > len(filenames_xls) - 1:
			print('перемещение завершено')
			break
		if file.split('\\')[-1][:-4] == filenames_xls[i]:
			shutil.move(file, path_destination)
			i += 1
		else:
			pass
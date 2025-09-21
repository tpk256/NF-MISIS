import glob, shutil
import dotenv, os
dotenv.load_dotenv()


def xls_mover():
	#удаляю все файлы в папке photo_files(страховка)
	files = glob.glob(r"C:\Users\tpk25\Downloads\xls_files\*")
	for file in files:
		try:
			os.remove(file)
		except Exception as ex:
			print(f'Невозможно удалить файл: {file}. Причина: {ex}')
	#можно поменять под твой пк (папка с фото) или так и оставить эту папку в загрузках
	path_destination = r'C:\Users\tpk25\Downloads\xls_files'

	files_xls = glob.glob(r'C:\Users\*\Downloads\*.xls')
	for file in files_xls:
		shutil.move(file, path_destination)

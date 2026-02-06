import logging

# Создаем логгер
logger = logging.getLogger('UserLogger')
logger.setLevel(logging.INFO)

# Создаем обработчик файлового журнала
file_handler = logging.FileHandler('user_logs.txt')
file_handler.setLevel(logging.INFO)

# Создаем форматтер для вывода в файл
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавляем обработчик в логгер
logger.addHandler(file_handler)

# Пример использования
username = input("Введите имя пользователя: ")
logger.info(f"Пользователь {username} зашел в систему")

# Дальше можешь добавить записи в логгер при выходе пользователя и т.д.
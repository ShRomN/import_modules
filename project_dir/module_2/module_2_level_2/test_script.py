# импорт библиотеки для работы с путями
import os
# импорт библиотеки для работы с системными переменными
import sys

# Формируем переменную с абсолютным путем к папке корня проекта
root_project_directory_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..\.."))

# Добавлае полученный путь в список системной переменной PATH
sys.path.append(root_project_directory_path)

# Подключаем интересующий модуль используя путь от корня проекта
from module_1.test_m1 import TEST_VARIABLE

# Вывод импортированной переменной из модуля - module_1.test_m1
print(TEST_VARIABLE)

# Вывод справочнойт информации
print('Путь к файлу скрипта:', __file__)
print('Путь к папке со скриптом:', os.path.dirname(__file__))
print('Путь к папке на \"два уровня выше\" папки со скриптом:', os.path.join(os.path.dirname(__file__), "..\.."))
print('Абсолютный путь к папке на \"два уровня выше\" папки со скриптом:', os.path.abspath(os.path.join(os.path.dirname(__file__), "..\..")))
print('Список значений переменной PATH:', sys.path)

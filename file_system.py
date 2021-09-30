# from pathlib import Path
#
# root = Path('/')
# files = [x for x in root.iterdir() if x.is_dir()]
# for i in files:
#     print(i)

# print(os.path.exists(__file__)) пригодится для проверки на существование
# print(os.path.getatime(__file__)) пригодится для времени доступа к файлу


from os import path, listdir
import time  # временно для замера скорости
import pprint  # временно для вывода на экран


# @dict
def build_os_tree(full_path: str) -> tuple:
    path_tail = path.basename(full_path)
    if path.islink(full_path) or not path.exists(full_path):
        # print(f'ФАЙЛ НЕ СУЩЕСТВУЕТ: {full_path}')
        return '.', [0]
    if not path_tail:
        path_tail = path

    size = path.getsize(full_path)

    if path.isfile(full_path):
        return path_tail, [size]

    elif path.isdir(full_path):
        try:
            branches = listdir(full_path)
            if not branches:
                return path_tail, [size, dict()]  # dict() нужен ли?
            else:
                branches = [build_os_tree(path.join(full_path, b)) for b in branches if
                            not b.startswith('.')]  # переместить ниже if not b.startswith('.')
                for b in branches:
                    size += b[1][0]
                return path_tail, [size, dict(branches)]
        except PermissionError:
            # print('ФАЙЛ БЕЗ ДОСТУПА: ', size, path_tail)

            return '.', [0]
            # return path_tail, [size]  # '.', 0 - чтобы после исключилось
    else:
        # print('ФАЙЛ ИНОГО ТИПА: ', size, path_tail)

        return '.', [0]
        # return path_tail, [size]  # '.', 0 - чтобы после исключилось


# root_dir = '/'
root_dir = '/Users/dumanskij/Документы Mac/СПбГЭУ/PROGI/GIT all/file_explorer_project'  # временно
print('---ПРОЦЕСС НАЧАТ---')
start_time = time.time()
os_tree = dict([build_os_tree(root_dir)])
print('---ПРОЦЕСС ЗАВЕРШЕН---')
print("--- %s seconds ---" % (time.time() - start_time))

# pprint.PrettyPrinter().pprint(os_tree)  # временный вывод

# print(path.getsize('/Users/dumanskij/Документы Mac/СПбГЭУ/PROGI/GIT all/tradeBot_project/dist'))  # временно
# print(515879226 - 516816458)  # временно

# --- КОММЕНТАРИИ ---
# сделать сортировку по размеру и фильтровать скрытые только после учета их размеров
# добавить округление размера файла на 2 этапах и последнее время доступа к файлу

# добавить проверку на удаляемость
# отображать значок папка

# сделать в ООП как одно из деревьев

# выяснить, какие типы файлов встречаются

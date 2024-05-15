
#Если использовать вместо list set, то результат будет верным,
# но не совпадать с примером из задания
folders = ['root/a', 'root/a/b', 'root/c/x', 'root/a/b/c', 'root', 'root/c']
start_dir = min(folders, key = len)
folders.remove(start_dir) 
folders_1 = dict()
space = ' '
space_count = 0

#проверка входных данных
for z in folders:
    #Разбивает на отдельные буквы и сочетания
    test_str = z.split('/')
    for t in test_str:
        #Проверка условий
        if t.islower() != True or len(t) > 10:
            print('Входные данные не прошли проверку, отмена')
            exit()

#Ловим корневой каталог
for i in folders:
    if i.count('/') == 1:
        folders_1[i] = []

#Собираем все возможные дальнейшие направления путей
for m in folders:
    for key in folders_1:
        if key == m:
            pass
        if key in m:
            folders_1[key].append(m)

#Пересортировываем по длине чтобы удобно было потом преобразовать
for key1,value in folders_1.items():
    folders_1[key1] = sorted(value, key=len)

#Выводим корневой каталог
print(start_dir)
for key2,value in folders_1.items():
    #Будем подсчитывать кол-во пробелов для вывода
    space_count = 0
    for value1 in value:
        space_count += 1
        #Если это первый после корня каталог
        if value1.count('/') == 1:
            print(space*space_count + value1.replace(start_dir + '/', ''))
            last_element = value1
            continue
        #Остальные после первого каталога
        print(space*space_count + value1.replace(last_element+ '/', ''))
        last_element = value1
        
#print(folders_1)





# Пьянков Михаил Феликсович
## date :: 09.12.24
## grade :: хорошо

В ходе выполнения работы было произведено исследование, в ходе которого было принято решение использовать хэш-таблицу для выполнения поставленной задачи. Соответственно была реализована структура данных: хэш-таблица.

[Полный код работы](https://github.com/moevm/alg-2024-3384/pull/95/files)

## Задание на защиту

1) Добавить команду help в CLI.
2) Вынести CLI в отдельную функцию.
3) Реализовать механизм сохранения (сериализацию) данных программы вместе с цифровой подписью, защищающей данные от редактирования вне программы.

## Выполнение задания
### Идея выполнения

1) Функцию help добавим также, как и остальные команды, которые уже присутствуют в программе.
2) Вынесем CLI в отдельную функцию.
3) Сохранять данные будем в текстовый файл, первые четыре строки файла будут содержать информацию о полях хэш-таблицы: max_size, max_chain_length, current_size, max_load соответственно. Остальные строки, за исключением последней будут хранить информацию о студентах в виде "ID;name;age;special". В последней строке будет содержаться цифровая подпись, которая в данном случае является хэшем всех данных с полиномиальной функцией хэширования. Таким образом будут предотвращены попытки редактировать данные вне программы и загружать их в программу.

### Исполнение в коде

1) Добавлено в функцию CLI команда help:
```python
commands = ['insert', 'search', 'erase', 'update', 'exit', 'print', 'save', 'help', 'load']
```
```python
        elif command == 'help':
            print('Перечень команд: insert, search, erase, update, exit')
            print('insert: после команды вам будет необходимо ввести имя, возраст (число) и специальность студента для добавления')
            print('search: введите ID студента, которого необходимо найти')
            print('erase: введите ID студента, которого необходимо удалить')
            print('update: после команды вам будет необходимо ввести имя, возраст (число) и специальность студента для обновления')
            print('exit: команда выполняет выход из программы')
            print('save: команда выполняет сохранение базы данных в файл')
            print('load: команда выполняет загрузку в базу данных из файла')
            print('help: команда выводить информацию о командах')
```

2) Вынесение CLI в отдельную функцию:
```python
def interface(hashTable: HashTable, file_name = 'Database.txt'):
```

3) Добавлены функциии save и load, также команды добавлены в CLI, данные будут сохранятся в файл 'Database.txt':

```python
def save(self, file_name = 'Database.txt'):
    file = open(file_name, 'w')
    file_hash = 0
    p_numbers = 53
    p_student = 181
    file.write(str(self.max_size) + '\n')
    file.write(str(self.max_chain_length) + '\n')
    file.write(str(self.current_size) + '\n')
    file.write(str(self.max_load) + '\n')

    mlp_numbers = 1
    file_hash += self.max_size * (p_numbers ** mlp_numbers)
    mlp_numbers += 1
    file_hash += self.max_chain_length * (p_numbers ** mlp_numbers)
    mlp_numbers += 1
    file_hash += self.current_size * (p_numbers ** mlp_numbers)
    mlp_numbers += 1
    file_hash += self.max_load * (p_numbers ** mlp_numbers)
    mlp_numbers += 1

    for i in self.data:
        if i is not []:
            for j in i:
                ID, student = j[0], j[1]
                student_data = [ID, student.full_name, student.age, student.special]
                save_string = ';'.join(map(str,student_data))
                file.write(save_string + '\n')
                file_hash += sum([ord(str(save_string[i])) * (p_student ** i) for i in range(len(save_string))])

    file.write(str(file_hash))
    file.close()
```
```python
def load(self, file_name = 'Database.txt'):
    try:
        file = open(file_name, 'r')
    except Exception:
        print('Нет файла для выполнения загрузки')
        return 0

    file_hash = 0
    p_numbers = 53
    p_student = 181
    max_size = int(file.readline()[:-1])
    max_chain_length = int(file.readline()[:-1])
    current_size = int(file.readline()[:-1])
    max_load = float(file.readline()[:-1])

    mlp_numbers = 1
    file_hash += max_size * (p_numbers ** mlp_numbers)
    mlp_numbers += 1
    file_hash += max_chain_length * (p_numbers ** mlp_numbers)
    mlp_numbers += 1
    file_hash += current_size * (p_numbers ** mlp_numbers)
    mlp_numbers += 1
    file_hash += max_load * (p_numbers ** mlp_numbers)
    mlp_numbers += 1

    ids = []
    students = []
    lines = file.readlines()
    for i in  lines[:-1]:
        load_str = i[:-1]
        file_hash += sum([ord(load_str[i]) * (p_student ** i) for i in range(len(load_str))])
        load_str = load_str.split(';')
        ID = load_str[0]
        name = load_str[1]
        age = int(load_str[2])
        special = load_str[3]
        student = Student(name, age, special)
        ids.append(ID)
        students.append(student)

    load_hash = float(lines[-1])
    file.close()
    if file_hash == load_hash:
        print('Цифровые подписи соответствуют')
    else:
        print('Цифровые подписи не соответствуют')
        return 0
    self.max_size = max_size
    self.max_chain_length = max_chain_length
    self.current_size = current_size
    self.max_load = max_load
    for i in range(len(ids)):
        self.insert(ids[i], students[i])
    return 1
```

Все изменения можно посмотреть [здесь](https://github.com/moevm/alg-2024-3384/pull/95/files#diff-f361c8c39911d0c698538021a51f2b8e35e2a9225f9a8ce0c72f2cfc2f02e1cb)
class Student:
    def __init__(self, full_name: str, age: int, special: str):
        self.full_name = full_name
        self.age = age
        self.special = special

    def __eq__(self, other):
        if other is None:
            return 0
        return self.age == other.age and self.full_name == other.full_name and self.special == other.special

    def __str__(self) -> str:
        return f'имя: {self.full_name}, возраст: {self.age}, специальность: {self.special}'


class HashTable:
    def __init__(self, max_size=997, max_load=0.75, max_chain_length=3):
        self.max_size = max_size
        self.current_size = 0
        self.max_load = max_load
        self.max_chain_length = max_chain_length
        self.data = [[] for _ in range(self.max_size)]

    def load_factor(self) -> float:
        return self.current_size / self.max_size

    def hash_function(self, key: str) -> int:
        p = 97
        key_hash = 0
        key_hash += sum([ord(key[i]) * (p ** i) for i in range(len(key))])
        return key_hash % self.max_size

    def __re_balance__(self):
        old_data = self.data
        self.max_size *= 2
        self.data = [[] for _ in range(self.max_size)]
        self.current_size = 0
        for chain in old_data:
            for student in chain:
                self.insert(student[0], student[1])

    def insert(self, student_id: str, student: Student):
        key_hash = self.hash_function(student_id)
        for i in self.data[key_hash]:
            if i[0] == student_id:
                print('Студент с таким ID уже есть!')
                return 0
        self.data[key_hash].insert(0,[student_id, student])
        self.current_size += 1

        if self.load_factor() > self.max_load:
            self.__re_balance__()
        return 1

    def erase(self, student_id: str):
        key_hash = self.hash_function(student_id)
        if self.data[key_hash] is []:
            print('Нет студента с таким ID!')
            return 0
        for i in range(len(self.data[key_hash])):
            if self.data[key_hash][i][0] == student_id:
                self.data[key_hash].pop(i)
                self.current_size -= 1
                return 1
        print('Нет студента с таким ID!')
        return 0

    def update(self, student_id: str, student: Student):
        key_hash = self.hash_function(student_id)
        if self.data[key_hash] is []:
            print('Нет студента с таким ID!')
            return 0
        for i in range(len(self.data[key_hash])):
            if self.data[key_hash][i][0] == student_id:
                self.data[key_hash][i][1] = student
                return 1
        print('Нет студента с таким ID!')
        return 0

    def search(self, student_id: str):
        key_hash = self.hash_function(student_id)
        if self.data[key_hash] is []:
            return None
        else:
            for i in range(len(self.data[key_hash])):
                if self.data[key_hash][i][0] == student_id:
                    return self.data[key_hash][i][1]
        return None

    def __str__(self) -> str:
        res = ''
        for i in range(self.max_size):
            for j in range(len(self.data[i])):
                res += 'ID: ' + self.data[i][j][0] + ' ' + self.data[i][j][1].__str__() + '\n'
        if res != '':
            return res[:-1]
        else:
            return 'Empty'

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


def student_input():
    name = input('Введите имя студента: ')
    age = input('Введите возраст студента: ')
    special = input('Введите специальность студента: ')
    while True:
        try:
            age = int(age)
            break
        except Exception:
            print('Ошибка, вы неверно ввели возраст студента!')
            age = input('Введите возраст студента: ')
    student = Student(name, age, special)
    return student

def interface(hashTable: HashTable, file_name = 'Database.txt'):
    print('Программа для администирования базы данных студентов, команды: [insert, search, erase, update, exit, help]')
    print('Сначала введите наименование команды, далее следуйте указаниям, появившимся в консоли')
    print('Для подробностей введите команду help')
    command = ''
    commands = ['insert', 'search', 'erase', 'update', 'exit', 'print', 'save', 'help', 'load']
    while command != 'exit':
        command = input()
        while not (command in commands):
            print('Вы ввели неверную команду, попробуйте снова!')
            command = input()

        if command == 'exit':
            exit()
        elif command == 'insert':
            student = student_input()
            ID = input('Введите ID, по которому вы хотите добавить студента: ')
            flag = hashTable.insert(ID, student)
            if flag:
                print('Добавление успешно выполнено')
            else:
                print('Добавление не было выполнено')
        elif command == 'search':
            ID = input('Введите ID, по которому вы хотите найти студента: ')
            if hashTable.search(ID) == None:
                print('Нет студента с таким ID')
            else:
                print(hashTable.search(ID))
        elif command == 'erase':
            ID = input('Введите ID, по которому вы хотите удалить студента: ')
            flag = hashTable.erase(ID)
            if flag:
                print('Удаление успешно выполнено')
            else:
                print('Удаление не было выполнено')
        elif command == 'update':
            ID = input('Введите ID, по которому вы хотите обновить данные студента: ')
            student = student_input()
            flag = hashTable.update(ID, student)
            if flag:
                print('Обновление успешно выполнено')
            else:
                print('Обновление не было выполнено')
        elif command == 'print':
            print('Вывод всей базы данных:')
            print(hashTable)
        elif command == 'save':
            hashTable.save(file_name)
            print(f'Данные сохранены в: {file_name}')
        elif command == 'load':
            flag = hashTable.load(file_name)
            if flag:
                print(f'Данные загружены из: {file_name}')
            else:
                print(f'Ошибка загрузки данных')
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

if __name__ == '__main__':
    hashTable = HashTable()
    interface(hashTable)

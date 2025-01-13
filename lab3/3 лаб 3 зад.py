def ReadFile(file, type):
    open_file=open(file, 'r', encoding='utf8')
    if type=='полностью':
        with open_file as i:
            context=open_file.read()
            return context
    elif type=='построчно':
        with open_file as i:
            for e in open_file:
                return e
try:
    print(ReadFile('C:/Users/barsi/PycharmProjects/pythonProject/exaple.txt', 'полностью'))
except FileNotFoundError:
    print('Не удалось найти указанный файл')


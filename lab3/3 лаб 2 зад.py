def AddStr(char):
    file=open('user_input.txt', 'a', encoding='utf8')
    with file as i:
        file.write(char)

print(AddStr('текст'))
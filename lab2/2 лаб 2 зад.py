def describe_person(name, age=30):
    return 'Имя: '+ name + ', ' + 'Возраст: '+ str(age)

print(describe_person('Имя', 20))
print(describe_person('Имя'))

# Ввод переменных при помощи input

username = input("Введите Ваше имя ")
title = input("Введите заголовок заметки ")
under_title1 = input("Введите первый подзаголовок заметки ")
under_title2 = input("Введите второй подзаголовок заметки ")
status = input("Задайте статус заметки в формате done/undone ")
content = input("Введите содержание заметки ")
created_date = input("Введите дату создания заметки в формате дд-мм-гггг ")
issue_date = input("Введите дату дедлайна для задачи в формате дд-мм-гггг ")

list_of_titles=[title, under_title1, under_title2] # Создание списка с заголовками

# Вывод
print ("Имя пользователя: ", username, end=";\n")
print("Заголовок заметки: ", title, end=";\n")
print("Первый подзаголовок заметки ", under_title1)
print("Второй подзаголовок заметки ", under_title2)
print("Описание заметки: ", content, end=";\n")
print("Статус заметки: ", status, end=";\n")
print("Дата создания: ", created_date, end=";\n")
print("Дедлайн: ", issue_date, end=".\n")

print(list_of_titles)

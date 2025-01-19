#Объединение всех переменных в список

username = input("Введите Ваше имя ")
title = input("Введите заголовок заметки ")
under_title1 = input("Введите первый подзаголовок заметки ")
under_title2 = input("Введите второй подзаголовок заметки ")
status = input("Задайте статус заметки в формате done/undone ")
content = input("Введите содержание заметки ")
created_date = input("Введите дату создания заметки в формате дд-мм-гггг ")
issue_date = input("Введите дату дедлайна для задачи в формате дд-мм-гггг ")


list_of_titles=[title, under_title1, under_title2] # Создание списка с заголовками

note=[username, status, content, created_date, issue_date, list_of_titles] # Создание списка со всеми данными

print(note, sep='\n') # Вывод списка со всеми данными

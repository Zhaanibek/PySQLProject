# -*- coding: utf-8 -*-

from database import Session
from crud import add_user, get_user_by_username, update_user_password, delete_user, get_top_3_students


def main_menu():
    print('Добро пожаловать!')
    user_input = input(f'Меню:\n'
                       f'1. Вход\n'
                       f'2. Регистрация\n'
                       f'q. Выйти из приложения\n'
                       f'Вы выбрали: ')
    return user_input


def logged_in_menu():
    print('Выберите действие:')
    user_input = input(f'Меню:\n'
                       f'1. Сменить пароль\n'
                       f'2. Удалить аккаунт\n'
                       f'3. Топ три класса\n'
                       f'q. Выйти\n'
                       f'Вы выбрали: ')
    return user_input


with Session() as session:
    while True:
        user_input_main = main_menu()

        if user_input_main == '1':
            username = input("Введите ваше имя: ")
            password = input("Введите ваш пароль: ")

            current_user = get_user_by_username(session, username)

            if current_user and current_user.password == password:
                print(f"Вы успешно зашли от имени {current_user.username}!\n")
                while True:
                    user_input_logged_in = logged_in_menu()
                    if user_input_logged_in == '1':
                        new_password = input("Введите новый пароль: ")
                        update_user_password(session, username, new_password)
                        try:
                            session.commit()
                            print("Пароль успешно изменен!\n")
                        except:
                            print("Ошибка при изменении пароля!\n")
                            session.rollback()
                    elif user_input_logged_in == '2':
                        confirm = input("Вы уверены, что хотите удалить свой аккаунт? (y/n): ")
                        if confirm.lower() == 'y':
                            delete_user(session, username)
                            try:
                                session.commit()
                                print("Аккаунт успешно удален!\n")
                            except:
                                print("Ошибка при удалении аккаунта!\n")
                                session.rollback()
                            break
                        else:
                            print("Удаление аккаунта отменено.\n")
                    elif user_input_logged_in == '3':
                        top_3_students = get_top_3_students(session)
                        for idx, (student, avg_score) in enumerate(top_3_students, start=1):
                            print(f"Top {idx} Student: {student.name}, Average Score: {avg_score}")

                    elif user_input_logged_in == 'q':
                        print('Вы успешно вышли!')
                        break
                    else:
                        print("Неверный ввод.\n")
            else:
                print("Не удалось войти. Пожалуйста, проверьте имя пользователя и пароль.\n")

        elif user_input_main == '2':
            new_username = input(f"Имя нового пользователя: ")
            new_password = input(f"Пароль нового пользователя: ")

            add_user(session, username=new_username, password=new_password)

            try:
                session.commit()
                print('Регистрация прошла успешно!\n')

            except:
                print('Ошибка регистрации!\n')
                session.rollback()

        elif user_input_main == 'q':
            print('Вы успешно вышли из приложения!')
            break

        else:
            print("Неверный ввод.\n")

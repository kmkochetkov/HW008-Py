# Модуль контроллера действий пользователя

import teacher, pupil
from data import load, save


def controller():
    load()
    print('Вы учитель [1]\nили \nученик     [2]\n > :\n')
    act = input()
    if act == '1':
        option= 1
        while option == 1:
            print('Выберите действие:\nдобавление ученика(цы) [1]\nдобавление оценки      [2]\nвыход                  [3]\n> :')
            act = input()
            if act == '1':
                teacher.add_pupil()
            if act == '2':
                teacher.add_mark()
            if act == '3':
                option = 0
            else:
                save()
                controller()
    elif act == '2':
        option = 1
        while option == 1:
            last_name = input('Введите фамилию ученика(цы)\n либо введите [0] для выхода \n> : ')
            if last_name == '0':
                option = 0
            else:
                pupil.see_result(last_name)
        controller()
    else:
        print('Ошибочный ввод. Повторите, пожалуйста')
        controller()


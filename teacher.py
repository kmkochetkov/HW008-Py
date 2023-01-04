import data
def add_pupil():
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    group = input("Введите класс: ")
    data.add_pupil([surname, name, group])


def add_mark():
    last_name = input("Введите фамилию ученика: ")
    subject = input("Введите предмет: ")
    mark = input("Введите оценку или оценки через пробел: ").split()
    data.add_mark(last_name, subject, mark)
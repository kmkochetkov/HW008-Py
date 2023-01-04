# #
# #
# #

import json
import os

def add_pupil(data):
    pupil_data[data[0]] = data[1:], {}


def add_mark(last_name, lesson, score):
    if pupil_data.get(last_name) is None:
        print(f'Ученик {last_name} не найден.')
    else:
        if lesson in pupil_data[last_name][1]:
            pupil_data[last_name][1][lesson].extend(score)
        else:
            pupil_data[last_name][1][lesson] = score



def get_pupil(last_name):
    if pupil_data.get(last_name) is None:
        print(f'Ученик {last_name} не найден.')
    else:
        data = pupil_data[last_name]
        print(f'{last_name}{",".join(data[0])}:')
        print(*[f'{key}: {",".join(value)}' for key, value in data[1].items()], sep='\n')



def save():
    json.dump(pupil_data, open('pupil_data.json', 'w'))


def load():
    global pupil_data
    if os.stat('pupil_data.json').st_size == 0:
        pupil_data = {}
    else:
        pupil_data = json.load(open('pupil_data.json'))

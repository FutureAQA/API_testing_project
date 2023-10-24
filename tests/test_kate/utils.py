import json


def file_read(file):
    f = open(file, 'r', encoding='utf-8')
    j = json.load(f)
    return j

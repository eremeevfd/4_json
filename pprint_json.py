# -*- coding: utf-8 -*-
import json
from pprint import pprint

def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as data_file:
        data_file = json.load(data_file, encoding='utf-8')
    return data_file


def pretty_print_json(data):
    pprint(data)

if __name__ == '__main__':
    path = input()
    data = load_data(path)
    pretty_print_json(data)

# -*- coding: utf-8 -*-
import json
import os


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as data_file:
            data_file = json.load(data_file)
            return data_file


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    path = input("Введите путь к файлу, который хотите вывести красиво: ")
    data = load_data(path)
    pretty_print_json(data)
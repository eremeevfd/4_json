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
    pretty_printnig_json_file_path = input("Enter path to file you want to pretty print: ")
    opened_json_file = load_data(pretty_printnig_json_file_path)
    pretty_print_json(opened_json_file)
#!/usr/bin/python3

import csv
import json


def convert_csv_to_json(filename):
    try:
        with open(filename, "r", encoding='utf-8') as csvfile:
            data = list(csv.DictReader(csvfile))
        with open('data.json', "w", encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)
        return True
    except FileNotFoundError:
        return False

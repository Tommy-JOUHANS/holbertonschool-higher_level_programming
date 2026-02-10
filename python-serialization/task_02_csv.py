#!/usr/bin/python3
"""Module for the objective of this exercise is to gain experience
 in reading data from one format (CSV) and converting
 it into another format (JSON) using serialization techniques.

 """

import csv
import json


def convert_csv_to_json(csv_file):
    """Reads data from a CSV file, converts it to JSON format,
     and saves it to a new file named 'data.json'."""

    try:
        with open(csv_file, mode='r') as file:
            csv_reader = csv.DictReader(file)
            data = list(csv_reader)

        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)
        return True
    except Exception:
        print("file not found")
        return False

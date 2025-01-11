import csv
import json

def csv_to_json(csv_file, json_file):
  with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)

    data = list(reader)

  with open(json_file, 'w') as f:
    json.dump(data, f, indent=4)

csv_to_json('mic_data.csv', 'data.json')
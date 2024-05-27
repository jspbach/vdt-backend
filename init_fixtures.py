import csv
import json

"""Run this code to generate fixtures."""

def csv_to_json_fixture(model_name, csv_file_path, json_file_path):
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        data = []
        for i, row in enumerate(reader, start=1):
            data.append({
                "model": model_name,
                "fields": {
                    "full_name": row['Họ và tên'],
                    "gender": row['Giới tính'],
                    "institution": row['Trường']
                }
            })
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)

csv_to_json_fixture("members.Member", "./data/mock_data.csv", "./apiserver/fixtures/members.json")

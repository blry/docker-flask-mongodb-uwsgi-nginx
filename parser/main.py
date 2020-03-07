import os
from pymongo import MongoClient
from hashlib import md5
from openpyxl import load_workbook
from bson.objectid import ObjectId
import datetime
import re


def main():
    parsed_files_col, parsed_records_col = get_working_collections()
    parsed_files = list(parsed_files_col.find())
    all_files = get_all_files('xlsx')
    print('Found %d files in xlsx dir:' % len(all_files))

    for file in all_files:
        if file not in parsed_files:
            print('%s is processing' % file['path'])
            records = parse_records(file['path'])
            parsed_records_col.insert_many(records)
            parsed_files_col.insert_one(file)
            print('Done. Added %d records' % len(records))
        else:
            print('%s is already processed' % file['path'])

    print('Finished!')


def get_working_collections():
    mongodb_user = os.getenv('MONGO_INITDB_ROOT_USERNAME')
    mongodb_pwd = os.getenv('MONGO_INITDB_ROOT_PASSWORD')
    client = MongoClient('mongodb://%s:%s@mongodb' % (mongodb_user, mongodb_pwd))

    mongodb_db_name = os.getenv('MONGO_INITDB_DATABASE')
    db = client[mongodb_db_name]

    return db.parsed_file_hashes, db.parsed_records


def get_all_files(path):
    files = []

    with os.scandir(path) as entries:
        for entry in entries:
            entry_path = os.path.abspath(entry)
            if entry.is_file() and os.path.splitext(entry_path)[1] == '.xlsx':
                file_hash = md5(entry_path.encode()).hexdigest()[:24]
                files.append({'_id': ObjectId(file_hash), 'path': entry_path})
            elif entry.is_dir():
                files += get_all_files(entry_path)

    return files


def get_week_dates(string):
    dates = [date.split('-') for date in re.findall(r'\d+-\d+-\d+', string)]

    week_start = [int(numeric_string) for numeric_string in dates[0]]
    week_start = datetime.datetime(year=week_start[2], month=week_start[0], day=week_start[1])
    week_end = [int(numeric_string) for numeric_string in dates[1]]
    week_end = datetime.datetime(year=week_end[2], month=week_end[0], day=week_end[1])

    return week_start, week_end


def parse_records(path):
    records = []
    workbook = load_workbook(path, True)

    for worksheet in workbook.worksheets:
        week_start, week_end = get_week_dates(worksheet.cell(row=3, column=1).value)
        record = {'week_start': week_start, 'week_end': week_end}
        row = 6
        while True:
            row += 1
            name = worksheet.cell(row=row, column=1).value or worksheet.cell(row=row, column=2).value
            if name is None or name == '':
                break
            if 'Total' in name:
                continue

            record[name.replace('.', '').replace('$', '')] = int(worksheet.cell(row = row, column=3).value)

        records.append(record)

    return records


if __name__ == '__main__':
    main()

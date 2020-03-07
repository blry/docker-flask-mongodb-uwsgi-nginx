import os
from hashlib import md5
from bson.objectid import ObjectId
import datetime as dt
import re


def all_files(path):
    files = []

    with os.scandir(path) as entries:
        for entry in entries:
            entry_path = os.path.abspath(entry)
            if entry.is_file() and os.path.splitext(entry_path)[1] == '.xlsx':
                file_hash = md5(entry_path.encode()).hexdigest()[:24]
                files.append({'_id': ObjectId(file_hash), 'path': entry_path})
            elif entry.is_dir():
                files += all_files(entry_path)

    return files


def week_dates(string):
    dates = [date.split('-') for date in re.findall(r'\d+-\d+-\d+', string)]

    week_start = [int(numeric_string) for numeric_string in dates[0]]
    week_start = dt.datetime(year=week_start[2], month=week_start[0], day=week_start[1])
    week_end = [int(numeric_string) for numeric_string in dates[1]]
    week_end = dt.datetime(year=week_end[2], month=week_end[0], day=week_end[1])

    return week_start, week_end


def test_week_dates():
    week_start, week_end = week_dates('Week 31 (Q3) From: 07-31-2016 To: 08-06-2016')
    assert week_start == dt.datetime(year=2016, month=7, day=31)
    assert week_end == dt.datetime(year=2016, month=8, day=6)


if __name__ == '__main__':
    test_week_dates()

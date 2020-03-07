import os
from pymongo import MongoClient


def find_records_in(parsed_records_col, week_start, week_end):
    result = parsed_records_col.aggregate([
        {'$match': {
            '$and': [{'week_start': {'$gte': week_start}}, {'week_end': {'$lte': week_end}}]
        }},
        {'$project': {'items': {"$objectToArray": '$$ROOT'}}},
        {'$unwind': '$items'},
        {'$group': {'_id': '$items.k', 'sum': {'$sum': '$items.v'}}}
    ])

    records = {}
    for record in list(result):
        records[record['_id']] = record['sum']

    if '_id' in records:
        del records['_id']
    # else:
        # raise an exception: Records not found

    records['week_start'] = week_start.isoformat()[:10]
    records['week_end'] = week_end.isoformat()[:10]

    return records


def mongo_database():
    mongodb_user = os.getenv('MONGO_INITDB_ROOT_USERNAME')
    mongodb_pwd = os.getenv('MONGO_INITDB_ROOT_PASSWORD')
    client = MongoClient('mongodb://%s:%s@mongodb' % (mongodb_user, mongodb_pwd), connect=False)
    mongodb_db_name = os.getenv('MONGO_INITDB_DATABASE')

    return client[mongodb_db_name]


def test_mongo_database():
    database = mongo_database()

    assert database.name == 'parsed'
    assert isinstance(database.client, MongoClient)


if __name__ == '__main__':
    test_mongo_database()
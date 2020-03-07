import os
from pymongo import MongoClient, collection


def working_collections():
    mongodb_user = os.getenv('MONGO_INITDB_ROOT_USERNAME')
    mongodb_pwd = os.getenv('MONGO_INITDB_ROOT_PASSWORD')
    client = MongoClient('mongodb://%s:%s@mongodb' % (mongodb_user, mongodb_pwd))

    mongodb_db_name = os.getenv('MONGO_INITDB_DATABASE')
    db = client[mongodb_db_name]

    return db.parsed_file_hashes, db.parsed_records


def test_working_collections():
    parsed_file_hashes, parsed_records = working_collections()

    assert isinstance(parsed_file_hashes, collection.Collection)
    assert isinstance(parsed_records, collection.Collection)
    assert parsed_file_hashes.database.name == os.getenv('MONGO_INITDB_DATABASE')
    assert parsed_records.database.name == os.getenv('MONGO_INITDB_DATABASE')


if __name__ == '__main__':
    test_working_collections()

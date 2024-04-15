from pymongo import MongoClient


def init_database(user, password, db_name, host):
    connection_str = host.replace("<username>", user).replace("<password>", password).replace("<dbname>", db_name)
    client = MongoClient(connection_str)
    return client[db_name]
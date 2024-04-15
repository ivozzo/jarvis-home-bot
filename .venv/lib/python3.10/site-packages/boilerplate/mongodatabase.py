import boilerplate.mongo.initializer as initializer


class MongoDatabase:
    def __init__(self, host, user, password, database):
        self.host = host
        self.database = initializer.init_database(user=user, password=password, db_name=database, host=host)

    def get_collection(self, collection_name):
        return self.database[collection_name]

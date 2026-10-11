


class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("1. Allocating memory for Singleton Instance...")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, db_url = str):
        self.db_url = db_url
        print("2. Initializing instance state...")


db1 = DatabaseConnection("/db:1")
db2 = DatabaseConnection("/db:2")







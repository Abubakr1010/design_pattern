


class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


db1 = Database()
db2 = Database()

print(id(db1))
print(id(db2))

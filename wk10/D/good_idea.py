from abc import ABC, abstractmethod

# 1️⃣ สร้าง Abstraction
class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass


# 2️⃣ Low-level module implement abstraction
class MySQLDatabase(Database):
    def save(self, data):
        print(f"Saving {data} to MySQL")


class PostgreSQLDatabase(Database):
    def save(self, data):
        print(f"Saving {data} to PostgreSQL")


# 3️⃣ High-level module พึ่ง abstraction
class UserService:
    def __init__(self, db: Database):  # รับ dependency จากภายนอก
        self.db = db

    def register_user(self, name):
        self.db.save(name)


# 4️⃣ Inject dependency
mysql_db = MySQLDatabase()
service = UserService(mysql_db)

service.register_user("Alice")

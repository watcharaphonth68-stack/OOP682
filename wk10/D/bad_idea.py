class MySQLDatabase:
    def save(self, data):
        print(f"Saving {data} to MySQL")

class UserService:
    def __init__(self):
        self.db = MySQLDatabase()   # ❌ ผูกติดกับ MySQL ตรง ๆ

    def register_user(self, name):
        self.db.save(name)

service = UserService()
service.register_user("Alice")

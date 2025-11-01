


# CRUD 

# c - CREATE
# r - READ
# u - UPDATE
# D - DELETE

# import sqlite3
# 
# conn = sqlite3.connect("my_database.db")
# cursor = conn.cursor()
# 
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT,
#         age INTEGER       
#     )
# """)
# 
# # CREATE
# cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 21))
# conn.commit()
# 
# # READ
# cursor.execute("SELECT * FROM users")
# print(cursor.fetchall())
# 
# # UPDATE
# cursor.execute("UPDATE users SET age = ? WHERE name = ?", (22, "Bob"))
# conn.commit()
# 
# # DELETE 
# cursor.execute("DELETE FROM users WHERE name = ?", ("Bob", ))
# conn.commit()
# 
# conn.close()

import sqlite3

class DataBase:
    def __init__(self, db_name='databse.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER
                )
            """
        )

    def close(self):
        self.conn.close()

class User(DataBase):
    def __init__(self, name=None, age=None):
        super().__init__()
        self.name = name
        self.age = age

    def save(self):
        self.cursor.execute("INSERT INTO users (name, age) VALUES (?, ?) ",
            (self.name, self.age)
         )
        self.conn.commit()

    @classmethod 
    def all(cls):
        db = DataBase()
        db.cursor.execute("SELECT * FROM users")
        users = db.cursor.fetchall()
        db.close()
        return users

    @classmethod 
    def update_age(cls, name, new_age):
        db = DataBase()
        db.cursor.execute(
            "UPDATE users SET age = ? WHERE name = ?",
            (new_age, name)
        )
        db.conn.commit()
        db.close()

    @classmethod 
    def delete(cls, user_id):
        db = DataBase()
        db.cursor.execute(
            "DELETE FROM users WHERE id = ?",
            (user_id,)
        )
        db.conn.commit()
        db.close()


user1 = User("Sofia", 16)
user1.save()

user2 = User("Luiza", 21)
user2.save()

user3 = User("Islam", 16)
user3.save()

print(f"All Users {User.all()}")

User.update_age("Islam", 15)
print(f"All Users {User.all()}")

User.delete(1)
print(f"All Users {User.all()}")
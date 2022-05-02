from flask_login import UserMixin

from database import *

class User(UserMixin):
    def __init__(self, id_, first_name, last_name, email):
        self.id = id_
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    @staticmethod
    def get(user_id):
        db = database().get_db()
        user = db.execute(
            "SELECT * FROM customers WHERE id = ?", (user_id,)
        ).fetchone()
        if not user:
            return None

        user = User(
            id_=user[0], first_name=user[1], last_name=user[2], email=user[3], 
        )
        return user

    @staticmethod
    def create(id_, first_name, last_name, email):
        db = database().get_db()
        db.execute(
            "INSERT INTO customers (id, first_name, last_name, email) "
            "VALUES (?, ?, ?, ?)",
            (id_, first_name, last_name, email),
        )
        db.commit()



test1 = User(1, 'testFname', 'testLname', 'test@gmail.com')
#test1.create(2, "sam", "smith", "samsmith@gmail.com")
print(test1.get(2).first_name)
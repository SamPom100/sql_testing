import sqlite3
import os.path

class database:
    def create_database(self):
        conn = sqlite3.connect('customer.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE customers (
                id TEXT PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )""")
        conn.commit()

    def __init__(self):
        if not os.path.isfile('customer.db'):
            self.create_database()
        self.conn = sqlite3.connect('customer.db')

    def get_db(self):
        return sqlite3.connect('customer.db')

    def close_database(self):
        self.conn.close()

    def insertRow(self, first_name, last_name, email):
        c = self.conn.cursor()
        c.execute("INSERT INTO customers VALUES (?, ?, ?)", (first_name, last_name, email))
        self.conn.commit()

    def queryDatabase(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM customers")
        rows = c.fetchall()
        return rows

    def deleteRow(self, first_name, last_name, email):
        c = self.conn.cursor()
        c.execute("DELETE FROM customers WHERE first_name = ? AND last_name = ? AND email = ?", (first_name, last_name, email))
        self.conn.commit()

    def updateRow(self, first_name, last_name, email):
        c = self.conn.cursor()
        c.execute("UPDATE customers SET first_name = ?, last_name = ?, email = ? WHERE first_name = ? AND last_name = ? AND email = ?", (first_name, last_name, email, first_name, last_name, email))
        self.conn.commit()
    
    def deleteDatabase(self):
        c = self.conn.cursor()
        c.execute("DROP TABLE customers")
        self.conn.commit()



c = database()
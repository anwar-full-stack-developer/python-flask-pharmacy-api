# import sqlite3
# from sqlalchemy import text
# import app_init

# db=app_init.db
# app=app_init.app
# api = app_init.api

# # from db_connection import create_db_table, get_db_connection
# def load_data():
#     print(app.config["SQLALCHEMY_DATABASE_URI"])
#     conn = sqlite3.connect(app.config["SQLALCHEMY_DATABASE_URI"])
#     cur = conn.cursor()
#     cur.execute("INSERT INTO medicine_gener_types (name, details) VALUES (?, ?)", ('Allopathy', ''))


#     # db.execute("INSERT INTO medicine_gener_types (name, details) VALUES (?, ?)", ('Homeopathy', ''))
#     # db.execute("INSERT INTO medicine_gener_types (name, details) VALUES (?, ?)", ('Unani', ''))
    
#     db.commit()
#     # connection.close()

# if __name__ == '__main__':
#     # Create the database tables.
#     with app.app_context():
#         db.create_all()
#         # load_data()
#         con=db.engine.connect()
#         # con.execute(text("INSERT INTO medicine_gener_types (name, details) VALUES (:name, :details)"), {"name": "Allopathy", "details": ""})



# # connection = sqlite3.connect('database.db')
# # connection = get_db_connection()

# # create user table
# # create_db_table()

# # with open('schema.sql') as f:
# #     connection.executescript(f.read())

# # cur = connection.cursor()


# # def create_tables():
# #     tables = [
# #         """DROP TABLE IF EXISTS games;
# #         CREATE TABLE IF NOT EXISTS games(
# #                 id INTEGER PRIMARY KEY AUTOINCREMENT,
# #                 name TEXT NOT NULL,
# # 				price REAL NOT NULL,
# # 				rate INTEGER NOT NULL
# #             )
# #             """
# #     ]
# #     cursor = cur
# #     for table in tables:
# #         cursor.execute(table)
    
# # create_tables()


# # cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
# #             ('First Post', 'Content for the first post')
# #             )

# # cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
# #             ('Second Post', 'Content for the second post')
# #             )

# # cur.execute("INSERT INTO users (name, email, phone, address, country) VALUES (?, ?, ?, ?, ?)",
# #             ('admin', 'admin@admin.com', '42423424', "NY, USA", "USA")
# #             )
# # cur.execute("INSERT INTO users (name, email, phone, address, country) VALUES (?, ?, ?, ?, ?)",
# #             ('test', 'test@test.com', '42423424', "NY, USA", "USA")
# #             )

# # connection.commit()
# # connection.close()
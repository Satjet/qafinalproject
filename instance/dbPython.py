import sqlite3

connection = sqlite3.connect("chefrecipe.db")
print(connection.total_changes)


cursor = connection.cursor()

# cursor.execute("DROP TABLE Users")

# SQL Create Users Table
# cursor.execute("""CREATE TABLE Users (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 username TEXT,
#                 password  TEXT,
#                 email TEXT
#                 )""")

# Test inserting users into table
# cursor.execute("INSERT INTO Users (username, password, email) VALUES ('Ajay', 'password', 'test@test.com')")
# cursor.execute("INSERT INTO Users (username, password, email) VALUES ('Roman', 'Masala Chana', 2)")
# cursor.execute("INSERT INTO Users (username, password, email) VALUES ('Fred', 'Caesar Salad', 3)")
#
# target_Login_name = "Ajay"
# rows = cursor.execute(
#     "SELECT id,username, password, email FROM Users WHERE username = ?",
#     (target_Login_name,),
# ).fetchall()
# print(rows)

# Create Chef Database
# cursor.execute("""CREATE TABLE Chefs (
#                 chef_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT,
#                 link  TEXT
#                 )""")

# Populate Chef Database
cursor.execute("INSERT INTO Chefs (name, link) VALUES ('Sanjeev Kapoor',''")

# Create Recipe Database
# cursor.execute("""CREATE TABLE Recipes (
#                 recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 chef_id INTEGER,
#                 link  TEXT,
#                 FOREIGN KEY(chef_id) REFERENCES Chefs(chef_id)
#                 )""")

# Populate Recipe Database
cursor.execute("INSERT INTO Recipes (chef_id, link) VALUES ('1',''")
cursor.execute("INSERT INTO Recipes (chef_id, link) VALUES ('1',''")
cursor.execute("INSERT INTO Recipes (chef_id, link) VALUES ('1',''")

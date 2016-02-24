import sqlite3
db = sqlite3.connect(':memory:')
# Creates or opens a file called mydb with a SQLite3 DB
#db = sqlite3.connect('data/mydb')
cursor =db.cursor()
cursor.execute('''
    CREATE TABLE news_table(id INTEGER PRIMARY KEY, name TEXT,
                       URL TEXT unique)
''')
cursor = db.cursor()
name1= 'SPorts'
URL1 = 'http://aaztak.intoday.in/'
name1= 'Sp1'
URL1 = 'http://aaztak666.intoday.in/'
cursor.execute('''INSERT INTO news_table(name, URL)
                  VALUES(?,?)''', (name1,URL1))
print('FIRST USER INSERTED')
db.commit()
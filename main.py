import sqlite3
db=sqlite3.connect('students.db')
c=db.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS student(
id INTEGER PRIMARY KEY,
hobby TEXT,
name TEXT,
last_name TEXT,
born INT,
hw_score INT
) ''')


# c.execute(''' INSERT INTO student (hobby, name, last_name, born, hw_score) VALUES
# ('футбол', 'Иван', 'Иванов', 1999, 10),
# ('баскетбол', 'Петр', 'Петров', 2000, 9),
# ('волейбол', 'Сергей', 'Сергеев', 1998, 90),
# ('бокс', 'Александр', 'Александров', 2002, 1),
# ('теннис', 'Михаил', 'Михайлов', 2001, 88),
# ('плавание', 'Дмитрий', 'Дмитриев', 1997, 5),
# ('гимнастика', 'Елена', 'Еленова', 1996, 85),
# ('легкая атлетика', 'Анна', 'Аннова', 1995, 78),
# ('бокс', 'Виктор', 'Викторов', 2003, 2),
# ('плавание', 'Ольга', 'Ольгова', 2004, 95)
# ''')

# c.execute('''SELECT * FROM student WHERE LENGTH(last_name) > 10''')

# c.execute(''' UPDATE student SET name = 'genius' WHERE hw_score > 10 ''')

# c.execute('''SELECT * FROM student where name = 'genius' ''')

# c.execute('''DELETE FROM student WHERE id % 2 = 0''')


# c.execute('''SELECT * FROM student''')


for i in c.fetchall():
    print(i)

db.commit()
db.close()
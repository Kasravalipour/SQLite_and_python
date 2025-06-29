import sqlite3

# connect to the database 
conn = sqlite3.connect('customer.db')

# create a cursor
curs = conn.cursor()

# CREATE TABLE (اصلاح: تغییر executemany به execute و اصلاح نام جدول)
curs.execute("""CREATE TABLE IF NOT EXISTS customer (
    first_name TEXT,
    last_name TEXT,
    age INTEGER
)""")

# and now we are gonna put data in our created table
#sqlcommands = curs.execute("INSERT INTO custumer VALUES ('Kasra', 'Valipour', 16)")

# record plus one thing in a table 
many_custumers = [('zahra', 'zahedi', 18),
                  ('parisa', 'honari', 17),
                  ('parsa', 'ghorbani', 25),
                  ('arvin', 'shahi', 16)
    ]

#sqlcommands_many = curs.executemany("INSERT INTO customer VALUES (?, ?, ?)", many_custumers)

# and now we are gonna query and fetchell in our database
fech_q = curs.execute("SELECT * FROM customer")
items = curs.fetchall()
print(items)



# bebinim ke dorost amale sql anjam shode ya na --> def try
try:
    # inja moteqayere har execute ro bayad bezaram
    fech_q
    conn.commit()
    print("Command executed successfully ✔")
except Exception as e:
    print("An error occurred:", e)

# close our connection
conn.close()

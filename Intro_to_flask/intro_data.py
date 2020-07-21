import sqlite3

conn = sqlite3.connect('intro_data.sqlite3')
curs = conn.cursor()
drop_if_exists = '''
DROP TABLE IF EXISTS name
'''
# Drop Previous Table
curs.execute(drop_if_exists)
# Create Table
create_statement = '''
CREATE TABLE name (ID INTEGER PRIMARY KEY AUTOINCREMENT, name text, location text);
'''
curs.execute(create_statement)
# Adding to table
insert_statement = '''
INSERT INTO name (name, location)
VALUES ("Noah", "Philly"),("SasDaddy", "Atlanta")
'''
curs.execute(insert_statement)
# Check Table
select_statement = """
SELECT ID, name, location from name;
"""

curs.execute(select_statement)
curs.fetchall()
conn.commit()
curs.close()
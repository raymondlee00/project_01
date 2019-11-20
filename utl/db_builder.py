import sqlite3

DB_FILE="../discobandit.db" # build the db structure (tables and stuff) in the discobandit.db on the topmost level, not in the utl folder

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================


#Initialize the accounts table
create_accounts_table = """ CREATE TABLE IF NOT EXISTS accounts (
                            username TEXT, password TEXT
                            );"""

c.execute(create_accounts_table)

def addAccount(user, password):
    insert_account = str.format("INSERT INTO accounts VALUES ('{}', '{}');", user, password)
    c.execute(insert_account)

#==========================================================

db.commit() #save changes
db.close()  #close database
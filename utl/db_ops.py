import sqlite3

DB_FILE = "discobandit.db"

def accountExists(user):
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops

    #==========================================================

    c.execute(
    """
        SELECT * FROM accounts WHERE username = (?)
    """, (user,)
    )

    rowCount = 0
    for row in c:
        rowCount += 1

    #==========================================================

    db.close()  #close database

    if (rowCount == 1):
        return True

    return False

# function to takes in a username and password and creates a new user entry
def addAccount(user, pw):
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops

    #==========================================================

    c.execute("INSERT INTO accounts VALUES (?, ?)", (user, pw))

    #==========================================================

    db.commit() #save changes
    db.close()  #close database

# function that authenticates the username and password arguments to verify that the account exists
def authenticate(user, pw):
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops

    #==========================================================

    c.execute(
    """
        SELECT * FROM accounts WHERE username = (?)
    """, (user,)
    )

    rowCount = 0
    for row in c:
        db.close() #only one iteration should happen anyway so I can close it right now
        rowCount += 1
        if (rowCount != 1):
            return False

        return pw == row[1]


#for each method, I have added an example code that is commented out at the end
#please use them as reference since in some methods you have to give inputs in a specific way
##add cols to your selected table
def addcols(col_name,col_type,tb_name):#see example code below
    db_name="discobandit.db"
    c=sqlite3.connect(db_name)
    db=c.cursor()
    command="ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"
    c.execute(command.format(tn=tb_name,cn=col_name,ct=col_type))
    c.commit()
    c.close()
#addcols("testing","TEXT","TABLE1")
def CreateTable(table_name,col_string): ## see example code below
    db_name="discobandit.db"
    c=sqlite3.connect(db_name)
    db=c.cursor()
    command="CREATE TABLE if not exists {tb} ({cols})"
    c.execute(command.format(tb=table_name,cols=col_string))
    c.commit()
    c.close()
#CreateTable("Students","ID INTEGER, GPA REAL")

#this is a helper function, please don't use this as it can cause unexpected behaviours
#I am keeping it because I have used it within a function where I know its behaviour
def data_builder():
    db_name="discobandit.db"
    c=sqlite3.connect(db_name)
    db=c.cursor()
    return c
def addRows(table_name,columns,values): #everything is inputed as strings,
                                       #for addRows you have to use '' for TEXT values
                                       ## see example code below
    c=data_builder()
    command='''
    INSERT INTO {tn} ({cols})
     VALUES ({vals} )'''
    c.execute(command.format(tn=table_name,cols=columns,vals=values))
    c.commit()
    c.close()
#addRows("TABLE2","ID,NAME","123,'tanzim'") here, the col NAME accepts TEXT
#values.Hence, I used '' to surround tanzim. If you don't do this, the code will be broken.

#this function lets you modify col values in specified rows
def update(table_name,cols,conditional):# the condition is where you specify your addRows
    c=data_builder()                    # see example code to see how to use it
    command='''
    UPDATE {tn}
    SET {col}
    WHERE
    {cond}'''
    c.execute(command.format(tn=table_name,col=cols,cond=conditional))
    c.commit()
    c.close()
#update("TABLE2","ID=5,NAME='Goku'", "NAME='Go'")

def retrieve_data(table_name,cols_needed,conditional):## returns a list of tuples of the desired data
    db_name="discobandit.db"                             ##from the database
    c=sqlite3.connect(db_name)                         ## If you want all data from a table
    db=c.cursor()                                      ## enter 1 = 1 as conditional
    command='''
    Select {col}
    FROM {tn}
    WHERE {cond}
    '''
    db.execute(command.format(tn=table_name,col=cols_needed,cond=conditional))
    answer=db.fetchall()
    c.commit()
    c.close()
    return answer
# print(retrieve_data("TABLE2","NAME","ID=5"))
def multi_retrieve_data(table1_name,table2_name,cols,conditional): #links data between multiple_tables
    db_name="discobandit.db"                                        #returns a list of tuples
    c=sqlite3.connect(db_name)
    db=c.cursor()
    command='''
    Select {col}
    FROM {tn1}
    INNER JOIN {tn2}
    ON {cond}'''
    db.execute(command.format(col=cols,tn1=table1_name,tn2=table2_name,cond=conditional))
    answer=db.fetchall()
    c.commit()
    c.close()
    return answer
#print(multi_retrieve_data("TABLE2","Students","NAME,GPA","Students.ID=TABLE2.ID"))
def deleterow(table,condition): #deletes the rows specifieid with the condition
    db_name="discobandit.db"
    c=sqlite3.connect(db_name)
    db=c.cursor()
    command='''
    DELETE FROM {tn}
    WHERE {cond}
    '''
    db.execute(command.format(tn=table,cond=condition))
    c.commit()
    c.close()
#deleterow("TABLE2","ID=23")
CreateTable("loc_data",'''
longitude REAL,city TEXT, timezone TEXT, accuracy INTEGER, asn INTEGER,region TEXT,
organization_name TEXT, organization TEXT, contry_code TEXT, ip TEXT,
latitude REAL,area_code INTEGER, continent_code TEXT, country TEXT,
country_code3 TEXT ''')
CreateTable("planes","data TEXT")

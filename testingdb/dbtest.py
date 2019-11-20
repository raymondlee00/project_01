import sqlite3
db_name="data.sqlite"
c=sqlite3.connect(db_name)
db=c.cursor()
command="CREATE TABLE if not exists TABLE1 (col1 TEXT, col2 TEXT, col3 TEXT)"
c.execute(command)
c.commit()
c.close()
##add cols to your selected table
def addcols(col_name,tb_name):
    db_name="data.sqlite"
    c=sqlite3.connect(db_name)
    db=c.cursor()
    command="ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"
    c.execute(command.format(tn=tb_name,cn=col_name,ct="INTEGER"))
    c.commit()
    c.close()
def CreateTable(table_name,col_string): ## insert the cols you want to make
    db_name="data.sqlite"
    c=sqlite3.connect(db_name)
    db=c.cursor()
    command="CREATE TABLE if not exists {tb} ({cols})"
    c.execute(command.format(tb=table_name,cols=col_string))
    c.commit()
    c.close()
def addRows(table_name,columns,values): #for addRows you have to use parenthesis before vlaues
    db_name="data.sqlite"               ## see example code below
    c=sqlite3.connect(db_name)
    db=c.cursor()
    command='''
    INSERT INTO {tn}({cols}) VALUES{vals}'''
    c.execute(command.format(tn=table_name,cols=columns,vals=values))
    c.commit()
    c.close()
## addRows('TABLE1',"col1,col2",("come","hey"))
##for now update isnot working, I'll fix it tomorrow
def updateTable(cols,values,table_name,conditional): #cols,conditional and values gotta be lists
    db_name="data.sqlite"               ## see example code below
    c=sqlite3.connect(db_name)
    db=c.cursor()
    setCommand=""
    tracker=0
    for col in cols:
        setCommand=setCommand+col+ "=" + values[tracker]+ " "
        tracker=tracker+1
    whereCommand=""
    tracker=0
     UPDATE table2
     SET ID = 10,
     Name= 'Go'
     Where Name= 'hey'
     '''
    c.execute(command)
    c.commit()
    c.close()
updateTable(["ID","NAME"],[2,"Chimchar"],"TABLE2",[("ID",23),("Name","Pika")])
addRows("TABLE2","ID,NAME",(23,"Pika"))

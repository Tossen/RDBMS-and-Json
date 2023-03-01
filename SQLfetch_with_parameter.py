import pyodbc 
import pandas as pd
import ast
file = open("login.txt", "r")
contents = file.read()
d = ast.literal_eval(contents)

file.close()

print(type(d))


username = d["Username"]
password = d["Password"]
# print(username)
# print(password)
    

try:
    # user1 = myLogin(username)
    # pass =  myLogin(password)

    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                            "Server=TMACS-ENGINE\sa;"
                            "Database=CrownA+;"
                            "uid=" + username +";pwd=" + password)
    tableName = input('Enter Search TableInstance :')
    inputParam = input('Enter Search Param : ')
    sql = 'select * from ' + (tableName) + ' where CustomerID = ?'
    df = pd.read_sql_query(sql,cnxn,params = [inputParam])
    # CBLoans
    #sql="Select Top 5 * from mytable where id between ? and ?"
    #df = pd.read_sql(sql,cnxn,params =[52,65])
    print(df)
    df.to_csv('C:/Users/Tossen Macs/Documents/QueryOutputFile/Detail.csv')
    
except Exception as e:
    print(str(e))






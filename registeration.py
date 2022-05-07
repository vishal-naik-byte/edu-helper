import mysql.connector

def check_login(Email=None,password=None):
    try:
        mydb=mysql.connector.connect(host="localhost",database="students",user="root",password="root")
        mycursor=mydb.cursor()
        #mycursor.execute('delete from attendence where RollNo=1;')
        mycursor.execute("select * from register where Email='{}' and password='{}';".format(Email,password))
        result=mycursor.fetchall()
        print(result)
    except mysql.connector.Error as e:
        print(e)
    finally:
        mydb.commit()
        if mydb.is_connected():
            mydb.close()
    return result


def postData(name=None,email=None,password=None):
    query=False
    if name == None or email == None or password == None:
        return None
    try:
        mydb=mysql.connector.connect(host="localhost",database="students",user="root",password="root")
        mycursor=mydb.cursor()
        #mycursor.execute('delete from attendence where RollNo=1;')
        mycursor.execute("INSERT INTO register (Name,Email,password) VALUES ('{}','{}','{}');".format(name,email,password))
        result=mycursor.fetchall()
        query=True
    except mysql.connector.Error as e:
        print(e)
    finally:
        mydb.commit()
        if mydb.is_connected():
            mydb.close()
    return query
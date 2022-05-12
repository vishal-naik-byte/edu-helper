import mysql.connector

def get_Attendence(RollNo=None):

    if RollNo == None:
        return "Something Went Wrong or You did not typed your RollNo Correctly"

    try:
        mydb=mysql.connector.connect(host="localhost",database="students",user="root",password="root")
        mycursor=mydb.cursor()
        #mycursor.execute('delete from attendence where RollNo=1;')
        mycursor.execute("select * from attendence where RollNo={};".format(RollNo))
        result=mycursor.fetchall()
        string="Hello %s, Your Attendence Percentage is %d" % (result[0][1],result[0][5])
    except mysql.connector.Error as e:
        print(e)
    finally:
        mydb.commit()
        if mydb.is_connected():
            mydb.close()
    return string+"%"

def get_Result(RollNo=None):
    
    if RollNo == None:
        return "Something Went Wrong or You did not typed your RollNo Correctly"

    try:
        mydb=mysql.connector.connect(host="localhost",database="students",user="root",password="root")
        mycursor=mydb.cursor()
        mycursor.execute("select * from result where RollNo={};".format(RollNo))
        result=mycursor.fetchall()
        string="Hello %s, Your Result is: mmt:%d,Dsc:%d,Cs:%d,Ecom:%d,Total:%d,TotalPercentage:%d" % (result[0][1],result[0][2],result[0][3],result[0][4],result[0][5],result[0][6],result[0][7])
    except mysql.connector.Error as e:
        print(e)
    finally:
        mydb.commit()
        if mydb.is_connected():
            mydb.close()
    return string+"%"
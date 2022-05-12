from getData import *
#file1=open("complaint.txt","a")

#file1.write("canteen is not good\n")
#file1.close()
a="result:rollno:678"
split=a.split(':')

if split[0] == "result":
    RollNo=split[2]
    print(RollNo)
    result=get_Result(RollNo)
    #print(result)

import mysql.connector

user1 = input("Please enter user: ")
pass1 = input("Please enter your password: ")
host1 = input("Please enter host: ")
databasename = input("Please enter name of the database: ")
mydb =mysql.connector.connect(user=user1, password=pass1,
                              host=host1,database =databasename)

mycursor = mydb.cursor()

dept_id = input("ENTER DEPARTMENT_ID : ")
course_id = input("ENTER COURSE_ID : ")
teacher_id = input("ENTER TEACHER_ID : ")
class_room = input("ENTER CLASSROOM NAME : ")
mycursor.execute("insert into course (courseId,deptNo) values (%s,%s)",(course_id,dept_id))
mycursor.execute("insert into professor (empId,deptNo) values (%s,%s)",(teacher_id,dept_id))
mycursor.execute("insert into teaching (empId,courseId,sem,year,classRoom) values (%s,%s,%s,%s,%s)",(teacher_id,course_id,"even",2006,class_room))
mydb.commit()

roll = input("ENTER YOUR ROLL NUMBER: ")

query1 = "select deptNo from student where rollNo={}".format(str(roll))
mycursor.execute(query1)
deptOfRoll = mycursor.fetchone()
if deptOfRoll is None:
    print("Please enter a valid Roll Number")

elif deptOfRoll[0]==dept_id:
    while(True):
        course = input("ENTER NAME OF THE COURSE THAT YOU WANT TO ENROLL IN: ")
        if(course=='exit'):
            break
        query2 = "select preReqCourse from preRequisite where courseId={}".format(course)
        mycursor.execute(query2)
        temp = mycursor.fetchall()
        preReqCourses = []
        for x in temp:
            preReqCourses.append(x[0])
        print(preReqCourses)
        vis = [0]*len(preReqCourses)
        query3 = "select courseId,grade from enrollment where rollNo={}".format(roll)
        mycursor.execute(query3)
        temp2 = mycursor.fetchall()
        coursesDoneByYou = []
        for x in temp2:
            #print(x)
            coursesDoneByYou.append(list(x))
        print(coursesDoneByYou)
        chk=0
        for j in range(len(coursesDoneByYou)):
            if(course==coursesDoneByYou[j][0] and (coursesDoneByYou[j][1]=='S' or coursesDoneByYou[j][1]=='A' or coursesDoneByYou[j][1]=='B' or coursesDoneByYou[j][1]=='D' or coursesDoneByYou[j][1]=='C' or coursesDoneByYou[j][1]=='E' )):
                print("Because you have already completed this course, we are unable to register you for it again.")
                chk=1
        if(chk==1):
            continue
        for i in range(len(preReqCourses)):
            for j in range(len(coursesDoneByYou)):
                if(preReqCourses[i]==coursesDoneByYou[j][0] and (coursesDoneByYou[j][1]=='S' or coursesDoneByYou[j][1]=='A' or coursesDoneByYou[j][1]=='B' or coursesDoneByYou[j][1]=='D' or coursesDoneByYou[j][1]=='C' or coursesDoneByYou[j][1]=='E')):
                    vis[i]=1
                elif(preReqCourses[i]==coursesDoneByYou[j][0] and (coursesDoneByYou[j][1]=='U' or coursesDoneByYou[j][1]=='W') ):
                    print("You have not completed a course {} which is pre requisite of {}. So you cannot register to this course".format(preReqCourses[i],course))
                    chk=1
                    break
            if(chk==1):
                break
        if(chk==1):
            continue
        for i in range(len(vis)):
            if(vis[i]==0):
                print("You do not have all of the prerequisites for this course, so please complete those before enrolling in this course.")
                chk=1
                break
        if(chk==1):
            continue
        mycursor.execute("insert into enrollment (rollNo,courseId,sem,year) values (%s,%s,%s,%s)",(roll,course,'even',2006))
        mydb.commit()
        print("You are successfully enrolled for the course {}".format(course))
else:
    print("You dont belong to this department sorry!!")

mydb.close()
import pymysql
db = pymysql.connect('localhost', 'root', 'password', 'login')
cursor = db.cursor()

def sign_up():
    userid = input('Enter UserID : ')
    query = "select * from login;"
    try:
        cursor.execute(query)
        fetch = cursor.fetchall()
        n = len(fetch)
        flag = 0
        for i in range(n):
            if userid == fetch[i][0]:
                print('User already exist!, redirecting to login page')
                flag = 1
                login()
        if flag == 0:
            pswd = input('Enter password : ')
            re_pswd = input('Enter password again : ')
            if pswd == re_pswd:
                query = "insert into login values('" + userid + "', '" + pswd + "');"
                try:
                    cursor.execute(query)
                    print('Sign up successful')
                except:
                    db.rollback()
                    print('Sign up fail')
            else:
                print("Password didn't match")
    except:
        db.rollback()

def login():
    userid = input('Enter UserID : ')
    query = "select * from login;"
    try:
        cursor.execute(query)
        fetch = cursor.fetchall()
        n = len(fetch)
        flag = 0
        for i in range(n):
            if userid == fetch[i][0]:
                pswd = input('Enter password : ')
                if pswd == fetch[i][1]:
                    print('Login successfully :)')
                    flag = 1
                else:
                    print("UserID and password doesn't match")
                    flag = 1
        if flag == 0:
            print('NO such user exist!, redirecting to Sign Up page')
            sign_up()
    except:
        db.rollback()

def show():
    query = "select * from login;"
    try:
        cursor.execute(query)
        fetch = cursor.fetchall()
        n = len(fetch)
        for i in range(n):
            print(fetch[i][0], fetch[i][1])
    except:
        db.rollback()
        print('Bad')

def change_pswd():
    userid = input('Enter UserId : ')
    query = 'select * from login;'
    try:
        cursor.execute(query)
        fetch = cursor.fetchall()
        n = len(fetch)
        flag = 0
        for i in range(n):
            if userid == fetch[i][0]:
                pswd = input('Enter old password : ')
                if pswd == fetch[i][1]:
                    new_pswd = input('Enter new password : ')
                    query = "update login set password = \'" + new_pswd + "\' where userid = \'" + userid + "\'"
                    try:
                        cursor.execute(query)
                        db.commit()
                        print('Password changed successfully')
                        flag = 1
                    except:
                        db.rollback()
                else:
                    print('Wrong password')
                    flag = 1
        if flag == 0:
            print('No such user exist!')
    except:
        db.rollback()
        print('Bad')

print('1.Sign UP', '2.Login', '3.Show All User', '4.Change Password', sep="\n")
opt = int(input())
if opt == 1:
    sign_up()
elif opt == 2:
    login()
elif opt == 3:
    show()
elif opt == 4:
    change_pswd()

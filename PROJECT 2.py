print('-----------------------------------------------------')
print("\t     WELCOME TO BANKING SOFTWARE")
print('-----------------------------------------------------')
def menu():
    ans='y'
    while(ans=='y' or ans=='Y'):
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print("\t1. ADD ACCOUNT")
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print("\t2. UPDATE AN ACCOUNT")
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print("\t3. DEPOSIT AMOUNT")
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print("\t4. WITHDRAW AMOUNT")
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print("\t5. DELETE AN ACCOUNT")
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print("\t6. SEARCH AN ACCOUNT")
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print("\t7. DISPLAY ALL ACCOUNTS")
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print("\t8. EXIT")
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        choice=int(input("\tEnter your choice:"))
        if choice==1:
            add()
        elif choice==2:
            update()
        elif choice==3:
            deposit()
        elif choice==4:
            withdraw()
        elif choice==5:
            delete()
        elif choice==6:
            search()
        elif choice==7:
            display()
        elif choice==8:
            print('***************Exiting*******************')
            break
        else:
            print('\t...wrong choice!!!')
        ans=input('Do You Want To Continue (y,n):')
        
def add():
    try:
        print('\t          .......Details Of The Customer.......   ')
        print("\t***** All information prompted are mandatory to be filled********")
        acno=int(input("Enter Account Number:"))
        name=input('Enter Name :')
        address=input("Enter Address :")
        phno=input("Enter Phone Number :")
        email=input("Enter Email ID:")
        dep=int(input("Enter Deposited Amount:"))
        withd=0
        bal=dep
        cursor=bnk.cursor()
        query="insert into bank values({},'{}','{}','{}','{}',{},{},{})".format(acno,name,address,phno,email,dep,withd,bal)
        cursor.execute(query)
        bnk.commit()
        print("\t *****Account has been successfully created!!!*****\n")
    except:
        print("...............Sorry!!!Invalid Data...................")
def update():
    try:
        acno=int(input('Enter Account number:'))
        print('.............Enter New Account Details..............')
        name=input('Account Beneficiary:')
        address=input('Enter New Address:')
        phno=input('Enter Updated Phone Number:')
        email=input('Enter Valid Email ID:')
        cursor=bnk.cursor()
        cursor.execute("update bank set Cust_Name='{}',Address='{}',Phone_No='{}',Email='{}' where Acc_No={}".format(name,address,phno,email,acno))
        bnk.commit()
        print('\t****Account Has Been Updated*****\n')
    except:
        print("..................Invalid Entry...................\n")    

def deposit():
    try:
        acno=int(input('Enter Account number:'))
        dep=int(input('Enter Amount To Be Deposited:'))
        cursor=bnk.cursor()
        cursor.execute("update bank set Dep_Amt=Dep_Amt+{} where Acc_No={}".format(dep,acno))
        cursor.execute('update bank set Balance=Balance+{} where Acc_No={}'.format(dep,acno))
        bnk.commit()
        print("*******Successfully Deposited******\n")
    except:
        print("............Error..........\n")
def withdraw():       
    try:
        acno=int(input('Enter Account number:'))
        withd=int(input('Enter Amount To Be Withdrawn:'))
        cursor=bnk.cursor()
        cursor.execute("update bank set With_Amt=With_Amt+{} where Acc_No={}".format(withd,acno))
        cursor.execute('update bank set Balance=Balance-{} where Acc_No={}'.format(withd,acno))
        bnk.commit()
        print("*******Successfully Withdrawn******\n")
    except:
        print("...............Error................\n")
def search():
    try:
        acno=int(input('Enter Account Number:'))
        cursor=bnk.cursor()
        cursor.execute('select * from bank where Acc_No={}'.format(acno))
        record=cursor.fetchone()
        print('....................ACCOUNT DETAILS......................')
        print('Account Beneficiary:',record[1])
        print('Address:',record[2])
        print('Phone Number:',record[3])
        print('Email ID :',record[4])
        print('Deposited amount :',record[5])
        print('Withdrawed amount :',record[6])
        print('Balance amount :',record[7])
    except:
        print("Error!!!...\n")
 
def display():
    try:
        cursor=bnk.cursor()
        cursor.execute("select * from bank")
        res=cursor.fetchall()
        print('\t............ALL THE ACCOUNT DETAILS............')
        for i in res:
            print('********************************************************************************************************\n')
            print("\tAccount Number:",i[0])
            print("\tAccount Beneficiary:",i[1])
            print("\tAddress:",i[2])
            print("\tPhone Number:",i[3])
            print("\tEmail id:",i[4])
            print("\tDeposited Amount:",i[5])
            print("\tWithdrawed Amount:",i[6])
            print("\tBalance Amount:",i[7],"\n")
            
    except:
        print("...............ERROR!!!...................\n")
def delete():
    acno=int(input('Enter Account Number:'))
    cursor=bnk.cursor()
    cursor.execute('delete from bank where Acc_No={}'.format(acno))
    print('\t****Account Has Been Deleted*****\n')
    bnk.commit()
import mysql.connector as c
bnk=c.connect(host='localhost',user='root',passwd='D!nken2459',database='banking')
pwd=input('Enter Password:')
cursor=bnk.cursor()
cursor.execute("SELECT pwd FROM password")
pwd1=cursor.fetchone()
if pwd in pwd1:
    menu()
else:
    print('\tWrong Password!! Try Again...')

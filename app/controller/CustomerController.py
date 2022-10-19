import mysql.connector as connection

class Customer:  
    def myConnecion():
        db = connection.connect(
            host='127.0.0.1',
            user='root',
            password='Rajith1234@',
            database='python_pos'
        )

        #print(db)

        return db

    def printMenu():
        print('======================================================================')
        #print('||                                                                  ||')
        print('||    1.Register Customer                     2.Update Customer     ||')
        print('||    3.Search Customer                       4.Delete Customer     ||')
        #print('||                                                                  ||')
        print('======================================================================')

        option = input('Enter Option Number To Continue :')

        return option

    def saveCustomer(myDatabase):
        mycursor = myDatabase.cursor()

        print('======================================')
        name = input('Enter Customer Name :')
        address = input('Enter Customer Adddress :')
        salary = input('Enter Customer Salary :')

        #print(name,address,salary)

        qury = 'insert into customer(name,address,salary) value (%s,%s,%s)'
        value = (name,address,salary)
        mycursor.execute(qury,value)
        myDatabase.commit()
    
    def updateCustomer(myDatabase):
        myCursor = myDatabase.cursor()

        print('======================================')
        name = input('Enter Customer Name Want to Update :')
        address = input('Enter  Cutomer new Address :')
        salary = input('Enter Customer new Salary :')

        #print(name,address,salary)

        qury = 'update Customer set address = %s , salary = %s where name = %s'
        value = (address,salary,name)
        myCursor.execute(qury,value)
        myDatabase.commit()

    def deleteCustomer(myDatabase):
        myCursor = myDatabase.cursor()

        print('======================================')
        name = input('Enter name of the Customer want to Delete :')

        query = 'delete from Customer where name = %s'
        value = [name]
        myCursor.execute(query,value)
        myDatabase.commit()

    def searchCustomer(myDatabase):
        myCusrsor = myDatabase.cursor()

        print('======================================')
        name = input('Enter Name of the Customer want to search :')

        query = 'select * from customer where name = %s'
        value = [name]
        myCusrsor.execute(query,value)
        myresult = myCusrsor.fetchall()
        
        for result in myresult:
            print(result)



    #print("Number :",printMenu())

    option = printMenu()

    if(option == '1'):
        saveCustomer(myConnecion())
    elif(option == '2'):
        updateCustomer(myConnecion())
    elif(option == '3'):
        searchCustomer(myConnecion())
    elif(option == '4'):
        deleteCustomer(myConnecion())
    else:
        print('Entered Wrong Number !')
        printMenu()
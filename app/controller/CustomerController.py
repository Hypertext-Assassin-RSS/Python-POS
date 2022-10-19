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

    




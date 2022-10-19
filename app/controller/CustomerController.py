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

    saveCustomer(myConnecion())




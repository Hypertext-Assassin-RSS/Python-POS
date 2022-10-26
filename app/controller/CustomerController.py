from distutils.command.install_egg_info import safe_name
import mysql.connector as connection
import tkinter as tk


class Connection:
    def makeConnection(self):
            db = connection.connect(
                        host='127.0.0.1',
                        user='root',
                        password='Rajith1234@',
                        database='python_pos'
                    )

            mycursor = db.cursor()
            qury = 'create table if not exists customer(name varchar(50),address varchar(50),salary varchar(50))'
            mycursor.execute(qury)

            return db

# class PrintMenue:
#     print('======================================================================')
#     # print('||                                                                  ||')
#     print('||    1.Register Customer                     2.Update Customer     ||')
#     print('||    3.Search Customer                       4.Delete Customer     ||')
#     # print('||                                                                  ||')
#     print('======================================================================')

#     option = input('Enter Option Number To Continue :')

            # print(db)
class Customer:
    def saveCustomer(self,myDatabase,name,address,salary):
        mycursor = myDatabase.cursor()

        # print('======================================')
        # name = input('Enter Customer Name :')
        # address = input('Enter Customer Adddress :')
        # salary = input('Enter Customer Salary :')

        # print(name,address,salary)

        qury = 'insert into customer(name,address,salary) value (%s,%s,%s)'
        value = (name,address,salary)
        mycursor.execute(qury,value)
        myDatabase.commit()

        print(mycursor.rowcount, "record inserted.")

        print('ok')

    def updateCustomer(self,myDatabase,name,address,salary):
        mycursor = myDatabase.cursor()

        # print('======================================')
        # name = input('Enter Customer Name Want to Update :')
        # address = input('Enter  Cutomer new Address :')
        # salary = input('Enter Customer new Salary :')

        # print(name,address,salary)

        qury = 'update Customer set address = %s , salary = %s where name = %s'
        value = (address,salary,name)
        mycursor.execute(qury,value)
        myDatabase.commit()

        print(mycursor.rowcount, "record(s) affected")

    def deleteCustomer(self,myDatabase,name):
        mycursor = myDatabase.cursor()

        # print('======================================')
        # name = input('Enter name of the Customer want to Delete :')

        query = 'delete from Customer where name = %s'
        value = [name]
        mycursor.execute(query,value)
        myDatabase.commit()

        print(mycursor.rowcount, "record(s) deleted")

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



    # print("Number :",printMenu())

    # option = printMenu()

    # if(option == '1'):
    #     saveCustomer(myConnecion())
    # elif(option == '2'):
    #     updateCustomer(myConnecion())
    # elif(option == '3'):
    #     searchCustomer(myConnecion())
    # elif(option == '4'):
    #     deleteCustomer(myConnecion())
    # else:
    #     print('Entered Wrong Number !')
    #     printMenu()
class widndow:
    

    def main():
            window = tk.Tk()
        
            nameLabel = tk.Label(text='name')
            nameLabel.pack()
            nameEntry = tk.Entry( width=50)
            nameEntry.pack()

            addressLabel = tk.Label(text='address')
            addressLabel.pack()
            addressEntry = tk.Entry( width=50)
            addressEntry.pack()

            salaryLabel = tk.Label(text='salary')
            salaryLabel.pack()
            salaryEntry = tk.Entry( width=50)
            salaryEntry.pack()

            def save():
                name = nameEntry.get()
                address =  addressEntry.get()
                salary = salaryEntry.get()
                print(name,address,salary)

                myDatabase = Connection().makeConnection()
                print(myDatabase)
                customer = Customer()
                customer.saveCustomer(myDatabase,name,address,salary)

            def update():
                name = nameEntry.get()
                address =  addressEntry.get()
                salary = salaryEntry.get()
                print(name,address,salary)
                
                myDatabase = Connection().makeConnection()
                print(myDatabase)
                customer = Customer()
                customer.updateCustomer(myDatabase,name,address,salary)
            
            def delete():
                name = nameEntry.get()
                print(name)
                
                myDatabase = Connection().makeConnection()
                print(myDatabase)
                customer = Customer()
                customer.deleteCustomer(myDatabase,name)
            

            buttonSave = tk.Button(text="Save",width=10,height=2,bg="blue",fg="yellow", command=save)
            buttonSave.pack()

            buttonUpdate = tk.Button(text="Update",width=10,height=2,bg="orange",fg="yellow", command=update)
            buttonUpdate.pack()

            buttonDelete = tk.Button(text="Delete",width=10,height=2,bg="red",fg="yellow", command=delete)
            buttonDelete.pack()

            window.mainloop()

    main()

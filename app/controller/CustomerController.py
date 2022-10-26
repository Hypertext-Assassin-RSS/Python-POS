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

    def searchCustomer(self,myDatabase,name):
        myCusrsor = myDatabase.cursor()

        # print('======================================')
        # name = input('Enter Name of the Customer want to search :')

        query = 'select * from customer where name = %s'
        value = [name]
        myCusrsor.execute(query,value)
        myresult = myCusrsor.fetchall()

        for result in myresult:
            return result



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
            window.title("Python POS")
            window.geometry("400x200")

            nameLabel = tk.Label(text='Name    ')
            addressLabel = tk.Label(text='Address  ')
            salaryLabel = tk.Label(text='Salary      ')

            nameLabel.grid(row=0, column=0, pady=2)
            addressLabel.grid(row=1, column=0, pady=2)
            salaryLabel.grid(row=2, column=0, pady=2)

            nameEntry = tk.Entry(width=50)
            addressEntry = tk.Entry(width=50)
            salaryEntry = tk.Entry(width=50)

            nameEntry.grid(row=0, column=1, pady=2)
            addressEntry.grid(row=1, column=1, pady=2)
            salaryEntry.grid(row=2, column=1, pady=2)

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
            
            def search():
                name = nameEntry.get()
                print(name)

                myDatabase = Connection().makeConnection()
                print(myDatabase)
                customer = Customer().searchCustomer(myDatabase,name)
                #print(customer)
                
                address = customer[1]
                salary = customer[2]

                addressEntry.delete(0,tk.END)
                addressEntry.insert(0,customer[1])

                salaryEntry.delete(0,tk.END)
                salaryEntry.insert(0,customer[2])


            buttonSave = tk.Button(text="Save", width=20, height=2, bg="blue", fg="yellow", activebackground='white' , command=save)
            buttonUpdate = tk.Button(text="Update", width=20,height=2, bg="orange", fg="yellow", activebackground='white' , command=update)
            buttonDelete = tk.Button(text="Delete", width=20,height=2, bg="red", fg="yellow", activebackground='white' , command=delete)
            buttonSearch = tk.Button(text="Search", width=20,height=2, bg="green", fg="yellow", activebackground='white' , command=search)

            buttonSave.grid(row = 3, column = 0, pady = 0)
            buttonUpdate.grid(row = 3, column = 1, pady = 0)
            buttonDelete.grid(row = 4, column = 0, pady = 0)
            buttonSearch.grid(row = 4, column = 1, pady = 0)

            window.mainloop()

    main()

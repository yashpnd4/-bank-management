import json
import random 
import string
from pathlib import Path

#"JSON MEANS JavaScript Object Notation"

def read_int(prompt):
    value = input(prompt)
    if not value.isdigit():
        return None
    return int(value)

class Bank:
    database = 'data.json'
    
    data = []
    try:
        if Path(database).exists():
            with open(database) as fs:
                content = fs.read().strip()
                if content:
                    data = json.loads(content)
        else:
            print("No such file exists")
            
            
    except Exception as err: 
        print(f"an exception occured as {err}")
         
    @classmethod
    def __update(cls):
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))
            
    
    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        spchar = random.choices("!@#$%*&",k=1)
        pieces = alpha + num + spchar
        random.shuffle(pieces)
        return "".join(pieces)
    def Createaccount(self):
        accnumber = Bank.__accountgenerate()
        while any(i['accountNo.'] == accnumber for i in Bank.data):
            accnumber = Bank.__accountgenerate()
        info = {
            "name":input("Please enter your name: "),
            "age":input("Please enter your age: "),
            "email":input("Please enter your email: "),
            "pin":input("Please enter your 4 number  pin: "),
            "accountNo.":accnumber,
            "balance":0
        }
        
        if not info['age'].isdigit() or int(info['age']) < 18 or not info['pin'].isdigit() or len(info['pin']) != 4:
            print("You are not eligible for creating an account")
        else:
            print("account is being created...")
            print("account created successfully")
            for i in info:
                print(f"{i}:{info[i]}")
            print("please notedown your account number")
            
            Bank.data.append(info)
        
            Bank.__update()
            
            
            
            
    def Depositmoney(self):
        accnumber = input("please tell your account number: ")
        pin = input("please enter your pin: ")
        
        userdata = [i for i in Bank.data if i['accountNo.']==accnumber and i['pin']==pin]
        if not userdata:
            print("sorry no data is found")
        else:
            amount = read_int("how much you want to deposit: ")
            if amount is None:
                print("please enter a valid number")
                return
            if amount > 10000 or amount <= 0:
                print("the amount is too much and you can deposit below 10000")
            
            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print("ammount deposited successfully")

    def withdrawmoney(self):
        accnumber = input("please tell your account number: ")
        pin = input("please enter your pin: ")
        userdata = [i for i in Bank.data if i['accountNo.']==accnumber and i['pin']==pin]
        if not userdata:
            print("sorry no data is found")
        else:
            amount = read_int("how much you want to withdraw: ")
            if amount is None:
                print("please enter a valid number")
                return
            if amount > 10000 or amount <= 0:
                print("the amount is too much and you can withdraw below 10000")
            elif userdata[0]['balance'] < amount:
                print("sorry you dont have that much money")
            else:
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("ammount withdrawn successfully")






    def showdetails(self):
        accnumber = input("please tell your account number: ")
        pin = input("please enter your pin: ")
        userdata = [i for i in Bank.data if i['accountNo.']==accnumber and i['pin']==pin]
        print("your information are as follows:")
        if not userdata: 
            print("sorry no data is found")
        else:
            for i in userdata[0]:
                print(f"{i}:{userdata[0][i]}")




    def Updateaccount(self):
        accnumber = input("please tell your account number: ")
        pin = input("please enter your pin: ")
        userdata = [i for i in Bank.data if i['accountNo.']==accnumber and i['pin']==pin]
        if not userdata:
            print("sorry no data is found")
        else:
            print("you cannot change the age, account number and balance")
            print("you can only change the name ,email,and pin")
            print("fill the detils for change or leave it empty if no change")

            newdata = {
                "name": input("please enter your name or press enter to skip: "),
                "email": input("please enter your new email or press enter to skip: "),
                "pin": input("please enter your new pin or press enter to skip: "),
            }
                
            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']
            if newdata["email"] == "":
                newdata["email"] = userdata[0]['email']
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]['pin']

            newdata['age'] = userdata[0]['age']
            newdata['accountNo.'] = userdata[0]['accountNo.']
            newdata['balance'] = userdata[0]['balance']

            updated = False
            for i in newdata:
                if newdata[i] != userdata[0][i]:
                    userdata[0][i] = newdata[i]
                    updated = True

            if updated:
                Bank.__update()
                print("Updated successfully")




    def delete(self):
        accnumber = input("please tell your account number: ")
        pin = input("please enter your pin: ")
        userdata = [i for i in Bank.data if i['accountNo.']==accnumber and i['pin']==pin]
        if not userdata:
            print("sorry no data is found")
        else:
            check = input("press Y/y if you actually want to delete the account or press N/n")
            if check == "Y" or check == "y":
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                Bank.__update()
                print("Deleted successfully")
            elif check == "N" or check == "n":
                print("Account not deleted")
                Bank.__update()


            



    def Displayaccount(self):
        accnumber = input("please tell your account number: ")
        pin = input("please enter your pin: ")
        userdata = [i for i in Bank.data if i['accountNo.']==accnumber and i['pin']==pin]
        if not userdata:
            print("sorry no data is found")
        else:
            for i in userdata[0]:
                if i == "pin":
                    print(f"{i}:****")
                else:
                    print(f"{i}:{userdata[0][i]}")

user =Bank()
print("press 1 for creating an account")
print("press 2 for depositing the money in the bank account")
print("press 3 for withdrawing the money from the bank account")
print("press 4 to show the details")
print("press 5 for updating the details")
print("press 6 for deleting the account")
print("press 7 for displaying the account details")

check = read_int("Tell your response: ")

if check == 1:  
    user.Createaccount()
elif check == 2:
    user.Depositmoney()
elif check == 3:
    user.withdrawmoney()
elif check == 4:
    user.showdetails()
elif check == 5:
    user.Updateaccount()
elif check == 7:
    user.Displayaccount()
else:
    print("please choose one of the given options")
    
    

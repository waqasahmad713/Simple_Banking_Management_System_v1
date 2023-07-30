import pickle
import os
import pathlib
class Account :
    accNo = 0
    name = ''                        #class veriables
    deposit=0
    type = ''
    
    def createAccount(self):
        self.accNo= int(input("Enter the account no : "))
        self.name = input("Enter the account holder name : ")
        self.type = input("Ente the type of account \n Current Account \n Saving Account\n: ")
        self.deposit = int(input("Enter The Initial amount\n500 for Saving \n1000 for current\n:"))
        print("\n\n\nCongrats Account Created")
    
    def showAccount(self):
        print("Account Number : ",self.accNo)
        print("Account Holder Name : ", self.name)
        print("Type of Account",self.type)
        print("Balance : ",self.deposit)
    
    def modifyAccount(self):
        print("Account Number : ",self.accNo)
        self.name = input("Modify Account Holder Name :")
        self.type = input("Modify type of Account :")
        self.deposit = int(input("Modify Balance :"))
        
    def depositAmount(self,amount):
        self.deposit += amount
    
    def withdrawAmount(self,amount):
        self.deposit -= amount
    
    def report(self):
        print(self.accNo, " ",self.name ," ",self.type," ", self.deposit)
    
    def getAccountNo(self):
        return self.accNo
    def getAcccountHolderName(self):
        return self.name
    def getAccountType(self):
        return self.type
    def getDeposit(self):
        return self.deposit
    

def intro():
    print("\t\t\t\t**********************")
    print("\t\t\t\tWAQAS BANK")
    print("\t\t\t\t**********************")
    print("\t\t\t\tCreadit gose to :")
    print("\t\t\t\tDR AMIR AKBER SIR AND HILAL KTK")


def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)

def displayAll():
    file = pathlib.Path("accounts.data")        #provide data from specfic path or file
    if file.exists ():
        infile = open('accounts.data','rb')    #read binary mode
        mylist = pickle.load(infile)
        for item in mylist :
            print(item.accNo," ", item.name, " ",item.type, " ",item.deposit )
        infile.close()
    else:
        print("No records to display")
        

def displaySp(num): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist :
            if item.accNo == num :
                print("Your account Balance is = ",item.deposit)
                found = True
    else :
        print("No records to Search")
    if not found :
        print("No existing record with this number")

def depositAndWithdraw(num1,num2): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist :
            if item.accNo == num1 :
                if num2 == 1 :
                    amount = int(input("Enter the amount to deposit : "))
                    item.deposit += amount
                    print("Your account is updated")
                elif num2 == 2 :
                    amount = int(input("Enter the amount to withdraw : "))
                    if amount <= item.deposit :
                        item.deposit -=amount
                    else :
                        print("You withdraw larger amount")
                
    else :
        print("No records to Search")
    outfile = open('newaccounts.data','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')

    
def deleteAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist :
            if item.accNo != num :
                newlist.append(item)
        os.remove('accounts.data')          
        outfile = open('newaccounts.data','wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
     
def modifyAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist :
            if item.accNo == num :
                item.name = input("Enter the account holder name : ")
                item.type = input("Enter the account Type : ")
                item.deposit = int(input("Enter the Amount : "))
        
        outfile = open('newaccounts.data','wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
   

def writeAccountsFile(account) : 
    
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else :
        oldlist = [account]
    outfile = open('newaccounts.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')
    
        
# start of the program
num=0
intro()
while True:
    #system("cls");
    print("\tMAIN MENU")
    print("\t1. NEW ACCOUNT")
    print("\t2. DEPOSIT AMOUNT")
    print("\t3. WITHDRAW AMOUNT")
    print("\t4. BALANCE ENQUIRY")
    print("\t5. ALL ACCOUNT HOLDER LIST")
    print("\t6. CLOSE AN ACCOUNT")
    print("\t7. Update  ACCNT")
    print("\tSelect Your Option (1-7) ")
    ch =input("enter your choice:")
    #system("cls"); 
    if ch == '1':
        writeAccount()
    elif ch =='2':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 1)
    elif ch == '3':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 2)
    elif ch == '4':
        num = int(input("\tEnter The account No. : "))
        displaySp(num)
    elif ch == '5':
        displayAll()
    elif ch == '6':
        num =int(input("\tEnter The account No. : "))
        deleteAccount(num)
        print("Account deleted")
    elif ch == '7':
        num = int(input("\tEnter The account No. : "))
        modifyAccount(num)
    else :
        print("Invalid choice")
    ans=input("do you want to continue? y/n")
    if ans not in['y','Y','n','N']:
        print("Sorry, please use y/n")
        ans=input("do you want to continue? y/n")
    if ans in['n','N']:
        print("Thank you for using  waqas Banking Management system")
        # import package and making object 
        import turtle 
        screen = turtle.Screen() 
          
        # method to draw ellipse 
        def draw(rad):   # rad --> radius for arc 
            for i in range(2): 
                turtle.circle(rad,90) 
                turtle.circle(rad//2,90) 
          
        
        screen.setup(500,500) # Set screen size 
        screen.bgcolor('black') # Set screen color 
        col=['violet','blue','green','yellow', 'orange','red'] # Colors
        val=10
        ind = 0 # some integers
        turtle.speed(100) # turtle speed 
        for i in range(36): # loop for multiple ellipse 
                 turtle.seth(-val) # oriented the ellipse at angle = -val 
                 turtle.color(col[ind]) # color of ellipse 
                 if ind==5: # to access different color 
                     ind=0
                 else: 
                     ind+=1
                 draw(80) # calling method 
                 val+=10 # orientation change 
        turtle.hideturtle() # for hiding the turtle 
        break

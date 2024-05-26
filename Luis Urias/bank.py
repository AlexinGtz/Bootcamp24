import datetime

class Transaction:
    def __init__(self, date, amount, type, client):
        self.date = date
        self.amount = amount
        self.type = type
        self.client = client
 

class Bank:
    def __init__(self):
        self.users= [
            Employee('Luiginini', '123'),
            Client('Pedro','123'),
            Client('Pablo','123'),
        ]

    def singup_user(self, name, password):
        new_client = Client(name, password)
        self.users.append(new_client)

    def login_user(self, name, password):
        for user in self.users:
            if(user.name == name.strip()):
                if(user.password != password):
                    print("Wrong password. Try again!")
                    return None
                else:
                    print("Logged in\n")
                    return user
                
    def print_user_list(self):
        counter = 1
        print("| # |\tName\t|\tType\t|")
        print("-----------------------------------------")
        for user in self.users:
            print(f"| {counter} |\t{user.name}\t|\t{user.type}\t|")
            counter += 1


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.type = None
    
    def greet(self):
        print(f"Hello Mr./Ms. {self.name}, welcome to BootBank")

class Client(User):
    def __init__(self, name, password, transactions: Transaction = [], balance = 0):
        super().__init__(name, password)
        self.type = 'CLIENT'
        self.transactions = transactions
        self.balance = balance

    def deposit(self, amount):
        self.balance +=  amount
        self.transactions.append(
            Transaction(datetime.datetime.now(), amount, 'DEPOSIT', name)
        )
        print("Successfully deposited amount")
        print(f"Your new balance is ${self.balance}.00")
        return


    def withdraw(self, amount):
        if(self.balance < amount):
            print("You don't have enough cash!")
            return
        
        self.balance -=  amount
        self.transactions.append(
            Transaction(datetime.datetime.now(), amount, 'WITHDRAW', name)
        )
        print("Successfully withdrew amount")
        print(f"Here's is you money ${amount}")
        print(f"Your new balance is ${self.balance}.00")
        return
     
    def log_transactions(self):
        counter = 1
        print(f"| # |\tAmount\t\t|\tDate                        \t|\tType\t\t|\tClient\t\t|")
        print("-----------------------------------------")
        for txn in self.transactions:
            if(txn.client == name):
                print(f"| {counter} |\t{txn.amount}\t\t|\t{txn.date}\t|\t{txn.type}\t\t|\t{txn.client}\t\t|")
                counter += 1
        print(f"Current balance \t\t\t\t\t ${self.balance}.00 |")

    def log_current_balance(self):
        print(f"Current balance \n ${self.balance}.00")

class Employee(User):
    def __init__(self, name, password): 
        super().__init__(name, password)
        self.type = 'EMPLOYEE'


# ---------------- APP ---------------

bankDatabase = Bank()
print("Welcome to Bootbank!")

exitApp = False

while(not exitApp):
    option = int(input("Do you want to log in or exit the app?\n1. Log in\n2. Exit App\n\n"))

    if(option == 1):
        #User login
        name = input("Please enter your name\n")
        password = input("Please enter your password\n")
        currentUser = bankDatabase.login_user(name, password)
        if(not currentUser):
            print("Please try again")
        else:
            currentUser.greet()
            logoutUser = False
            while (not logoutUser):
                if(currentUser.type == 'CLIENT'):
                    userOption = int(input("What action do you want to do?\n1. Deposit\n2. Withdraw\n3. See your transactions\n4. See your current balance\n5. Log out\n\n"))
                    match userOption:
                        case 1:
                            amount = int(input("Enter your deposit amount:\t"))
                            if (amount <= 0):
                                print("That's not a valid quantity")
                                continue
                            currentUser.deposit(amount)
                            continue
                        case 2:
                            amount = int(input("Enter your withdrawal amount:\t"))
                            if (amount <= 0):
                                print("That's not a valid quantity")
                                continue
                            currentUser.withdraw(amount)
                            continue
                        case 3:
                            currentUser.log_transactions()
                            continue
                        case 4:
                            currentUser.log_current_balance()
                            continue
                        case 5:
                            logoutUser = True
                            continue
                elif(currentUser.type == 'EMPLOYEE'):
                    userOption = int(input("What action do you want to do?\n1. Singup User\n2. List Users\n3. Log out\n\n"))
                    match userOption:
                        case 1:
                            name = input("Enter the user's name:\n\n")
                            password = input("Enter the user's password:\n\n")
                            bankDatabase.singup_user(name, password)
                            continue
                        case 2:
                            bankDatabase.print_user_list()
                            continue
                        case 3:
                            logoutUser = True
                            continue
                # else:
                #     print("User type not recognized\n")           
    elif(option == 2):
        #Exit App
        exitApp = True
    else: 
        print("I don't know that option. Please try again!")
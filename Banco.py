import datetime

class Transaction:
    def __init__(self, date, amount, type):
        self.date = date
        self.amount = amount
        self.type = type

class Bank:
    def __init__(self):
        self.users = [
            Employee('Alex', '1234'),
        ]

    def signup_user(self, name, password):
        new_client = Client(name, password)
        self.users.append(new_client)

    def login_user(self, name: str, password: str):
        for user in self.users:
            if(user.name == name.strip()):
                if(user.password != password):
                    print('Wrong Password. Try Again!')
                    return None
                else:
                    print('Logged In\n')
                    return user

    def print_user_list(self):
        counter = 1
        print('| #\t|\tName\t|\tType\t|')
        print('------------------------')
        for user in self.users:
            print(f'| {counter}\t|\t{user.name}\t|\t{user.type}\t|')
            counter += 1

class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.type = None
    
    def greet(self):
        print(f'Hello Mr./Ms. {self.name}, welcome to BootBank')

class Client(User):
    def __init__(self, name: str, password: str, transactions: list[Transaction] = [], balance: int = 0):
        super().__init__(name, password)
        self.type = 'CLIENT'
        self.balance = balance
        self.transactions = transactions

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(
            Transaction(datetime.datetime.now(), amount, 'DEPOSIT')
        )
        print('Succesfully deposited amount')
        print(f'Your new balance is ${self.balance}.00')
        return

    def withdraw(self, amount):
        if(self.balance < amount):
            print('You\'re broke dude, don\' do this')
            return
        self.balance -= amount
        self.transactions.append(
            Transaction(datetime.datetime.now(), amount, 'WITHDRAW')
        )
        print('Succesfully withdrew amount')
        print(f'Here\'s your money ${amount}')
        print(f'Your new balance is ${self.balance}.00')
        return

    def log_transactions(self):
        counter = 1
        print('| #\t|\tAmount\t|\tDate\t|\tType\t|')
        print('------------------------')
        for txn in self.transactions:
            print(f'| {counter}\t|\t{txn.amount}\t|\t{txn.date}\t|\t{txn.type}\t|')
            counter += 1
        print(f'| Current Balance \t\t\t\t\t\t ${self.balance}.00 |')

    def log_current_balance(self):
        print(f'Current Balance\n${self.balance}.00')

class Employee(User):
    def __init__(self, name, password):
        super().__init__(name, password)
        self.type = 'EMPLOYEE'

# -----------------APP------------------------

bankDatabase = Bank()
print('Welcome to BootBank!!!!')

exitApp = False

while (not exitApp):
    option = int(input('Do you want to log in or exit the app?\n1. Login\n2. Exit app\n\n'))
    if(option == 1):
        name = input('Please enter your name\n')
        password = input('Please enter your password\n')
        currentUser = bankDatabase.login_user(name, password)
        if(not currentUser):
            print('Please try again')
        else:
            currentUser.greet()
            logoutUser = False
            while (not logoutUser):
                if(currentUser.type == 'CLIENT'):
                    userOption = int(input('What action do you want to do?\n1. Deposit\n2. Withdraw\n 3. See your transactions\n4. See current balance\n5. Logout\n'))
                    match userOption:
                        case 1:
                            amount = int(input('Enter your deposit amount:\t'))
                            if(amount <= 0):
                                print('That\'s not a valid quantity')
                                continue
                            currentUser.deposit(amount)
                            continue
                        case 2:
                            amount = int(input('Enter your withdrawal amount:\t'))
                            if(amount <= 0):
                                print('That\'s not a valid quantity')
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
                    userOption = int(input('What action do you want to do?\n1. Signup User\n2. List Users\n3. Logout\n'))
                    match userOption:
                        case 1:
                            name = input('Enter the user\'s name\n\n')
                            password = input('Enter the user\'s password\n\n')
                            bankDatabase.signup_user(name, password)
                            continue
                        case 2:
                            bankDatabase.print_user_list()
                            continue
                        case 3:
                            logoutUser = True
                            continue
    elif(option == 2):
        exitApp = True
    else:
        print('I don\'t know that option, please try again')

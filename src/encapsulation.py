#print inside a method
class Bank:
    def __init__(self):
        self.__balance = 5000

    def show_balance(self):
        print(self.__balance)

b = Bank()
b.show_balance()
#getter method
class Bank:
    def __init__(self):
        self.__balance = 5000
    def get_balance(self):
        return self.__balance
b = Bank()
print(b.get_balance())
#name mangling
class Bank:
    def __init__(self):
        self.__balance = 5000
b = Bank()
print(b._Bank__balance)



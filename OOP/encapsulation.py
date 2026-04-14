
#keeping your data safe inside the capsule of the object, you restict access direct access to some
#data so people dont accidenaly messup

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog_1 = Dog('Bob', 18)
print(dog_1.name)
print(dog_1.age)

#encapsulation

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance  # The '__' makes it private
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited {amount}")
#
#     def get_balance(self):
#         return self.__balance
#
# account = BankAccount(1000)
# account.deposit(500)
# # print(account.__balance)  # This would throw an error (Private!)
# print(account.get_balance()) # This works (Controlled access)

#sample

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}")

    def withdraw(self, amount):
        withdraw = self.__balance - amount
        print(f"Withdraw {amount}")

account = BankAccount(1000)
account.deposit(500)
account.withdraw(500)



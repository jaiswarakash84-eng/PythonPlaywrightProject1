# def greet(name, greeting):
#     print(f'{greeting}, {name}')
#
# greet('Akax', 'orxo')
#
# def fun():
#     print('hello world')
#
# fun()
# fun()
# fun()
#
# for i in range(5):
#     print("Hello")
#
#
# list = ["akax", "orxo","shery"]
# for name in list:
#     print(f"hello , {name}")
#
# i = 0
# while i < 5:
#     print(i)
#     i += 1
#
# a = 1
# b = 2
# print(a>b)
# print(a>=b)
# print(a<b)
#
#
#
# message = input("Enter your message: ")
#
# if message == "Hi":
#     print("Hello")
# elif message == "How are you?":
#     print("how are you?")
# else:
#     print("Sorry, i dont understand")
#
# a,b = 10 , "akash"
#
# try:
#     print(a + b)
# except TypeError as e:
#     print("please enter valid number")
# print("continue")
#
# import math
#
# print(math.sqrt(5))
from operator import add

#simple project
bot_name = "Bob"
print(f'hello! am {bot_name}! how can i help you?')

while True:
    user_input = input('you input:').lower()
    if user_input in ['hi', 'hello']:
        print(f'{bot_name} welcome to python')
    elif user_input in ['bye', 'see you']:
        print(f'{bot_name} bye have a nice day!')
    elif user_input in ['+', 'add']:
        print(f'{bot_name} : sure lets add some number please enter')
        try:
            num1 = int(input('please enter a number: '))
            num2 = int(input('please enter a number: '))
            print(f'{bot_name}: The sum is {num1 + num2}')
        except ValueError:
            print(f'{bot_name}: Oops')
    else:
        print(f'{bot_name}: am sorry')
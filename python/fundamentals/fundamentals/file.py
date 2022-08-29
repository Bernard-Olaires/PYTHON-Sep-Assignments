num1 = 42 # varriable declaration and integer 
num2 = 2.3 # varriable declaration and float 
boolean = True # varriable declaration and boolean
string = 'Hello World' # varriable declaration and string

pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] 
#varriable declaration and Composite List

person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
#varriable declaration and Composite Dictionary 

fruit = ('blueberry', 'strawberry', 'banana')
#varriable declaration and tuple 

print(type(fruit))
# print to console, type check

print(pizza_toppings[1])
# print to console, list access value

pizza_toppings.append('Mushrooms')
# list add value

print(person['name'])
#print to console, dictionary access value

person['name'] = 'George'
# dictionary change value 

person['eye_color'] = 'blue'
# dictionary change value

print(fruit[2])
# print to console , list acess value 

# conditional if - elif - else, print to console
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")


for x in range(5):
    print(x)
# for loop start at 0 and goes up until 5


for x in range(2,5):
    print(x)
# for loop starts at 2 and goes up until 5 

for x in range(2,10,3):
    print(x)
# for loops starts at 2 goes up until 3, increments of 3 


x = 0
while(x < 5):
    print(x)
    x += 1
# while loop, varriable declaration

pizza_toppings.pop()
# list delete value at end 

pizza_toppings.pop(1)
# list delete value at index

print(person)
#print to conbsole of dictionary


person.pop('eye_color')
# dictionary delete value

print(person)
# print to console of dictionary

# for loop throygh a list
for topping in pizza_toppings:
    # conditional if
    if topping == 'Pepperoni':
        # continues
        continue
    # print to console
    print('After 1st if statement')
    # conditional if
    if topping == 'Olives':
        # stops the loop
        break

# function declaration


def print_hello_ten_times():
    # for loop starts at 0 goes up until 10
    for num in range(10):
        # print to console
        print('Hello')


# function call
print_hello_ten_times()

# fuction Declaration with parameter x


def print_hello_x_times(x):
    # for loop up until  given number x
    for num in range(x):
        # print to console
        print('Hello')


# function call arguement of 4
print_hello_x_times(4)

# function declaration with default parameter


def print_hello_x_or_ten_times(x=10):
    # for loop until x
    for num in range(x):
        # prtint to console
        print('Hello')


# function call goes to 10
print_hello_x_or_ten_times()
# function call goes to 4
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
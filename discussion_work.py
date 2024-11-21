# QUESTIONS
# A Python program that prints all even 
# numbers btn 1 and 20 using a for loop.

for num in range(1, 21):  
    if num % 2 == 0:      
        print(num)

#Use a while loop to ask the user to input a number 
# until they provide a number greater than 10.

while True:
    num = int(input("Enter a number greater than 10 : "))
    if num > 10:
        print("You entered a valid number.")
        break
    else:
        print("Invalid command , Please enter a number greater than 10 .")
       

#3 Write a program that prints the multiplication table(from 1 to 10) 
# for numbers from 1-5 using nested for loops.

for i in range(1, 6):  # Loop through numbers from 1 to 5
    print(f"Multiplication table for {i}:")
    for j in range(1, 11):  
        print(f"{i} x {j} = {i * j}")
    print()  

#4 Given a list of integers [4,7,2,9,12,15], write a program using 
# a for loop to find the sum of all odd numbers and
# print the result.
# numbers = [4, 7, 2, 9, 12, 15]
# sum_of_odds = 0

for num in numbers:
    if num % 2 != 0:  # Check if the number is odd
        sum_of_odds += num

print("The sum of all odd numbers is:", sum_of_odds)

#  LISTS
#1)Create a list of 5 fruits and print each fruit on a new
#  line using a for loop.

fruits = ['apple', 'pine apple', 'mango', 'berry', 'pear']
for fruit in fruits:
    print(fruit)

#2) Write a function that takes a list of numbers and returns a 
# new list with each number squared. 
# Example: [1,2,3] should become [1,4,9]

def square_numbers(numbers):
    return [num ** 2 for num in numbers]
numbers = [1, 2, 3]
squared = square_numbers(numbers)
print(squared)  

# Write a Python program that takes two lists, list1 = [1,2,3] and 
# list2 = [4,5,6] and combines them into
# a single list, combined = [1,4,2,5,3,6].

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = []

# Using zip to combine the lists
for x, y in zip(list1, list2):
    combined.append(x)
    combined.append(y)
print(combined)  


 #4) Given a list of numbers, [3,1,4,5,9,2], write a program to 
 # find and print the two largest numbers
 # in the list without using the max() function.

numbers = [3, 1, 4, 1, 5, 9, 2]

sorted_numbers = sorted(numbers, reverse=True)
two_largest = sorted_numbers[:2]

print(two_largest) 

#DICTIONARIES
# 1) Create a dictionary with three key-value pairs representing a student's 
# information: name,age , grade.
# Print each key-value pair on a new line.

student = {
    'name': 'latifah',
    'age': 21,
    'grade': 'A'
}

for key, value in student.items():
    print(f"{key}: {value}")

#2) Write a function that takes a dictionary of people's names 
# and their ages,{'Alice': 24, 'Bob': 19, 'Charlie': 30}
#and returns a list of names of people who are 21 or older.

def eligible_ages(age_dict):
    return [name for name, age in age_dict.items() if age >= 21]

people = {'Alice': 24, 'Bob': 19, 'Charlie': 30}
eligible = eligible_ages(people)
print(eligible)  


#3) Given a dictionary representing items in a store with their 
# prices,{'apple': 0.5, 'banana': 0.3, 'orange': 0.7},
# write a program that takes a list of times bought,['apple', 'orange', 'banana', 'banana'],
# and calculates the total cost.

def calculate_total_cost(items_bought, store_prices):
    total = 0
    for item in items_bought:
        total += store_prices.get(item, 0)  
    return total

store = {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}
items = ['apple', 'orange', 'banana', 'banana']
total_cost = calculate_total_cost(items, store)
print(total_cost)  

def word_count(sentence):
    words = sentence.split()
    word_dict = {}
    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict

# Example usage:
sentence = "hello world hello"
word_counts = word_count(sentence)
print(word_counts) 

#OBJECT ORIENTED PROGRAMMING
#2) Create a class called car with attributes brand and color. Instantiate an object of the Car class
#  and print it's attributes
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

# Instantiate a Car object
my_car = Car("Toyota", "red")
print(my_car.brand) 
print(my_car.color) 

#2) Add a method called start_engine to the Car class that prints a 
# message saying the engine of the car has started.
#  Create an instance of Car and call the method.
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engine(self):
        print(f"The engine of the {self.brand} car has started.")

# Instantiate and use the method
my_car = Car("Toyota", "red")
my_car.start_engine()

#3) Create a class called BankAccount with attributes account_number and balance. Add methods to:
# Deposit an amount
# Withdraw an amount (only if sufficient balance exists)
# Print the account balance.
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Balance: {self.balance}")

# Example usage:
account = BankAccount(123456, 100)
account.deposit(50)  
account.withdraw(30)  
account.check_balance()  

#4) Implement a class called Library that manages a collection of books.
# Each book has a tittle, author, and available status. The class should have methods to:
# Add a book to the library.Remove a book from the library. 
# Check if a book is available by title. 
# Borrow a book (mark it as unavailable if it's available). 
# Return a book(mark it as available again if it was borrowed)

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author):
        self.books[title] = {'author': author, 'available': True}
        print(f"Added '{title}' by {author}.")

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
            print(f"Removed '{title}'.")
        else:
            print(f"'{title}' not found in library.")

    def check_availability(self, title):
        if title in self.books and self.books[title]['available']:
            print(f"'{title}' is available.")
        else:
            print(f"'{title}' is not available.")

    def borrow_book(self, title):
        if title in self.books and self.books[title]['available']:
            self.books[title]['available'] = False
            print(f"You borrowed '{title}'.")
        else:
            print(f"'{title}' is not available for borrowing.")

    def return_book(self, title):
        if title in self.books:
            self.books[title]['available'] = True
            print(f"Returned '{title}'.")
        else:
            print(f"'{title}' is not found in the library.")

# Example usage:
library = Library()
library.add_book("1984", "George Orwell")
library.check_availability("1984")  
library.borrow_book("1984")  
library.return_book("1984") 

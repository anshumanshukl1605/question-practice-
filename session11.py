# Question 1:
# Create a Student class.
# Take the student's name using __init__.
# Store the name inside the object.
# Create one Student object with the name "Anshuman".
# Print the student's name.

class Student:
    def __init__(self, name,score):
        self.name = name
        self.score=score


student1 = Student("Anshuman",90)

print(student1.name,student1.score)
#print(student1.score)


# Question 2:
# Create a Car class.
# Store the car's brand and price using __init__.
# Create one object with:
# brand = "Toyota"
# price = 1500000
# Print the brand and price.
class car :
  def __init__(self,brand,price ):
      self.brand= brand
      self.price= price 
car1= car("toyota",1500000)
print(car1.brand) 
print(car1.price)





# Question 3:
# Create a Student class.
# Store student's name and marks using __init__.
# Create two Student objects:
# student1 → "Anshuman", 90
# student2 → "Rahul", 85
# Print both students' names and marks.

class student:
  def __init__(self,name,marks):
      self.name=name
      self.marks=marks
student_1 = student("anshuman",90)
student_2 = student("rahul",85)
print(student_1.name,student_1.marks)
print(student_2.name,student_2.marks)


# Question 4:
# Create an Employee class.
# Store these three values using __init__:
# name
# department
# salary
#
# Create one Employee object:
# name = "Rahul"
# department = "IT"
# salary = 50000
#
# Print all three values.
class employee:
    def __init__(self,name,department,salary):
         self.name = name
         self.department = department
         self.salary = salary

employee_1=employee ("rahul","it",50000)
print (employee_1.name,employee_1.department,employee_1.salary)



# Question 5:
# Create a Product class.
# Store product name and price using __init__.
#
# Create two objects:
# product_1 → "Laptop", 50000
# product_2 → "Mouse", 1000
#
# Print only product_2's name and price.

class product :
  def __init__ (self,name,price) :
    self.name = name
    self.price = price 
product_1 = product ("laptop",50000)
product_2 = product ("mouse",1000)
print(product_2.name,product_2.price)  




# Question 6:
# Create a BankAccount class.
# Store account_holder and balance using __init__.
#
# Create two objects:
# account_1 → "Anshuman", 10000
# account_2 → "Rahul", 5000
#
# Print only account_1's balance.

class bankaccount:
  def __init__ (self,account_holder,balance):
      self.account_holder = account_holder
      self.balance = balance 
account_1 = bankaccount ("anshuman",10000)
account_2 = bankaccount ("rahul",5000)   
print(account_1.balance)   

# Question 7:
# Create a Book class.
# Store title, author and price using __init__.
#
# Create two objects:
# book_1 → "Python Basics", "Rahul", 500
# book_2 → "SQL Basics", "Aman", 400
#
# Print book_1's title and book_2's price.
class book:
  def __init__(self,title,author,price):
      self.title = title 
      self.author = author 
      self.price = price
book_1 = book("python basics","rahul",500)
book_2 = book("sql basics ","aman",400)
print(book_1.title)
print(book_2.price)      



# Question 8:
# Create a Laptop class.
# Store brand, model and price using __init__.
#
# Create two objects:
# laptop_1 → "Dell", "Inspiron", 55000
# laptop_2 → "HP", "Pavilion", 60000
#
# Print:
# 1. laptop_1's brand
# 2. laptop_2's model
# 3. laptop_1's price


class laptop :
  def __init__(self,brand,model,price):
      self.brand = brand 
      self.model = model 
      self.price = price 
laptop_1=  laptop("dell","inspiron",55000)
laptop_2 = laptop("hp","pavilion",60000)
print(laptop_1.brand,laptop_2.model,laptop_1.price)      

#-----------------------------------------------------------------------------class with method 

# Question 4:
# Create a BankAccount class.
# Store account_holder and balance using __init__.
#
# Create a method called show_balance().
# show_balance() should print:
# "Anshuman has 10000 balance"
#
# Create account_1 with:
# account_holder = "Anshuman"
# balance = 10000
#
# Then call show_balance().

class bankaccount :
  def __init__(self,account_holder,balance):
    self.account_holder = account_holder
    self.balance = balance 
  def show_balance(self):
    print(self.account_holder,"has",self.balance,"balance")
account_1 = bankaccount ("anshuman",1000)

account_1.show_balance()




# Question 5:
# Create a Student class.
# Store name and marks using __init__.
#
# Create a method show_details().
# Method ko self.name aur self.marks use karke print karna hai.
#
# Create:
# student_1 → "Anshuman", 90
#
# Then call show_details().



class student:
  def __init__(self,name,marks):
    self.name = name
    self.marks = marks 
  def show_details(self):
    print (self.name , "marks is :" ,self.marks)
student_1 = student ("anshuman" ,90)    
student_1.show_details()




# Question 6:
# Create an Employee class.
# Store name and salary using __init__.
#
# Create a method show_salary().
# It should print:
# "Rahul salary is 50000"
# or
# "Anshuman salary is 60000"
#
# Create two objects:
# employee_1 → "Rahul", 50000
# employee_2 → "Anshuman", 60000
#
# Call show_salary() for both objects.



class employee:
  def __init__ (self,name,salary):
    self.name = name 
    self.salary = salary 
  def show_salary(self):
    print(self.name,"salary is:",self.salary)
employee_1 = employee("rahul",50000)
employee_2 = employee("anshuman" ,60000)
employee_1.show_salary()
employee_2.show_salary()
    


# Question 7:
# Create a Product class.
# Store product name and price using __init__.
#
# Create a method called show_discount_price().
# Method mein price par 10% discount calculate karo
# aur final price print karo.
#
# Create:
# product_1 → "Laptop", 50000
#
# Then call show_discount_price().

class product :
  def __init__(self,name,price):
    self.name = name
    self.price = price
  def show_discount_price (self):
      discount = self.price * 10 / 100
      final_price = self.price - discount
      print(final_price)
product_1 = product ("laptop",50000)
product_1.show_discount_price()

      


# Question 8:
# Create a Calculator class.
#
# Create a method called add().
# add() method ko ek number parameter milega.
# Us number ko object ke stored number ke saath add karo.
#
# Create calculator_1 with number = 10
# Then:
# calculator_1.add(5)
#
# Expected output:
# 15


class Calculator :
  def __init__(self,number):
    self.number = number

  def add (self,x):
   result = self.number + x
   print(result)
Calculator_1 = Calculator (10)
Calculator_1.add(5)


   # Question 9:
# Create a Calculator class.
# Store one number using __init__.
#
# Create a multiply() method.
# multiply() ko ek number parameter milega.
# Stored number ko us parameter se multiply karo.
#
# Create:
# calculator_1 → number = 10
#
# Call:
# calculator_1.multiply(5)
#
# Expected output:
# 50

class Calculator :
 def __init__(self,x):
   self.x = x
 def multiply(self,y):
  result = self.x * y
  print(result)
Calculator_1 = Calculator(10)
Calculator_1.multiply(5)  

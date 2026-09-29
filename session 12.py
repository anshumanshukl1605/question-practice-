import numpy as np
#-------------------------------------------------------------------------------> topic_1





# Q1. Create a NumPy array containing the numbers:
# 10, 20, 30, 40, 50
# Print the array.
# Print the shape of the array.
# Print the data type (dtype) of the array.
a = np.array([10, 20, 30,40,50])
print(a)
print(np.shape(a))
print(a.dtype)




# Q2. Create a NumPy array containing the following values:
# 12, 24, 36, 48, 60
# Print the array.
# Print the number of elements in the array.
# Print the shape of the array.
# Print the data type (dtype) of the array.

a = np.array([12,24,36,48,60])
print(a)
print(a.size)
print(a.shape)
print(a.dtype)





# Q3. Create a 2D NumPy array representing the marks of 2 students
# in 3 subjects:
# Student 1: 75, 80, 85
# Student 2: 65, 70, 90
# Print the array.
# Print the shape of the array.
# Print the total number of elements in the array.
# Print the data type (dtype) of the array.
a = np.array([ [ 75, 80, 85], [65, 70, 90] ])
print (a)
print (a.shape)
print (a.size)
print (a.dtype)






# Q4. Create a NumPy array containing these decimal values:
# 10.5, 20.5, 30.5, 40.5
# Print the array.
# Print its dtype.
# Print its shape.
# Print the total number of elements.
# Do not manually specify the dtype.
# Let NumPy determine the dtype automatically.
a = np.array([10.5, 20.5, 30.5, 40.5])
print(a)
print(a.dtype)
print(a.shape)
print(a.size)







# Q5. Create a NumPy array containing:
# 10, 20.5, 30, 40.5
# Print the array.
# Print the dtype of the array.
# Print the shape of the array.
# Print the total number of elements.
# Observe what dtype NumPy chooses when integers and floats
# are present in the same array.
a = np.array([10, 20.5, 30, 40.5])
print(a)
print(a.dtype)
print(a.shape)
print(a.size)





# Q6. Create a 2D NumPy array representing the sales of 3 products
# across 4 days:
# Product 1: 100, 120, 110, 130
# Product 2: 80, 90, 95, 100
# Product 3: 150, 140, 160, 170
# Print the array.
# Print the shape of the array.
# Print the total number of elements.
# Print the dtype of the array.
# Without using a loop, determine from the shape and size:
# - How many products are represented ..........3
# - How many days of sales data are present......4
a = np.array([
    [100, 120, 110, 130],
    [80, 90, 95, 100],
    [ 150, 140, 160, 170]
])
print(a)
print(a.shape)
print(a.size)
print(a.dtype)
#------------------------------------------------------------------------>topic_2 ------------> Vectorized Arithmetic
     
# Q1. Create a NumPy array containing the following prices:
# 100, 200, 300, 400, 500
# Increase every price by 10 using a vectorized NumPy operation.
# Do not use a loop.
# Print the original prices.
# Print the updated prices.
a = np.array([100, 200, 300, 400, 500])
print(a)
b = (a+10)



# Q2. Create a NumPy array containing:
# 10, 20, 30, 40, 50
# Using vectorized arithmetic:
# 1. Add 10 to every element.
# 2. Subtract 5 from the result.
# 3. Multiply the result by 2.
# 4. Divide the result by 5.
# 5. Find the remainder when the result is divided by 3.
# Print the final result.
a = np.array([10, 20, 30, 40, 50])
a = a + 10
a = a - 5
a = a * 2
a = a / 5
a = a % 3
print(a)





# Q3. A shop has recorded the prices of 5 products:
# 100, 200, 300, 400, 500
# Create a NumPy array.
# Increase every price by 20%.
# Use vectorized arithmetic.
# Then create a Boolean array that checks
# which updated prices are greater than 300.
# Print:
# 1. Original prices
# 2. Updated prices
# 3. Boolean result
a = np.array([100, 200, 300, 400, 500])
b = a * 1.20
c = b > 300
print(a)
print(b)
print(c)







# Q4. A company has two NumPy arrays representing sales
# from two different weeks.
# Week 1:
# 100, 200, 300, 400, 500
# Week 2:
# 20, 40, 60, 80, 100
# Create both NumPy arrays.
# Add the two arrays element-by-element using vectorized arithmetic.
# Then find the difference between Week 1 and Week 2
# element-by-element.
# Print:
# 1. Week 1 sales
# 2. Week 2 sales
# 3. Combined sales
# 4. Difference in sales
week_1 = np.array([100, 200, 300, 400, 500])
week_2 = np.array([20, 40, 60, 80, 100])
Combined_sales = week_1 +week_2
difference_sales = week_1 - week_2
print(week_1)
print(week_2)
print(Combined_sales)
print(difference_sales)


# Q5. Create two NumPy arrays:
# Array A: 10, 20, 30, 40, 50
# Array B: 2, 4, 5, 8, 10
# Multiply Array A and Array B element-by-element
# using vectorized arithmetic.
# Print the result.
a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 5, 8, 10]) 
c = a*b
print(c)





# Q6. A company has recorded the following sales:
# 120, 250, 180, 300, 90
# Create a NumPy array.
# Check which sales values are greater than 200.
# Then check which sales values are greater than or equal to 180.
# Print both Boolean arrays.
a = np.array([120, 250, 180, 300, 90])
b = a > 200 
c= a>=180
print(b)
print(c)



# Q7. A company has recorded the following product prices:
# 100, 180, 250, 320, 400
# Create a NumPy array.
# Find which prices are:
# 1. Greater than 150 AND less than 350.
# Use vectorized operations.
# Do NOT use a loop.
# Print the Boolean result.
a = np.array([100, 180, 250, 320, 400])
b =( a > 150 ) & ( a <350 )
print(b)

#------------------------------------------------------------------>topic_3 ------------> Indexing , Slicing,and masking
# Q1. Create a NumPy array containing:
# 10, 20, 30, 40, 50
# Using indexing:
# 1. Print the first element.
# 2. Print the last element.
# 3. Print the third element.
# Do NOT use a loop.
a = np.array([10, 20, 30, 40, 50])
print(a[0])
print(a[-1])
print(a[2])



# Q2. Create a NumPy array containing:
# 10, 20, 30, 40, 50, 60, 70
# Using slicing:
# 1. Print the first 3 elements.
# 2. Print the elements from index 2 up to index 5.
# 3. Print the last 3 elements.
# Do NOT use a loop.
a = np.array([ 10, 20, 30, 40, 50, 60, 70])
print(a[0:3])
print(a[2:5])
print(a[-3:])



# Q3. Create a NumPy array containing:
# 10, 20, 30, 40, 50, 60, 70, 80
# Using slicing:
# 1. Print every second element.
# 2. Print the array in reverse order.
# 3. Print every second element starting from the end.
# Do NOT use a loop.
a = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print(a[::2])
print(a[::-1])
print(a[::-2])




# Q4. Create a NumPy array containing:
# 10, 20, 30, 40, 50, 60, 70, 80, 90
# Using slicing:
# 1. Extract the last 5 elements.
# 2. Extract the elements from the 3rd-last position
#   up to the last element.
# 3. Reverse only the last 5 elements.
# Do NOT use a loop.
a = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
print(a[4::])
print(a[:-3])
print(a[-5:][::-1])




# Q5. Create the following 2D NumPy array:
# [[10, 20, 30],
#  [40, 50, 60],
#  [70, 80, 90]]
# Using indexing:
# 1. Print the value 50.
# 2. Print the complete second row.
# 3. Print the complete third column.
# Do NOT use a loop.
a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
               ])
print(a[1,1])
print(a [1])
print(a[:, 2])




# Q6. Create this 3x4 NumPy array:
# [[10, 20, 30, 40],
#  [50, 60, 70, 80],
#  [90, 100, 110, 120]]
# Using 2D slicing:
# 1. Extract the first two rows.
# 2. Extract the last two columns.
# 3. Extract the middle 2x2 section:
#    [[60, 70],
#[100, 110]]
# Do NOT use a loop.
a = np.array(
  [[10, 20, 30, 40],
  [50, 60, 70, 80],
  [90, 100, 110, 120]]
)
print(a[:2])
print(a[:,2:])
print(a[1:3,1:3])




# Q7. Create a NumPy array containing:
# 10, 25, 40, 15, 60, 30, 80
# Use Boolean Masking to extract only the values
# that are greater than 30.
# Print the filtered values.
# Do NOT use a loop.
a = np.array([10, 25, 40, 15, 60, 30, 80])
b = a >30 
print(a[b])


# Q8. Create a NumPy array containing:
# 10, 20, 30, 40, 50
# Find all values greater than 25.
# Increase ONLY those values by 10 using Boolean Masking.
# Print the final array.
# Do NOT use a loop.
a = np.array ([10, 20, 30, 40, 50])
b = a>25
c=(a[b])
print(c+10)


#q9. A company has recorded the following sales:
# Sales data
sales = np.array([120, 250, 180, 320, 90, 400])
# Increase the sales values by 20 ONLY where sales are
# greater than 200 AND less than 400.
# Do NOT use a loop.
# Print the final array.
a = (sales > 200) & (sales<400)
b = sales[a] * 1.20
print(b)

#--------------------------------------------------------------------------->Topic 5 — Broadcasting Rules



prices = np.array([100, 200, 300, 400])
# Har price mein 50 add karo.
# NumPy broadcasting use karo.
# Loop use nahi karna.
print(prices+5)



prices = np.array([100, 200, 300, 400])
discount = np.array([10, 20, 30, 40])
# Subtract the corresponding discount from each price.
# Do NOT use a loop.
print(prices-discount)



import numpy as np

sales = np.array([
    [100, 200, 300],
    [150, 250, 350]
])

bonus = np.array([
    [10],
    [20]
])

# Add the corresponding bonus to every value in each row.
# Use NumPy broadcasting.
# Do NOT use a loop.

# Write your code below:


updated = sales+bonus 
print(updated)

#---------------------------------------------------------------------------->Topic 6 — Reshaping Arrays


# Create an array containing numbers 1 to 12.
# Reshape it into 3 rows and 4 columns.
# Print the reshaped array.

a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(a.reshape(3,4))





# Create an array containing 12 monthly sales values.

# Reshape it into 4 rows and 3 columns.
# Each row represents a quarter.
#
# Print the reshaped array.
# Then find the total sales of ALL 12 months.

# Write your code below:

a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(a.reshape(4,3))
print(a.sum())





import numpy as np

sales = np.array([
    [100, 200, 300],
    [150, 250, 350],
    [120, 220, 320]
])

# Each row represents a month.
# Each column represents a product.
#
# Find the total sales for EACH product.
# Use axis.
#
# Write your code below:


print(sales.sum(axis=0))










import numpy as np

sales = np.array([
    [100, 200, 300],
    [150, 250, 350],
    [120, 220, 320]
])

# Each row = one month
# Find the AVERAGE sales for each month.
# Use axis.
#
# Write your code below:

print(sales.mean(axis=1))










sales = np.array([
    [100, 200, 300],
    [150, 250, 350],
    [120, 220, 320]
])

# Each row = one month
# Find the HIGHEST single product sale in each month.
# Use max() and axis.
#
# Write your code below:

print(sales.max(axis=1))











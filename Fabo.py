# Fibonacci_numbers
 
n = int(input("Enter the number of Fibonacci terms you want: "))
a = 0
b = 1
print("The first", n, "Fibonacci numbers are:")

for i in range(n):
    print(a, end=" ")
    next_number = a + b
    a = b
    b = next_number

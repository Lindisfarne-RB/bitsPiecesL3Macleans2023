def reversed_string(text):
    result = ""
    index = len(text) - 1
    while index >= 0:
        result += text[index]
        index -= 1
    return result


print("=============REVERSE A STRING===========")
s = input("Enter a string")
s = reversed_string(s)
print(s)


print("-----------------------REVERSAL WITH RECURSION---------------")

def reversed_string(text):
    if len(text) == 1:
        return text
    return reversed_string(text[1:]) + text[:1]   #using slice here


print(reversed_string("Hello, World!"))

print("--------------------------------------------------")

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 5  #hard code

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))
   
   
   
   
for i in range (1,5):
    for j in range(1,i):
        print(j, end="")
    print("\n")
        
        
rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")
    
    
    
rows = int(input("Enter number of rows: "))

ascii_value = 65

for i in range(rows):
    for j in range(i+1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
    
    ascii_value += 1
    print("\n")
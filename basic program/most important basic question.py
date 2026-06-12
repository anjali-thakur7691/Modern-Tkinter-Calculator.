# # 1. REVERSE NUMBER

# num = "12345"
# # rev = 0
# # while num > 0:
# #     last_digit = num % 10
# #     rev = (rev * 10) + last_digit
# #     num = num // 10
# #     print("Reversed:", rev)

# reversed_number = num[::-1]

# print("original:", num)
# print("Reversed:", reversed_number) 

# SUM OF DIGITS

# num = 12345
# sum_digit = 0
# while num > 0:
#     digit = num % 10
#     sum_digit += digit
#     num = num // 10
# print("sum of digit:", sum_digit)

# PALINDROME NUMBER

# Taking input from the user
# num = input("Enter a number: ")

# # Reversing the string
# reverse_num = num[::-1]

# # Comparing original and reversed
# if num == reverse_num:
#     print(f"{num} is a Palindrome.")
# else:
#     print(f"{num} is not a Palindrome.")


# यूजर से इनपुट लें
# n = int(input("संख्या दर्ज करें: "))

# # नंबर की एक कॉपी 'temp' में सुरक्षित रखें
# temp = n 
# reverse = 0

# while n > 0:
#     digit = n % 10             # आखिरी अंक निकालें
#     reverse = reverse * 10 + digit  # उसे उल्टा (reverse) करें
#     n = n // 10                # नंबर से आखिरी अंक हटा दें

# # अब 'temp' (ओरिजिनल) और 'reverse' की तुलना करें
# if temp == reverse:
#     print(f"{temp} एक Palindrome संख्या है।")
# else:
#     print(f"{temp} Palindrome नहीं है।")


# LARGEST NUMBER OF LIST
# Max () function se

# numbers = [10,25,7,39,45,50]
# largest = max(numbers)
# print("largest numbers is:", largest)

# Loop ka use karke

# numbers = [10,5,15,25,50,90,70]
# largest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num
# print("largest numbers is:", largest)

# EVEN OR ODD
# num = 8
# if num % 2 == 0:
#     print(num, " is an even number")
# else:
#     print(num, " is an odd number")

#FECTORIAL OF NUMBER [Ex. 5! = 5x4x3x2x1 = 120]
# Loop se fectorial nikalna

# num = 5
# fact = 1
# for i in range(1, num + 1):
#     fact = fact * i
# print("Factorial is:", fact)

# Function bnakar
# num = 5
# fact = 1

# def factorial(num):
#     fact = 1
#     for i in range(1, num + 1):
#         fact *= i
#     return fact
# print(factorial(5))

# RECURSION SE FACTORIAL

# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)
#     print(factorial(5))
    
#PRIME NUMBER CHECK
# Loop ke sath
#num = 9
# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print("not prime")
#             break
#     else:
#         print("prime number")
# else:
#     print("not prime")

# user input ke sath

# num = int(input("Enter number: "))
# if num > 1:
#      for i in range(2, num):
#           if num % i == 0:
#            print("not prime")
#           break
#      else:
#        print("prime number")
# else:
#     print("not prime")
#     
#   count digits
# string Methord
#num = 12345
# count = len(str(num))
# print("Total digits:", count)

# loop methord se
# num = 123546
# count = 0

# while num > 0:
#     num = num // 10
#     count += 1
# print("Total digits:", count)

# FIBONACCI SERIES RULES ( fibonacci series me har next number pichle number ka sum hota hai)

# LOOP SE 
# n = 10
# a, b = 0, 1
# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

# REMOVE DUPLICATE FORM LIST

# SET KA EXAMPLE (SET JO HAI DUPLICATE KO HTA DETA HAI)

# my_list = [1,2,3,3,4,5,6,7]
# new_list = list(set(my_list))
# print(new_list)

# LOOP SE 
# my_list = [1, 2, 2, 3, 4, 4, 5]

# new_list = []
# for num in my_list:
#     if num not in new_list:
#         new_list.append(num)

# print(new_list)

# TABALE OF A NUMBER
# num = 5

# for i in range(1, 11):
#     print(num, "x", i, "=", num * i )

# sum of N numbers S = n + 1/ 2 methord se
# n = 5
# sum = n * (n + 1) // 2
# print("sum", sum)
# Loop se 
# n = 5
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print("sum =", sum)
# ARMSTRONG NUMBER
# num = int(input("enter number: "))
# order = len(str(num))
# sum = 0
# temp = num
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** order
#     temp //= 10
# if sum == num:
#     print("armstrong number")
# else:
#     print(" not armstrong number")

# REVERS STRING
# text = input("enter string: " )
# reverse = text[::-1]
# print("enter string:", reverse)
 
# COUNT VOWELS IN STRING
# text = input("Enter string: ")

# vowels = "aeiouAEIOU"
# result = ""
# for ch in text:
#     if ch in vowels:
#         result += ch
# print("vowels:", result)

         
    
    






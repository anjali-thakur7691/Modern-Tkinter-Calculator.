# num = 7
# i = 2
# is_prime = True

# while i < num:
#     if num % i ==0:
#         is_prime = False
#         break
#     i = i + 1
# if num > 1 and is_prime:
#     print("prime number")
# else:
#     print("not prime")

# count Frequency of all elements

a = [1,2,3,4,8,9,6,4,8,2,3,2]
i = 0
seen = []
while i < len(a):
    if a[i] not in seen:
        print(a[i] , "->", a.count(a[i]))
        seen.append(a[i])
    i = i + 1
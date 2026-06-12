# Pattern Programming ek aisi practice hai jisme hum programming
#  language (jaise Python) ka use karke different designs / patterns print karte hain —
#  jaise stars (*), numbers, ya characters se bane shapes.


# 1. Square Hollow Pattern 
# 👉 Condition TRUE → star ⭐
# Condition FALSE → space ⬜
# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# # 2. Number Triangular
# n=4
# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end=" ")
#     print()

#  3. Number Increasing Pyramid
# n=4
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

#  4. Number Increasing Reverse Pyramid
# n=4
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

#  5. Number Changing Pyramid
# n=4
# num=1
# for i in range(1,n+1):
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
#     print()

#  6. Zero-One Triangle
# n=4
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print((i+j)%2,end=" ")
#     print()

#  7. Palindrome Triangle
# n=4
# for i in range(1,n+1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     for j in range(2,i+1):
#         print(j,end=" ")
#     print()

# 🔷 8. Rhombus Pattern
# n=5
# for i in range(n):
#     print(" "*(n-i-1)+"* "*n)

# 🔷 9. Diamond Pattern
# n=4
# for i in range(1,n+1):
#     print(" "*(n-i)+"* "*i)
# for i in range(n-1,0,-1):
#     print(" "*(n-i)+"* "*i)

# 🔷 10. Butterfly Pattern
# n=4
# for i in range(1,n+1):
#     print("* "*i+" "*(2*(n-i))+"* "*i)
# for i in range(n,0,-1):
#     print("* "*i+" "*(2*(n-i))+"* "*i)

# 🔷 11. Square Fill Pattern
# n=5
# for i in range(n):
#     print("* "*n)

# 🔷 12. Right Half Pyramid
# n=5
# for i in range(1,n+1):
#     print("* "*i)

# 🔷 13. Reverse Right Half Pyramid
# n=5
# for i in range(n,0,-1):
#     print("* "*i)

# 🔷 14. Left Half Pyramid
# n=5
# for i in range(1,n+1):
#     print(" "*(n-i)+"* "*i)

# 🔷 15. Reverse Left Half Pyramid
# n=5
# for i in range(n,0,-1):
#     print(" "*(n-i)+"* "*i)

# 🔷 16. K Pattern
# n=5
# for i in range(n,0,-1):
#     print("* "*i)
# for i in range(2,n+1):
#     print("* "*i)

# 🔷 17. Triangle Star Pattern
# n=5
# for i in range(1,n+1):
#     print("* "*i)

# 🔷 18. Reverse Number Triangle
# n=4
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# 🔷 19. Mirror Image Triangle
# n=4
# for i in range(1,n+1):
#     print(" "*(n-i)+"* "*i)

# 🔷 20. Hollow Triangle
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if j==1 or j==i or i==n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# 🔷 21. Hollow Reverse Triangle
# n=5
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         if j==1 or j==i or i==n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# 🔷 22. Hollow Diamond
# n=4
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if j==1 or j==i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# for i in range(n-1,0,-1):
#     for j in range(1,i+1):
#         if j==1 or j==i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# 🔷 23. Hollow Hourglass
# n=5
# for i in range(n,0,-1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         if j==1 or j==i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# for i in range(2,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         if j==1 or j==i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# 🔷 24. Pascal Triangle
# n=5
# for i in range(n):
#     num=1
#     for j in range(i+1):
#         print(num,end=" ")
#         num=num*(i-j)//(j+1)
#     print()
# # 25. Right Pascal Triangle
# n=5
# for i in range(1,n+1):
#     print("* "*i)
# for i in range(n-1,0,-1):
#     print("* "*i)

# Alternate alphabate pattern
# n = 5
# for i in rang e(n):
#     for j in range(i + 1):
#         printn = 5 
# (chr(65 + (j % 2)), end=" ")
#     print()

# n = 5
# for i in range(5):
#     for j in range(3):
#         print(" * ", end= " ")
#     print()

# rows = 5 
# for i in range(rows , 0, -1):
#     for j in range(rows - i):
#         print(" ", end=" ")
#     for k in range(i, i+1):
#         print("*", end="")
#     else:
#         print("  ", end=" ")
# print() 

# n = 5
# for i in range(1,n+1):
#     print("  "  * (n-i) + "*"  * i)

# n = 5
# for i in range(n, n + 1):
#     print("  " * (n-1) + "*" * i)

# rows = 5

# for i in range(rows):
#     for j in range(rows - i - 1):
#         print("  ", end="")
#     for k in range(rows):
#         print("*",end=" ")

#     print() 
# hollow rhombus pattern   
# rows = 5 

# for i in range(rows):
#     for j in range(rows - i - 1):
#         print(" ",end="")
#     for k in range(rows):
#         if i == 0 or i == rows - 1 or k == 0 or k == rows - 1:
#             print("* ", end="")
#         else:
#             print("  ",end="")
#     print()

# Dimond pattern

# rows = 5
# for i in frange(1, rows + 1):
#     for j in range(rows-i):
#         print("  ", end="")
#     for k in range(2*i-1):
#         print("* ",end="")
#     print()
# # lower pyramid

# for i in range(rows - 1, 0, -1):
#     for j in range(rows - i):
#         print("  ", end="")
#     for k in range(2 * i - 1):
#         print("* ", end="")
#     print()

# rows = 5

# for i in range(rows - 1, 0, -1):
#     for j in range(rows - i):
#         print("  ", end="")
#     for k in range(2 * i - 1):
#         print("* ", end="")
#     print()

# for i in range(1, rows):
#     for j in range(rows-i):
#         print("  ", end="")
#     for k in range(2*i-1):
#         print("* ",end="")
#     print()

rows = 5

# for i in range(rows):
#     for j in range(rows-i-1):
#         print("  ",end="  ")
#     num = 1
#     for k in range(i+1):
#         print(num,end="  ")
#         num = num *(i-k)//(k+1)
#     print()

# for i in range(rows):
#     for j in range(rows-i-1):
#         print("  ",end="")
#     num = 1
#     for k in range(i+1):
#         print(num,end="  ")
#         num = num *(i-k)//(k+1)
#     print()

# Paskal triangal
# num = num * (i -k) // (k + 1)

# rows = 5
# for i in range(rows):
#     for j in range(rows - i - 1):
#         print("  ", end="")
#     num = 1
#     for k in range(i + 1):
#         print(num,end="  ")
#         num = num * (i -k) // (k + 1)
#     print()

# Buterfly tryangal
# rows = 4
# # upper part
# for i in range(1, rows+1):
# # left stars
#     for j in range(i):
#         print("* ", end="")
# # midil space
#     for k in range(2*(rows-i)):
#         print("  ",end="")
# # right stars
#     for i in range(i):
#         print("* ", end="")
#     print()
# #lower part
# for i in range(rows-1,0,-1):
# # left stars
#     for j in range(i):
#         print("* ", end="")
# # midil space
#     for k in range(2*(rows-i)):
#         print("  ",end="")
# # right stars
#     for i in range(i):
#         print("* ", end="")
#     print()
# K pattern
rows = 5
#upper part
# for i in range(rows,0,-1):
#     for j in range(i):
#         print("* ",end="")
#     print()
# lower part
# for i in range(2,rows+1):
#     for j in range(i):
#         print("* ",end="")
#     print()

# rows = 7 
# mid = rows // 2
# for i in range(rows):
#     for j in range(rows):
#         if j == 0 or i + j == mid or i - j == mid:
#             print("*",end=' ')
#         else:
#             print(" ",end=" ")
    # print()

# rows = 4
# for i in range(1, rows +1):
#     for j in range(rows - i):
#         print("  ",end="")
#     for k in range(1, i + 1):
#         print(k,end=" ")
#     for k in range(i -1,0,-1):
#         print(k,end=" ")
#     print()

# rows = 6
# for i in range(rows, 0, -1):
#     for j in range(rows, i+1):
#         print(" ",end="")
#     for k in range(i):
#         print("* ",end="")
#     print()
# Alfabatic pattern
# for i in range(5):
#     for j in range(i + 1):
#         print(chr(65 + i),end=" ")
#     print()

# for i in range(5):
#     for j in range(5 - i):
#         print(chr(65 + i),end=" ")
#     print()

# for i in range(5):
#     for j in range(5 - i):
#         print(chr(65 + j),end=" ")
#     print()

# for i in range(5):
#     for j in range(i + i + 1):
#         print(chr(65+j),end=" ")
#     print()

# for i in range(5):
#     for j in range(i + 1):
#         print(chr(65+j + i),end=" ")
#     print()
# ch = 65

# for i in range(7):
#     for j in range(i + 1):
#         if ch <= 90:
#             print(chr(ch), end=" ")
#             ch = ch + 1
#         else:
#             print(" ", end=" ")
#     print()

# ch = 65
# cs = 65

# for i in range(7):
#     for j in range(i + 1):
#         if ch <= 90:
#             print(chr(ch), end=" ")
#             ch = ch + 1
#         else:
#             print(chr(cs), end=" ")
#             cs = cs + 1
#     print()

# for i in range(5):
#     ch = 65
#     for j in range(i + 1):
#         print(chr(ch), end=" ")
#         ch = 2 + ch
#     print()

# for i in range(5):
#     ch = 65
#     for j in range(i + 1):

#        if ch == 69:
#           print(chr(101), end=" "  )
#        else:
#         print(chr(ch), end=" ")
#         ch = ch + 2
#     print()

# Alphabet pattern

# n = 5

# for i in range(n):
#     for j in range(n - i - 1):
#         print(" ", end= " ")
#     for k in range(i + 1):
#         print(chr(65+k),end=" ")
#     print()

# n = 5 
# for i in range(n,0,-1):
#     for j in range(n - i):
#         print(" ",end=" ")
#     for k in range(i):
#         print(chr(65 + k),end=" ")
#     print()

# n = 5 
# for i in range(n):

#     for j in range(n -i - 1):
#         print(" ",end=" ")
#     for k in range(i + 1):
#         print(chr(65 + k),end=" ")
#     for l in range(i - 1,-1,-1):
#         print(chr(65+i),end=" ")
#     print()


# n = 5 
# for i in range(n):

#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(n - i):
#         print(chr(65 + k),end=" ")
#     for l in range(n-i - 2,-1,-1):
#         print(chr(65+l),end=" ")
#     print()

# dimond alphabetic pattern
# n = 4
# for i in range(n):

#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for k in range(i+1):
#         print(chr(65 + k),end=" ")
#     for l in range(i-1,-1,-1):
#         print(chr(65+l),end=" ")
#     print()

# for i in range(1,n):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(n-i):
#         print(chr(65 +  k),end=" ")
#     for l in range(n -i-2,-1,-1):
#         print(chr(65+l),end=" ")
#     print()

n = 5
# for i in range(n):
#     for j in range(n):
#         print("",end="")
#     for k in range(n):
#         print(chr(65+k), end=" ")

#     print()
for i in range(1, n-1):
    for j in range(i):
        print("",end="")
    for k in range(i):
        print(chr(65+k), end=" ")

    print()
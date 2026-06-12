# MAP
# har element pr same function apply krta hai

# names = ["java","python","code","js"]
# result = map(str.upper,names)
# print(list(result))

# squares of a numbers

# nums = [1,2,3,4]
# result = map(lambda x : x * x , nums)
# print(list(result))

# syntax :
# filter(function, iterable)
# Even number nikalna hai

# nums = [1,2,3,4,5,6,7,8]
# result = filter(lambda x : x % 2 == 0 , nums)
# print(list(result))

# name with length > 5 
# names = ["ram", "mohan", "rahul", "anjali", "python"]
# result = filter(lambda x : len(x) > 5 , names)

# print(list(result))

# syntax
# reduce(function,iterable)

# from functools import reduce
# nums = [1,2,3,4,5,6]

# result = reduce(lambda a,b : a*b, nums)
# print(result)

# ZIP ()
# 2 ya zyada iterable ka pair bna deta hai

# names = ["anjali","thakur"]
# marks = [90,80]
# result = zip(names,marks)
# print(list(result))

# TRy
# try - except (jab hume lagta hai ki code me error aa sakta hai to hum us code ko try block me likhte hai taaki program creash na ho)

# try :
#     print(10/0)
# except:
#     print("Error Handling")

# else with try

# try:
#     print(10/4)
# except:
#     print("Error")
# else:
#     print("success")

# Finally with try
# try:
#     print(10/0)
# except:
#     print("Error")
# finally:
#     print("Always Runs")

#raise custom error

# age = 15

# if age < 18:
#     raise Exception("Not Eligible")
numbers = [10,20,30,40,50]
print("Original List", numbers)
old_num  = int(input("kaun sa number htana hai:?"))
new_num = int(input("Kaun sa naya number jodna hai:?"))
if old_num in numbers:
    index = numbers.index(old_num)
    numbers[index] = new_num
    print("Updated List:", numbers)
else:
    print("Number list me nhi mila") 
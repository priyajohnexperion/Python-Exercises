#List comprehension
number_list = [10,20,30,40,50,60,70,80,90,100]
number_list[:] = [x for x in number_list if x <= 50]
print(number_list)

# Method 2: Reverse Iteration
number_list = [10,20,30,40,50,60,70,80,90,100]
for x in reversed(number_list):
    if x > 50:
        number_list.remove(x)
print(number_list)
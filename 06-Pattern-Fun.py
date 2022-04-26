row_count = 5
b = 0
for i in range(row_count, 0, -1): #outer loop
    b += 1
    for j in range(1, i + 1):  #nested loop
        print(b, end=' ')  #display number
    print('\r')  #print in new line
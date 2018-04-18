count = 0
for num in range(2,1001):
    for i in range(2,num):
        if (num%i==0):
            break
    else:
        print(num ,end=' ')
        count += 1
        if(count%8==0):
            print(end="\n")

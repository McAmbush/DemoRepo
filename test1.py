    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    li = [] 
    a = []
    for i in range(x):
        for j in range(y):
            for k in range (z):
                if i+j+k!=n:
                    li.append(i)
                    li.append(j)
                    li.append(k)
                    a[0][i] = li
     print(a)  

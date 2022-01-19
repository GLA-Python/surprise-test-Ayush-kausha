def function_expan(x):
    c=[]
    flag=1
    for i in range(1,len(x)):
        b=x[i]-x[i-1]
        c.append(abs(b))

    for j in range(1,len(c)):
        if c[j]<=c[j-1]:
            flag=0
            break


    if flag==0:
        return False
    elif flag==1:
        return True




a=input().split()
b=list(map(int,a))
print(function_expan(b))

def fibonacci(n):
    if n==1:
        return 0
    elif (n==2):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


num=int(input("Enter the number of terms you want in the series: \n"))
for i in range(1,num+1):
    print(fibonacci(i),end=" ")
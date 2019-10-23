def getNthFib(n): # input n=6 #Sample output: 5(0,1,1,2,3,5)
    if n==2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib(n-1)+getNthFib(n-2)

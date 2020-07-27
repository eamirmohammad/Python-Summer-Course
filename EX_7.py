#EX_7 tabe fib:

#part 1
def fib(x):
    if x<1 :
        print ('Wrong Input')
    elif x == 1 or x == 2:
        return 1
    else:
        return fib (x-1) + fib (x-2)
print ('part 1 is ready\n')

#part 2
def fiblist(arg):
    l_fib = [1 , 1]
    if arg < 0 :
        print ('Error')
    elif arg == 1 :
        return l_fib[:1]
    elif arg == 2 :
        return l_fib[:2]
    else:
        for i in range (2,arg):
            l_fib.append(l_fib[i-2]+l_fib[i-1])
    return l_fib
print ('part 2 is ready\n')
    

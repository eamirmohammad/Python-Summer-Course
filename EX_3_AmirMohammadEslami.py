#Identifying the leap years (Amir Mohammad Eslami) :
year = None
year = int(input("What year? "))

if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
           print('leap Year')
        else:
            print('Not leap Year')

    else:
        print('leap Year')
else:
    print('Not leap Year')


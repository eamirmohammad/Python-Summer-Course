#EX_6 Amir Mohammad Eslami

print ('Question 45:\n') #question 45

Total = 0
while Total < 50:
    num = int(input('ENTER A NUMBER: '))
    Total += num
    print ('the Total is ', Total)
print ('Total is greater than 50. All done!\n')


print ('Question 46:\n') #question 46
num = None
num = int(input('Enter one number: '))
while num < 5:
    num = int(input('Enter another number: '))
print ('The last number you entered was a ', num)
print ('Question 46 is Done!')

print ('Question 47:\n') #question 47

num1 = int(input('Enter one number: '))
num2 = int(input('Enter second number: '))
Total = num1 + num2
print (Total, '\n')
ans = input('Do you want to add another number?\n(If the answer is yes type y) ')
while ans == 'y':
    num3 = int(input('Enter an other number: '))
    Total += num3
    ans = input('Do you want to add another number?\n(If the answer is yes type y) ')
print ('The total sum is : ', Total)
print ('Question 47 is Done!\n')

print ('Question 48:\n') #question 48

count = 0
ans = input('Who do you want to invite? ')
print (ans, 'has been invited.\n')
count += 1
ans2 = input ('Do you want to invite another one? (if the ans is yes, print yes)')
ans2 = ans2.lower()
while ans2 == 'yes':
    ans = input('Who do you want to invite else? ')
    print (ans, 'has been invited.\n')
    count += 1
    ans2 = input ('Do you want to invite another one? (if the ans is yes, print yes)')
print (count, 'people has been invited')
print ('Question 48 is Done!\n')

print ('Question 49:\n') #question 49

compnum = 50
count = 0
print ('Guess the number!')
ans = int(input('Enter your first guess: '))
count += 1
while ans != compnum:
    if ans > 50:
        print ('Too high')
    else:
        print ('Too low')
    ans = int(input('Make another guess: '))
    count += 1
print ('Well done, you took ', count, ' attempts')
print ('Question 49 is Done!\n')
      
print ('Question 50:\n') #question 50

num = int(input('Enter a number between 10 and 20: '))
while num <= 9 or num >= 20:
    if num >= 20:
        print ('too high')
    else:
        print ('too low')
    num = int(input('Try again, Enter a number between 10 and 20: '))
print ('Thank you!')
print ('Question 50 is Done!\n')

print ('Question 51:\n') #question 51
num = 10
while num != 1:
    print ('There are ', num,' green bottles hanging on the wall,\n',num, 'green  bottles on the wall, and if 1 green bottle should accidentally fall...')
    num -= 1
    ans = int(input('How many green bottles will be hanging on the wall? '))
    while ans != num:
        ans = int(input('No try again: '))
        
print ('There are ', num,' green bottles hanging on the wall,\n',num, 'green  bottles on the wall, and if 1 green bottle should accidentally fall...\n')
print ('There is no more green bottles hanging on the wall')
    

    
    
    

    

















    










    

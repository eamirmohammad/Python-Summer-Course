# EX_4 Amir Mohammad Eslami

print('Question 12:') #Qestion 12
num1 = None
num2 = None

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

if num1 > num2:
    print ('First number is greater than the second')
    print ('Second number:', num2)
    print ('First number:', num1)
else:
    print ('Second number is greater than the First')
    print ('First number:', num1)
    print ('Second number:', num2)

print ('Q12 is done.')

print ('\nQestion 13:') #Qestion 13

num3 = None
num3 = int(input('Enter one number less than 20: '))
if num3 < 20:
    print ('All done, Thanks!')
else:
    print ('Too High!, try again!')
print ('Q13 is done.')

print ('\nQestion 14:') #Qestion 14

num4 = None
num4 = int(input('Enter one number between 10 than 20(inclusive): '))
if 10 < num4 < 21:
    print ('Correct, Thanks!')
else:
    print ('Wrong Answer, try again!')
print ('Q14 is done.')

print ('\nQestion 15:') #Qestion 15

str1 = None
str1 = input('Enter your favorit color: ')

if str1 == 'Red' or str1 == 'red' or str1 == 'RED':
    print ('I like red too!')
else:
    print ('I don not like ', str1, ',I prefer red.')

print ('Q15 is done.')

print ('\nQestion 16:') #Qestion 16

str2 = None
str3 = None
str2 = input('Is it raining out there?\n ')
str2 = str2.lower()
if str2 == 'yes':
    str3 = input('Is it windy?\n ')
    str3 = str3.lower()
    if str3 == 'yes':
        print ('It is too windy for an umbrella.\n')
    else:
        print ('Take an umbrella.\n')
else:
    print('Enjoy your day!')
print ('Q16 is done.')

print ('\nQestion 17:') #Qestion 17
age = None
age = int(input('How old are you?'))
if (age >= 18):
    print ('You can vote!')
elif ( age == 17):
    print ('You can learn to drive a car')
elif ( age ==16):
    print ('You can buy a lottery ticket')
else:
    print ('You can go trick. or-Treating')
print ('Q17 is done.')

print ('\nQestion 18:') #Qestion 18
num5 = None
num5 = int(input('Enter a number: '))
if num5 < 10:
    print ('Too low!')
elif 10 <= num5 <20:
    print ('Correct.')
else:
    print ('Too high!')
print ('Q18 is done.')

print ('\nQestion 19:') #Qestion 19
num6 = None
num6 = int(input('Enter 1,or 2, or 3: '))
if num6 ==1:
    print ('Thank you.\n')
elif num6 == 2:
    print ('Well done\n')
elif num6 == 3:
    print ('Correct\n')
else:
    print ('Error! try some time else.\n')

print ('Q19 is done.')
    










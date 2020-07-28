# EX_5 Amir Mohammad Eslami

print ('Question 69:') #question 69
t1 = ('Iran', 'Iraq', 'Afghanistan', 'UAE', 'Turkey')
print (t1)
str1 = None
str1 = input('Which country do you choose?\n  ')
index = None
index = t1.index(str1)
print (index)
print ('Q69 is Done.\n')

print ('Question 70:') #question 70
index2 = None
index2 = int(input('choosa an index from 0 to 4'))
print (t1[index2])
print ('Q70 is Done.\n')

print ('Question 71:') #question 71
l_sport = ['volleyball', 'basketball']
sport = input('what is your favorite sport?\n ')
if sport != 'volleyball' and sport!= 'basketball':
    l_sport.append(sport)
l_sport.sort()
print (l_sport)
print ('Q71 is Done.\n')

print ('Question 72:') #question 72
l1 = ['cookie' , 'pizza' , 'pasta' , 'ghormeh' , 'sib', 'hotdog']
l2 =[]
ans = None
ans = input('which one do you not like? (if everything is good, type Done)')
while ans!='Done' :
    l2.append(ans)
    ans = input('What else? (if everything is good, type Done)')
for x in l1:
    for y in l2:
        if x==y:
            l1.remove(x)

print (l1)
print ('Q72 is Done.\n')

print ('Question 73:') #question 73
food = input ('Type four of your favorite foods with comma between them,\nthen press enter:  ')
l_food = food.split(',')
d_food = {}
for x in range(1,5):
    i = int(x)
    for y in l_food:
        d_food[i] = y
print (d_food)
rmv = input('which do you want to get rid of? enter the key number: ')
if len(rmv) > 1:  
    l_rmv = rmv.split(',')
else:
    l_rmv = list(rmv)
    
for i in range(0,len(l_rmv)):
    del d_food[int(l_rmv[i])]
print (d_food)
print ('Q73 is Done.\n')

print ('Question 74:') #question 74

color_l = ['purple', 'yellow', 'red, blue', 'black', 'white', 'pink', 'brown', 'gray', 'green']
print (color_l)
num1 = None
num2 = None
num1 = int(input('Between 0 to 4, where to start? '))
num2 = int(input('where do you want it to end between 5 to 9? '))
print (color_l[num1:num2])
print ('Q74 is Done.\n')

print ('Question 75:') #question 75

num_l = [235, 568, 154, 652]
for i in range(0,len(num_l)):
    print(num_l[i])
num3 = None
num3 = int(input('Enter a 3-digit number: '))
for j in range(0,len(num_l)):
    if num_l[j] == num3:
        ans = (num_l.index(num3))
    else:
        ans = 'That is not in the list'
print (ans)
print ('Q75 is Done.\n')


print ('Question 76:') #question 76 ,77

names = input ('who do you want to invite to the party? (use comma between names) ')
list_name = names.split(',')
name = None
name = input ('Do you want to add another one? (If they are enough, type No) ')
while name != 'No':
    list_name.append(name)
    name = input ('Anyone else? (If they are enough, type No) ')

print (list_name)
print ('number of people: ', len(list_name))
print ('Q76 is Done.\n')

print ('Question 77:') #question 77
print (list_name)
name = None
name = input('who is in your mind from the list? ')
print ('the position is: ', list_name.index(name))
ans = None
ans = input ('Do you want to invite him/her anyway? ')
ans.lower()
if ans == 'no' :
    list_name.remove(ans)
    print ('ok')
else:
    print ('Every thing is fine')
print (list_name)
print ('Q77 is Done.\n')

print ('Question 78:\n') #question 78

tv_list = ['Top Gear', 'BBC Earth', 'Cosmos' , 'Breaking Bad']
for i in tv_list:
    print (i)
new_prg = input('What program do you want to add? ')
new_prg_pl = int(input('Where do you want to put it? (form place 1 to 5) '))

tv_list.insert(new_prg_pl,new_prg)

print ('\n')
for l in tv_list:
    print (l)
print ('Q78 is Done.\n')
               
print ('Question 79:\n') #question 79

nums = []
for i in range (1,4):
    num = int(input('Enter a number: '))
    nums.append (num)
    print (nums)
ans = input ('Do you wan to keep he last number you entered? (Yes or No)')
ans = ans.lower()
while (ans != 'yes' and ans != 'no'  ): #or ans != 'no'
    
    ans = input ('Wrong answer, I ask again? (Yes or No)')
    ans = ans.lower()
if ans == 'no':
    del(nums[2])

print (nums)
print ('Q79 is Done.\n')   

        












# # 1.Selection statements
# # if, if-else, if-elif-else, if-elif 
# # 2. Iterative statements
# # for, while 
# # 3. Transfer statements 
# # break, continue

# # pass and del commands also there 

# # if 
# name=input('enter name:')
# if name.startswith('P'):
#     print('Good morning',name)

# # if-else
# name=input('enter name:')
# if name.startswith('a'):
#     print('Good morning',name)
# else:
#     print('Good morning , what can i help you',name)

# # if-elif-else
# name=input('Enter customer name:')
# if name.endswith('n'):
#     print('Hello, Good morning', name)
# elif name.startswith('p'):
#     print('Hello, Good evening', name)
# else:
#     print('Hello, sir',name)

# # if-elif
# role=input('Enter designation:')
# if role=='Manager':
#     print('Hello, Good morning sir')
# elif role=='HR':
#     print('Welcome to all new employees')

# # for
# i=input('enter a name:')
# for a in i:
#     print(a,sep='',end='')

# name=input('\nenter a name:')
# for a in name:
#     print(a,end='')

# # while 
# i=int(input('enter a number:'))
# while i<=10:
#     print(i)
#     i=i+1  

# # nested loops 
# num=int(input('enter a num:'))
# for i in range(num):
#     for j in range(i):
#         print(j)

# # transfer statements
# # break 
# # it will break the iteration and outside of the loop will executes
# for i in range(10):
#     if i==3:
#         print('Stop the process')
#         break
#     print(i)
# print('outside of the loop')

# list=[10,20,30,40,50]
# for item in list:
#     if item == 40:
#         print('select the number')
#         break
#     print('select items are:',item)
# print('don\'t select the item' )

# l=[1,2,3,4,5]
# for i in l:
#     if i==3:
#         print('stop the process if condition satisifies')
#         break
#     print('print statement executes until if condition satisfies')
# print('escape from the loop statement')

# # continue
# skip the current iteration and continue the next iteration 
# for i in range(10):
#     if i%2==0:
#         continue
    # print(i)

# l=[1,2,3,4,5,6,7,8,9]
# for item in l:
#     if item == 5:
#         print('select the items',item)
#         continue
#     print('items list',item)

# i = 1
# while i <= 10:
#     print(f"Hallo world {i} ")
#     i += 1

# user_input = int(input("enter a number : "  ))
# total = 0
# i = 1
# while i <= user_input:
#     total += i
#     print(i)
#     i += 1
# print(total)


# for i in range(1, 10):
#     print(f"hallo {i} world")


# total=0
# num=int(input("enter a number : " ))
# for i in range(1,num):
#     total += i
# print(total)


# total=0
# num=input("enter a number : " )
# for i in range(len(num)):
#     total += int(num[i])
# print(total)


# name=input(" enter your number  :  "  )
# var_name=""
# for i in range(len(name)):
#     if name[i] not in var_name:
#         print(f"{name[i]}  :  {name.count(name[i])}")
#         var_name += name[i]
   

# for i in range(1,10):
#     if i == 5:
#         continue
#     print(i)

# for i in range(1,10):
#     if i == 5:
#         break
#     print(i)


# import random

# guess_num=int(input("guess a number between 1 & 100 :  "))
# winning_num= random.randint(1, 100)
# guess =1
# game_over = False
# while not game_over:
#     if guess_num == winning_num:
#         print(f"You Winn, You guessed {guess} times")
#         game_over = True
#     else :
#         if guess_num < winning_num:
#             print("You guess Too low ")
#             guess += 1
#             guess_num = int(input("Guess again : "))
#         else:
#             print("You guess Too High ") 
#             guess += 1
#             guess_num = int(input("Guess again : "))
        

# num1=int(input("enter a number : "))
# num2=int(input("enter a number : "))


# def google(a,b):
#     return a+b
# total =google(a,b)
# print(total)

# def bigger(a,b,c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c
# big =bigger(num1,num2,num3)  


# num1 =int(input("enter 1st number : "))
# num2 =int(input("enter 2nd number : "))
# num3 =int(input("enter 3rd number : "))
# big =bigger(num1,num2,num3)  
# print(f"{big} is bigger")

# def big(a,b):
#     if a > b:
#         return a
#     return b

# def new_big(a,b,c):
#     old = big(a,b)
#     return big(old, c)
# print (new_big(100,20,60))


# def revers(word):
#     word_reverse = word[::-1]
#     if word ==word_reverse:
#         return True
#     return False

# word=input("enter your name : ")
# print(revers(word))

# def user_info(first_name, last_name="unknown", age=None):
#     print(f"your first name is {first_name}")
#     print(f"your last name is {last_name}")
#     print(f"your age is {age}")

# user_info("sanju")


# num = [1, 2, 'three', 'four', None]
# num[2] = 3
# num[4:]= ['five', 'six',2.2, True]
# print(num)


# frouts1 =['apple', 'mango']
# frouts2 =['orange','peach']
# frouts1.append('tomato')
# frouts2.insert(1, 'tomato')
# frouts1.extend(frouts2)
# fruits = frouts1 + frouts2
# print(fruits)
# print(frouts1)
# print(frouts2)

# frouts1 = ['apple', 'mango', 'banana', 'apple']
# frouts1.pop(1)
# frouts1.remove('apple')
# del frouts1[1]
# print(frouts1)
# if 'apple' in frouts1:
#     print ('apple is present')
# else:
#     print ('apple is not present')

# frouts1 = ['apple', 'mango', 'banana', 'apple']
# print(frouts1.count('apple'))
# print(frouts1)
# num = [5, 8, 3, 10, 1]
# num.sort()
# num.clear()
# num.reverse()
# frouts1.sort()
# print (sorted(num))
# print (num)
# f_1 = frouts1.copy()
# print(f_1)
# f1=input ("enter your name age domain").split()
# user_info='google com'.split()
# user, info='google com'.split()
# def u(a , b):
#     return a + " , " + b
# print(f"{user} \n{info}")
# print(f1)
# print(u(user, info))
# print (user)
# print (info)
# print(' '.join(user_info))

# nubmers = [[1,2,3],[4,5,6],[7,8,9]]
# nubmers = [1,2,3,4,5,6,7,8,9]
# print (nubmers)
# for sub in nubmers:
#     for i in sub:
#         print (i)
# print (nubmers[1][1])
# print (nubmers.index(5))

# def negitive_list(l):
#     negitive = []
#     for i in l:
#         negitive.append(-i)
#     return negitive

# nubmers = [1,2,3,4,5,6,7,8,9]

# print(negitive_list(nubmers))

# def squre_number(l):
#     squre =[]
#     for i in l:
#         squre.append(i**2)
        
#     return squre

# num = list(range(1,11))

# print (squre_number(num))
# print (type(num))
# def reverse(l):
#     return l[::-1]

# def rev(l):
#     l.reverse()
#     return l
# print(rev(num))


# def reverse_list(l):
#     r_list = []
#     for i in range(len(l)):
#         pop_list =l.pop()
#         r_list.append(pop_list)
#     return r_list

# print(reverse_list(num))

# def word_reverse(l):
#     words = []
#     for i in l:
#         words.append(i[::-1])
#     return words[::-1]
    

# word= ['abc','def','ghi','jkl','mno']
# print(word_reverse(word))
# word = 'abc', 'fhd'

# print(word[::-1])

# def odd_even(l):
#     odd = []
#     even = []
#     for i in l:
#         if i % 2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)
#     return (f'{odd} {even}')

# num = list(range(1,11))
# print (odd_even(num))

# def com_num(l1,l2):
#     common = []
#     for i in l1:
#         if i in l2:
#             common.append(i)
    
#     return common

# num1 = [1,2,5,7]
# num2 = [2,5,9,1,]
# print(com_num(num1,num2))

# def cnt(l):
#     count = 0
#     for i in l:
#         if type(i) == list:
#             count += 1
#     return count

# n = [1,2,3,[5,6,7],0]
# print(cnt(n))

# def cnt(l):
#     count = []
#     for i in l:
#         count.append(i)
#     return count

# n = [1,2,3,5,2,1,0]
# print(cnt(n))

# def cnt(l):
#     count = []
#     c = []
#     for i in l:
#         if i not in count:
#             count.append(i)
#         else:
#             c.append(i)
#     return c

# n = [1,2,3,5,2,1,0]
# print(cnt(n))


# google = ('sanju','subho','rintu')
# print(type(google))
# print(google)

# user = {'name' : 'sanju', 'age' : 25}
# print(user['name'])

# user1 =dict(name = 'rahul', age = 24)
# print(user1)

# user_info = {
#     'name' : 'google',
#     'age' : 24,
# }

# user_info = {
#     user : {
#         'name' : 'sanju',
#          'age' : 25},
    
# }

# print(user_info)

# user_info = {
#     'name' : 'sanju',
#     'age' : 24,
#     'class' : 12,
#     'subject' : 'commerce'
# }
# print(user_info)

# for i in user_info:
#     print (i)

# g=user_info.values()
# print(g)

# m = user_info.keys()
# print(m)

# for i in user_info.keys():
#     print (i)

# for i in user_info.values():
#     print (i)

# user_item = user_info.items()
# # print(user_item)

# for i in user_item:
#     print(i)

# for i, j in user_info.items():
#     print (f'{i} : {j}')

# print(f'I have to pay {bill:.2f}')
# print(user_info.popitem())
# print(user_info)
# print(user_info.pop('age'))
# print(user_info)
# user_info['roll'] = 25
# print(user_info)
# user_info = {
#     'name' : 'sanju',
#     'age' : 24,
#     'class' : 12,
#     'subject' : 'commerce'
# }

# more_info = {'roll' : 25, 'phone' : 1234, 'email' : '123@gmail.com'}
# user_info.update(more_info)
# # print(user_info)
# for i, j in user_info.items():
#     print(i ,'=', j)

# user_info1 = dict.fromkeys(['name','age','class'] ,'unknown')
# user_info.update(user_info1)
# print(user_info)
# g = user_info
# print(g)

# print(user_info.get('age'))
# search = input('enter your search:  ' )

# user_info = {
#     'name' : 'sanju',
#     'age' : 24,
#     'class' : 12,
#     'subject' : 'commerce'
# }

# def usr_get(l):
#     for i in l:
#         if user_info.get(search):
#             return ('present')
#         else:
#             return('not present')
# print(usr_get(user_info))

# print(user_info.get(search, 'not present !!!'))

# def counter(n):
#     count = {}
#     for i in range(1,n+1):
#         count[i] = i**3
#     return count
# search = int(input('enter a number : '))
# print(counter(search))

# search = input('enter your search : ')
# def word_count(s):
#     count = {}
#     for char in s:
#         count[char] = s.count(char)
#     return count
# print(word_count(search))

# goo = word_count(search)
# # print(goo)

# for i, j in goo.items():
#    print (f'{i} : {j}')

# user ={}
# name = input('enter your number : ')
# age = input('enter your age : ')
# roll = input('enter your roll : ')
# section = input('enter your section : ')

# user['name'] = name
# user['age'] = age
# user['roll'] = roll
# user['section'] = section
# print(user)
# for i, j in user.items():
#     print (f'{i} :  {j}')

 
# s ={1,2,3,4,5,4,3,5,1,6}
# # print(s)
# # s1 =s.copy()
# s.add(6)
# s.discard(8)
# s.remove(2)
# s.clear()
# print(s)

# l = [1,6,5,6,2,5,3,2,1,8,7]
# print(set(l))
# print(list(set(l)))

# s ={1,2,3,4}

# if 0 in s:
#     print('present')
# else:
#     print('not present')

# for i in s:
#     print (i)

# s1 ={3,4,5,6}

# print(s | s1)
# print(s & s1)

# num=list(range(1,11))
# def dual(l):
#     return([i**2 for i in l])

# print(dual(num))

# def equal(l):
#     return([i for i in l if i % 2 == 0])
# print(equal(num))

# friends =['sanju','subho','rintu','tukai']
# def names(l):
#     return [name[::-1] for name in l]
# print(names(friends))

# example =['sanju',10,1.5,True,False,5,'tukai']
# def ex(l):
#     # return[str(i) for i in l if (type(i) == int or type(i) == float)]
#     return[str(i) for i in l if (type(i) == str or type(i) == bool)]
# print(ex(example))

# nums =[1,2,3,4,5,6,7,8,9,10]

# def cnt(l):
#     return [i*2 if (i%2 == 0) else -i for i in l]

# new_num =[i*2 if (i%2 == 0) else -i for i in nums]
# print(new_num)
# print(cnt(nums))
# num1 =[1,2,3]
# num= [[i for i in num1] for j in range(3)]

# num= [[i for i in range(1,4)] for j in range(3)]

# print(num)

# num =[[1,2,3],[4,5,6],[7,8,9]]
# k = []
# def gg(l):
#     for i in l:
#         k.append(i)
#     return k

# print(gg(num))
# print (k)


# dicc = {num : num*2 for num in range(1,11)}
# print(dicc)

# name = 'google'
# word_count = {cher : name.count(cher) for cher in name}
# for i,j in word_count.items():
#     print (f'{i} : {j}')
# print(word_count)

# odd_even = {i : ('odd' if i%2 == 0 else 'even') for i in range(1,11)}
# print(odd_even)

# seet= {i**2 for i in range(1,6)}
# print(seet)
# name = ['sanju','tikai','hulo']
# frd ={i[0] for i in name}
# print(frd)

# def total(*args):
#     t = 0
#     for i in args:
#         t += i
#     return t
# print(total(1,2,3,4))


# def to_total(*args):
#     t = 0
#     for i in args:
#         t += i
#     return t

# num =[1,2,3,4]
# print(to_total(*num))

# def two(*args):
#     return [i**2 for i in args]
# print(two(1,2,3,4))

# def too(num1,*args):
#     if args:
#         return [i**num1 for i in args]
#     else:
#         return "You did'n type anything"

# num1 = 3
# number =[1,2,3,4,5]
# print(too(num1,*number))

# print(too(3,))

# def fun(**kwargs):
#     print(kwargs)

# def fun(**kwargs):
#     for i, j in kwargs.items():
#         print (f'{i} : {j}')
# d = {'name' : 'sanju', 'age' : 25}
# fun(**d)
# fun(name = 'sanju ', age = 25)


# def fun(name,*agrs,last_name = 'unknown',**kwargs):
#     print(name)
#     print(agrs)
#     print(last_name)
#     print(kwargs)
#     print({i for i , j in kwargs.items()})
#     print({j for i , j in kwargs.items()})

# fun('sanju',1,2,3,4, a =1, b =2)


# name =['sanju' , 'subho' ]
# n = [i.title() for i in name]
# print (n)

# def fun(l,**kwargs):
#     if kwargs.get('reverse') == True:
#         return [i[::-1].title() for i in l]
#     else:
#         return [i.title() for i in l]
# name =['sanju' , 'subho' ]   
# print(fun(name))

# git = lambda a,b : a + b
# print(git(3,2))

# # git1 = lambda n : n % 2 == 0
# git1 = lambda n : 'You are Right' if n% 2 == 0 else 'You are Wrong'
# print(git1(6))

# names =['sanju', 'tukai', 'subho']
# def find(l):
#     g = 0
#     for i in l:
#         print(f"{g} ------> {i}")
#         g += 1
# def find(l):
#     for i , j in enumerate(l):
#         print(f"{i} ------> {j}")
# find(names)

# def find(l,target):
#     for pov , name in enumerate(l):
#         if name == target:
#             return pov
#     return -1
# print(find(names,'sanju'))

# num = [1,2,3,4]
# def sq(l):
#     return l**2
# g = list(map(sq,num))
# print(g)
# new = [a**2 for a in num]
# print(new)

# e =list(map(lambda a:a**2, num))
# print (e)

# name =['abc','abcd','efg']
# # k = list(map(len,name))
# k = map(len,name)
# for i in k:
#     print(i)
# # print(k)

# def fil(a):
#     return a%2 == 0
# num = [1,2,3,4,5,6,7,8,9,10]
# # g = list(filter(fil,num))
# g = list(filter(lambda a:a%2 == 0,num))
# p = [i for i in num if i%2 == 0]
# print(p)
# print(g)

# num = [1,2,3,4]
# sqr = map(lambda a:a**2, num)

# new = iter(num)
# print(next(new))
# print(next(new))
# print(next(new))
# print(next(new))

# print(next(sqr))
# print(next(sqr))
# print(next(sqr))
# print(next(sqr))

# first_name = ['sanju','tukai','subho']
# middle_name = [123,12,123]
# last_name = ['parui','bhattacharjee','bhattachariya']

# g =zip(first_name,last_name,middle_name)
# g =zip(first_name,middle_name,last_name)
# k=(list(g))
# for i in k:
#     print(i)

# for i in k:
#     if 123 not in i:
#         print(i)

# l = [(1,2),(3,4),(5,6),(7,8)]
# print(list(zip(*l)))
# for i in zip(*l):
#     print(i)
# l1, l2 =list(zip(*l))
# print(list(l1))
# print(list(l2))
# total =[]
# for summ in zip(l1,l2):
#     total.append(sum(summ))
# print(total)

# l =[1,2,3],[4,5,6],[7,8,9]

# def avrage(*args):
#     avrages = []
#     for pair in zip(*args):
#         avrages.append(sum(pair)/len(pair))
#     return avrages
# print(avrage([1,2,3],[4,5,6],[7,8,9]))
# print(avrage(*l))

# avrage_finder = lambda *args:[sum(pair)/len(pair) for pair in zip(*args)]
# print(avrage_finder(*l))
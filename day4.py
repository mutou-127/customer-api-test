# def calc(a,b):
#     print(a+b)
#
#
# d=calc(10,2)
# print(d)
# def calc2(a,b):
#     s=a+b
#     return s
# print(calc2(1,2))
# c=calc2(1,2)
# print(c)

#

# def calc(a,b):
#     return a+b
# print(calc(10,20))
#
# s=lambda a,b:a+b
# print(s(10,20))
#
#
# lst=[10,20,30,40,50]
# for i in range(len(lst)):
#     a=lambda x:x[i]
#     print(a(lst))

# def fac(n):
#     if n==1:
#         return 1
#     else:
#        return n*fac(n-1)
#
# print(fac(6))

# def f(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return f(n-1)+f(n-2)
#
# print(f(9))
#
# for i in range(1,10):
#     print(f(i))
# import random
# def max(lst):
#     x=lst[0]
#     for i in range(len(lst)):
#         if lst[i]>x:
#             x=lst[i]
#     return x
# lst=[random.randint(1,100) for i in range(10) ]
# print(lst)
# print(max(lst))


# def change_lower_upper(x):
#     lst=[]
#     for i in x:
#         if 'A'<i<'Z':
#            lst.append( chr(ord(i)+32))
#         elif 'a'<=i<='z':
#             lst.append(chr(ord(i)-32))
#
#         else:
#             lst.append((i))
#     return ''.join(lst)
#
# s=input('write')
# s1=change_lower_upper(s)
# print(s1)


def get_find(s,lst):
    for i in lst:
        if s==i:
            return True
    return False
lst=['hello','worle','Abs']

r=get_find(input('write'),lst)
print('yes' if r else 'no')

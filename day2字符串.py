# s1='helLAowworld;'
# s2=s1.lower()
# print(s1,s2)
#
# #字符串分割
# email='sdlw@oqc.com'
# lst=email.split(sep='.')
# print (lst)
#
# print (s1.count('o'))
# print (s1.find('a'))
# #print (s1.index('a'))
#
# print (s1.startswith('o'))
# print (s1.endswith('world;'))

# s='Hellowworld'
# print(s.replace('o','1'))
#
#
# print(s.center(20,'1'))
#
# s='dl-hellowld'
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())
# print(s.strip())
#
# print(s.strip('he'))


#
# name='zhangsan'
# age=19
# score=99.9
# print('姓名：%s，年龄：%d，分数：%.1f'%(name,age,score))
#
# print(f'姓名：{name}，年龄：{age}，分数：{score}')
#
# print('姓名：{0}，年龄：{1}，分数：{2}'.format(name,age,score))
#
# s='Helloworld'
# print('{0:*^20}'.format(s))
#
# print('{0:,}'.format(12039.12123))
#
# a=123
# b=12
# print('{0:b}   {1:b}'.format(a,b))

# s='我爱你'
# s1=s.encode(errors='replace')
# print(s1)
# print(bytes.decode(s1))



# a='1231212'
# print(a.isdigit())
# s1='hello'
# s2='world'
# print(s1+s2)
#
# print(' '.join([s1,s2]))
#
#
# print(s1,s2)


# s='hekkoworldhekksowiisowks'
# s2=''
# for i in range(len(s)):
#     if s[i] not in s2:
#         s2+=s[i]
#
# print(s2)
#
#
# s3=set(s)
# print(s3)
# lst=list(s3)
# lst.sort(key=s.index)
# print(''.join(lst))



# a='\d+'
# s='3.333123I study python 3.11 every day'
# c=re.match(a,s)
# print(c)
# print(c.start())
# print(c.end())


# a='\d\.\d+'
# s='3.333123I study python 3.11 every day'
# c=re.findall(a,s)
# print(c)
import re

# a='黑客|破解|反爬'
# s='我想学习python 想破解什么是一个黑客的反扒的的是反爬'
# c=re.sub(a,'xx',s)
# print(c)
# print('-'*100)
#
# s2='http://www.dada.com/s?wd=sda'
# a='[?|:|/|]'
# lst=re.split(a,s2)
# print(lst)

#实战一  车牌归属地
#
# lst=['京A888','沪B666','浙A999']
# for i in lst:
#     a=i[0:1]
#     print(i,a)
#
# s='HelloPython,HelloJava,hlelophp'
# word=input('请输入要计算的字符：')
# print('{0}  sd {1}  chuxian {2}'.format(word,s,s.upper().count(word)))


# lst=[['01', 'dianfengshan','meidi',500],
#         ['02', 'weobolo','TCL',1000],
#         ['03', 'xijyi','boss',540]]
#
# for i in lst:
#     for j in i:
#             print(j,end='\t\t')
#     print()
#
# for i in lst:
#     i[0]='0000'+i[0]
#     i[3]='${0:.2f}'.format(i[3])
#
# for i in lst:
#     for j in i:
#             print(j,end='\t\t')
#     print()


import re









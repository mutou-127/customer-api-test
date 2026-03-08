

# print(A&B)
# print(A|B)
# print(A-B)
# print(B-A)
# print(A^B)
#
# A.add(11)
# print(A)
# A.remove(10)
# print(A)

# for i in A :
#     print(i)
#
# for a,b in enumerate(B,start=1):
#     print(a,b)
#
# s={i for i in range(1,10)}
# # print(s)
#
lst=[88,99,90,92,00,99]
# print(lst)
# for i in range(len(lst)):
#     if str(lst[i])!='0':
#         lst[i]='19'+str(lst[i])
#     else:
#         lst[i]='200'+str(lst[i])
#
# print(lst)

#
# for i,v in enumerate(lst):
#     if str(lst[i]) != '0':
#          lst[i]='19'+str(v)
#     else:
#         lst[i]='200'+str(v)
#
# print(lst)

# #京东购物流程
# lst=[]
# for i in range(5):
#     a=input('请输入商品编号入库：')
#     lst.append(a)
# for i in lst:
#     print(i)
# lst2=[]
# while True:
#     f=False
#     b=input('请输入您需要的商品')
#     for i in lst :
#         if b==i[0:4]:
#             lst2.append(i)
#             print('商品已入库')
#             f=True
#             break
#     if not f and b!='q':
#         print('商品不存在')
#     if b=='q':
#         break
#
# print('-'*50)
# print('gouwuh')
# lst2.reverse()
# print(lst2)
#
# d={'G156':['北京-天津', '18：06', '18：09','00：33'],
#    'G126':['北京-天津',' 18：15 ','18：49 ','00：34'],
#    'G892':['北京-河南',' 18：20 ','19：19 ','00：59']}
# for i in d:
#     print(i,end='   ')
#     for j in d[i]:
#         print(j,end='   ')
#     print()
# print(d['G156'])
#
# a=input('请输入你要选择的车次')
# b=input('请输入乘车人，若是多人乘车则用逗号分割')
# c=d.get(a,'Null')
# if c !='Null':
#     print(c[0],c[1])
#
# for i in d:
#     if a==i:
#         print('ninchengzuodechecishi ',d[i],'请',b,'快来')
#
s=set()
for i in range(1,6):
    a=input(f"请输入第{i}好友的手机号")
    s.add(a)
for i in s:
    print(i)

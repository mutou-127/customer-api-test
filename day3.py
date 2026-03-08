# # try:
# #     num1=int(input())
# #     num2=int(input())
# #     r=num1/num2
# # except ZeroDivisionError:
# #     print('error')
# # except ValueError:
# #     print("zifu")
# # else:
# #     print(r)
# # finally:
# #     print("fannial")
#
# try:
#     gender=input('1')
#     if gender!='男'and gender!='女':
#         raise Exception('性别只能是男或女')
#     else:
#         print(gender)
# except Exception as e:
#     print(e)


try:
    a=int(input('1'))
    b=int(input('1'))
    c=int(input('1'))
    if a+b>c and a+c>b and b+c>a:
        print('yes')
    else:
        raise Exception(a,b,c,'no')
except Exception as e:
    print(e)



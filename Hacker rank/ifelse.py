# x, y = map(float, input().split())
# if (x % 5 == 0 and y >= (x + .50)):
#     z = y - (x + 0.50)
#     print(z)
# else:
#     print(y)
################################################################################################
# Given a string, we'll say that the front is the first 3 chars of the string. ' \
# If the string length is less than 3,the front is whatever is there. Return a new string which is 3 copies of
# the front.
from numpy.matlib import randn


def front3(str):
    x = str[:3]
    print(x + x + x)


front3("java")
front3("vamshi")
################################################################################################
# str = 'code'
# print([:str+1])
######################################################################################################
# def string_match(a, b):
#     count = 0
#     for i in a,b:
#         if a[i] in b[i]:
#             count = count+1
#             print(count)
#
# string_match('xxcaazz', 'xxbaaz')

# for i in range(10):
#     print(i)

import date

current_date = date.print(current_date)

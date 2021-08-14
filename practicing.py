# # list1 = [15, 21, 32, 45, 21, 12, 16, 13]
# # # x = str(list1)
# # # print(x)
# #
# #
# # for i in list1:
# #     a = str(i)
# #     if a.endswith("2"):
# #         x = a.replace("2", "5")
# #         print("old number{}".format(i),"the number after replacing the digit is{}".format(x))
# # print(list1)
# # add a list of elements to a given set
# # sampleSet = {"Yellow", "Orange", "Black"}
# # sampleList = ["Blue", "Green", "Red"]
# #
# # sampleSet.update(sampleList)
# # print(sampleSet)
#
# # Return a set of identical items from a giventwoPythonset
# # set1 = {10, 20, 30, 40, 50}
# # set2 = {30, 40, 50, 60, 70}
# #
# #
# # print(set1.intersection(set2))
#
# #Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
# # f_name = "tom"
# # l_name = "cruise"
# #
# # print(f_name[::-1] ,l_name[::-1])
#
# # Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple
# # with those numbers
# # def sequence_numbers(*args):
# #     print(list(args))
# #     print(tuple(args))
# #
# # sequence_numbers(12,12,10,15,14,22,13)
# #
# #
#
# # Write a Python program to accept a filename from the user and print the extension of that
#
# # x = 'abc.java'
# # y= x.split('.')
# # print(y[-1])
#
# # Write a Python program to display the first and last colors from the following list. Go to the editor
# # color_list = ["Red","Green","White" ,"Black"]
# # color_list = ["Red","Green","White" ,"Black"]
# #
# # print(color_list[0],',',color_list[-1])
#
#
# # Write a Python program to get the difference between a given number and 17,
# # if the number is greater than 17 return double the absolute difference
#
# # def differnece(n):
# #
# #     if n <= 17:
# #         print(17-n)
# #     elif n > 17:
# #         print((n-17)*2)
# #
# #
# # differnece(20)
#
#
#
# # Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum
# # a = 10
# # b = 10
# # c = 10
# # sum = a+b+c
# # if a==b==c:
# #     print((a+b+c)*3)
# # else:
# #     print("not equal")
#
# # Write a Python program to get a new string from a given string where "Is" has been added to the front.
# # If the given string already begins with "Is" then return the string unchanged
# # x = "he is a doctor"
# # if x[0] == "is":
# #     print("string unchanged")
# # elif x[0] != 'is':
# #     print("is", x)
#
#
# # WriteaPythonprogramtofindwhetheragivennumber(acceptfrom the user) is even or odd, print out an appropriate message to the user
# # def even_odd(n):
# #     if (n%2)==0:
# #         print("it is a even number")
# #     elif (n%2)!=0:
# #         print("it is a odd number")
# #
# #
# # even_odd(25)
#
# # Write a Python program to count the number 4 in a given list
#
# # list = [1,2,3,4,5,6,4]
# # count = 0
# # for i in list:
# #     if i == 4:
# #         count = count+1
# # print(count)
#
#
# list = [23,1,18,4,16,18,25,52]
#
# x= list[4]
#
# # newlist = []
#
# list.remove(x)
#      # print(list)
#
#      # print(list)
# list[0] = x
# print(list)
#
#

# list = [12,6,32,21,85,46,33]

# newlist = []
# for i in range(len(list)):
#
#     # print(i)
#     if (i%2) == 0:
#         newlist.append(list[i])
# print(newlist)
# import json
# json_data = '{"company":{"employee":{"name":"Chris"}}}'
# y = json.loads(json_data)
# # print(y)
#
# for k in y.values():
#     # print(k)
#     for i in k.values():
#         # print(i)
#
#         i['name'] = 'vamshi'
# # print(i)
# # print(y)
# x = json.dumps(y)
# print(x)

list = ['kambhampati']

for i in list:
    x = str(i)

    y=len(x)/2
    n = int(y)

    z= x[:n] + 'bujju' + x[n:]
    print(z)

# def insert_dash(string, index):
#     return string[:index] + '-' + string[index:]
#
# print (insert_dash("355879ACB6", 5))




















s1 = "vamshi"
s2 = "teju"



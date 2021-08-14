# list = ["apple","bananan","mango"]
# print(list[-1])
# print(list.append("cherry"))
# if 'apple' in list:
#     print("yes apple is in the list")
# else:
#     print('no',"apple is not in the list")
#
# #

#
# x = "vamshi"
# y = "krishna"
#
#
# z = y[::-1]+" "+ x[::-1]
# print(z)

# def csvnumbers(*args):
#
#     x = list(args)
#     y = tuple(args)
#
#     print(x)
#     print(y)
#
# csvnumbers(15,20,1,5,14,12,13,46,78)

# x= "abc.python"
#
# y = x.split(".")
# print(y[-1])


# colors = ["Red","Blue","Green","Yellow"]
# print(colors[-1],",",colors[0])

# Write a Python program to get the difference between a given number and 17,
# if the number is greater than 17 return double the absolute difference
# def differenece(x):
#     if x>17:
#         print(x*x)
#     elif x<17:
#         print(17-x)
#     else:
#         print(x)
# differenece(45)
# differenece(15)
# differenece(17)

# Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return three times of their sum


# def sumofnumbers(x,y,z):
#     a = x+y+z
#     print(a)
#     if x==y==z:
#         print(a*3)
# sumofnumbers(10,10,10)

# Write a Python program to get a new string from a given string where "Is" has been added to the front.
# If the given string already begins with "Is" then return the string unchanged

# def addstring(x):
# ----------------------------------------------------------------------------------------------------------------
# x = "He is a doctor"
# if x[0] == "is":
#     print("is added")
# else:
#     print("is",x)
# ------------------------------------------------------------------------------------------------------------------
# Write a Python program to find whether a given number(accept from the user) is even or odd,
# print out an appropriate message to the user


# def evenorodd(x):
#
#     if x%2 == 0:
#         print("It is a even number")
#     else:
#         print("It is a odd number")
#
# evenorodd(44)
# evenorodd(45)
# evenorodd(24)
# evenorodd(13)

# --------------------------------------------------------------------------------------
# list = [12,4,1,5,21,4,3,12,4,58,96,44]
#
# count = 0
# for i in list:
#     if i == 4:
#         count = count+1
# print("the number of times 4 present in the list is",count)
# ___________________________________________________________________________________________________
# Given an integer, return the integer with reversed digits.
#
# ____________________________________________________________________________________________________
# For a given sentence, return the average word length.
# Note: Remember to remove punctuation first.

# sentence1 = "Hi all, my name is Tom...I am originally from Australia."
# sentence2 = "I need to work very hard to learn more about algorithms in Python!"

# _____________________________________________________________________________________________________________________________
# list = [15,25,26,41,12,18,12,150,180,200]
# #display the numbers are which are divisable by 5 but if the number is greater than 150 dont print
# # list2 = []
# for i in list:
#     if i%5==0 and i<=150:
#         print(i)


#######################################################
# x = 23
#
# y = str(x)
#
# count = 0
# for i in y:
#     # if i in y:
#         count = count+1
# print(count)
######################################################################
# list =[1,2,3,4,5]
# list1 = ["vamshi"]
#
# list2 = list+list1
# print(list2)
# #########################################################################
#
# def findidigit(string):
#
#  count = 0
#  counta = 0
#  for i in string:
#      if i.isdigit():
#         count = count+1
#      elif i.isalpha():
#          counta = counta+1
#  print("the number of digits in astring are",count)
#  print("the number of alphabhes in a string are",counta)
#
#
# findidigit("vamshi123")
# # findidigit("siteja67589")

################################################################################
# dict = {"id":[2,3,5],"name":["vamshi","teja"]}
# # dict1 = {
#
# x = dict["id"]
# z = dict["name"]
# # print(x)
# for i in x:
#     if i == 5:
#      y =  x.index(5)
#      x[y] = 6
# # print(x)
# dict["id"] = x
# # print(dict)
# z.append("kambhamapti")
# dict["name"] = z
# print(dict)
################################################################################################
# def findi(n):
#     my_dict = {}
#     for i in range(1,n):
#        key = i
#        value = i*i
#        my_dict[key]= value
#     print(my_dict)
#
# findi(10)
########################################################################################################
# def eachn():
#     # x = ''
#     new_list = []
#     for i in range(1000, 2000):
#         j = str(i)
#         # print(j[0])
#         x = j[0]
#         y = j[1]
#         z = j[2]
#         m = j[3]
#         if (int(x) % 2 == 0) :
#             new_list.append(i)
#         print(i,"it is a even number")
#     #
#     #     and (int(y) % 2 == 0) and (int(z) % 2 == 0) and (int(m) % 2 == 0):
#     #         print(i)
#     #         new_list.append(i)
#     #
#     # print(new_list, "it is a number")
#
#
# eachn()
################################################################################################333333333333333333
# Find A given number is leap year or not

# def leapornot(n):
#     if n%4 == 0 and  (n % 100) != 0 :
#             print(n,"is a leap year")
#     else:
#             print(n,"is not a leap year")
#
#
# leapornot(2020)
# leapornot(1992)
# leapornot(2024)
# leapornot(2021)
# leapornot(1801)
# leapornot(1986)
##########################################################################################
# import datetime
#
# current_date = datetime.datetime.now()
# print(current_date)
##################################################################"'
# how to filter a posituv enumber from the list


# def postivefinder(list):
#
#
#     for i in list:
#      if i >0:
#         print(i,"it is a postitve number")
#      else:
#         print(i,"it is a negtive number")
#
#
# postivefinder([45,-48,98,100,0,-78])
###############################################################################################################3
# Write a Python program to calculate the sum of the digits in an integer
# def sumofinteger(n):
#
#
#     x = str(n)
#     count = []
#     for i in x:
#         i = i+1
#         print(i)
#
# sumofinteger(4859)'
##############################################################################################
# sentense = ["Hello" ,"world!",2021,"How","was",2020]
#
# c = str(sentense)
# # print(type(c))
# counta = 0
# countd = 0
# for i in c:
#    if  i.isalpha():
#        counta = counta+1
#    elif  i.isdigit():
#         countd = countd+1
# print("number of digits are",countd)
# print("number of alphabets are",counta)

##########################################################################

# digit = 4859
# x = str(digit)
# sum_of_number = 0
# for i in x:
#
#    sum_of_number = sum_of_number+int(i)
# print(sum_of_number)
################################################################################################
# def defining(a):
#
#     formula = a+a*a+a*a*a
#     print(formula)
#
# defining(2)
#####################################################################################################x
# list = [2,3,6,5,48,45,74,569]
#
# x = list[2:5]
# print(x)
# s1 = 'vamshik'
# s2 = 'teju'
#
#
# middles1 = int(len(s1)/2)
# middles1value = s1[middles1]
#
# middles2 = int(len(s2)/2)
# middles2value = s2[middles2]
#
# finalstring = s1[0]+s2[0]+middles1value+middles2value+s1[-1]+s2[-1]
# print(finalstring)

# input = "PytejUkAMbat"
# #ytejkbatPUAM
#
# x1 = []
# x2 = []
#
#
# for i in input:
#     if i.islower():
#         x1.append(i)
#     elif i.isupper():
#         x2.append(i)
# x3 = x1+x2
# str = ''.join(x3)
# print(str)

#
#
# input = "PhOle@tVA!%mC23"
# uppercount = 0
# lowercount = 0
# digitcount = 0
# special_char = 0
# for i in input:
#     if i.islower():
#         uppercount = uppercount+1
#     # print(uppercount)
#     elif i.isupper():
#          lowercount = lowercount+1
#     # print(lowercount)
#     elif i.isdigit():
#           digitcount = digitcount+1
#     else:
#         special_char = special_char+1
#         # print(special_char)
# print("uppercase character count is",uppercount)
# print("lowercase  character count is ",lowercount)
# print("special characte count is ",special_char)
# print("count of digits is ",digitcount)

# s4 = "welcome to usa. usa is land of dreams" # no of times usa occured in this
# s5 = "PYhelloYou" # he is part of s5
# s6 = "Apple" # count occurances of each character. a- 1, p -2 , l-1 e -1

#
# s4 = "welcome to usa. usa is land of dreams"
# def string_count(string,name):
#     return string.count(name)
#
# x = string_count("welcome to usa. usa is land of dreams",'usa')
# print(x)

#
#
#
# s6 = "Apple"
# acount = 0
# pcount = 0
# lcount = 0
# ecount = 0
# for i in s6:
#     if i == 'a':
#         acount = acount+1
#     elif i == 'p':
#         pcount = pcount+1
#     elif i == 'l':
#         lcount = lcount+1
#     elif i == 'e':
#         ecount = ecount+1
# print("acount is",acount)
# print("pcount is",pcount)
# print("lcount is",lcount)
# print("ecount is",ecount)
#
#
# s1 = "PYhello"
# s2 = 'he'
# if s2 in s1:
#     print("present")


# string = "apple"
# string1 = " "
#
# for i in string:
#     if i in string1:
#         string1[i] = string1[i]+1

# dict1 = {"a":100,"b":200,"c":300} # check if 200 is present in the values. If yes print true
# dict2 = {"name":"teju","salary":5000,"place":"fairfax"} # rename "place" to "city" and change salary to 8000
#
# get the key corresponding to min value. Output should be Math
#
# str1 = "Teju is in USA. Teju is working now" # find the last position/index of "teju" in this string
# str2= "teju" # reverse the string
# str3 = ["emma","teju","","hello"] # remove empty string from list. Output should be ["emma","teju","hello"]


# dict1 = {"a":100,"b":200,"c":300}
# for k,v in dict1.items():
#     if v == 200:
#         print("yes")



# dict2 = {"name":"teju","salary":5000,"place":"fairfax"}
#
#
# new_key = "city"
# old_key = "place"
#
# dict2[new_key] = dict2.pop(old_key)
# dict2['salary'] = 8000
# print(dict2)


#
#
#
#
#
#
#
# dict3 = {"physics":80,"Math":40,"chemistry":90}
#
#
# print(min(dict3, key=dict3.get))
#
#
# str1 = "Teju is in USA. Teju is working now"
#
# x =str1.rfind('Teju')
# print(x)
#
#
# str2= "teju"
# x = str2[::-1]
# print(x)
#
# str3 = ["emma","teju","","hello"]
# while("" in str3) :
#     str3.remove("")
# print(str3)
#
#
# dict1 = {"a":100,"b":200,"c":300}
# for k,v in dict1.items():
#     if v == 200:
#         print(k)

#
# # stre1 = "Siteja is @ developer /* & Musician" # remove special chars. Siteja is developer Musician
# # stre2 = "Siteja25 is data sceint50st and AI expert" # get only the words which contain alphabets and digits. Siteja25 sceint50st
# # liste1 = [12,15,32,55,75,150,180,200] # display numbers which are divisible by 5 and if you find a number greater than 150 stop the iteration.
#
# stre1 = "Siteja is @ developer /* & Musician"
#
# str2 = ''
# for i in stre1:
#     if i.isalnum():
#         str2 = str2+ i
#
# print(str2)
#
#
# import re
# stre2 = "Siteja25 is data sceint50st and AI expert"
# res = re.findall(r'(?:\d+[a-zA-Z]+|[a-zA-Z]+\d+)', stre2)
# print(res)
#
#
#
#
#
#
# liste1 = [12,15,32,55,75,150,180,200]
#
# for i in liste1:
#     if i > 150:
#         break
#     elif (i%5)== 0:
#         print(i)
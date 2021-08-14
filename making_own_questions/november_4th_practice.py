# str1 = "Hello world. hello Teju. hellO Vamshi". Find no of times hello is present
import re
str1 = "Hello world. hello Teju. hellO Vamshi"
x= str1.lower()
l = x.split()
print(l)
count = 0
for i in x.split():
    if i == 'hello':
        count = count+1

print(count)




###########################################################################################################

str2 = "Chem = 50 Physics = 20"

lst = []
for i in str2.split():
    # print(i)
    if i.isdigit():

        lst.append(i)
sum = 0
avg = 0
for i in lst:
    sum = sum+int(i)
avg = sum/len(lst)
print(sum)
print(avg)
######################################################################################################################
# Create python object with name "Toyota"  brand "Corolla" year "2020". Convert it to json and save it to file
import json


python_obj = {"name":"toyota","brand":'corolla',"year":2020}
print(type(python_obj))
json_object = json.dumps(python_obj)
print(type(json_object))
with open("sample_filejson","w") as jsonFile:
    jsonFile.write(json.dumps(json_object))




##########################################################################################

#write a function which accepts any number of arguments and prints the value.
#For ex  nums(20,30) should print 20 30

def accepts_num(*args):

    for i in args:
        print(i)


accepts_num(20,30)
#################################################################################################
list = [10,24,56,1,45,33]
x = max(list)
print(x)
################################################################################################


# generate python list of all odd numbers between 4 and 45
for i in range(4,45):
    if (i%2) != 0:
        print(i,"is a odd number")
#################################################################################

















import json

json_obj = '{"company":{"employee":{"name":"Chris","occupation":"Developer"}}}'
y = json.loads(json_obj)
# print(y)

x = y['company']

for k,v in x.items():
    # print(v)

    for key,value in v.items():
        print(value)


######################################################################3
x = 2+22+222
sum = 0
new_s = []
for i in str(x):
    print("i is",i)
    new_s.append(i)
# print(new_s)

for i in new_s:
    sum = sum+int(i)
print(sum)
###############################################################################


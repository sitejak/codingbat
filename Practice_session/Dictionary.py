my_dict = {"emp_name":"tom","emp_id":2013,"emp_branch":"cse","emp_university":"texas a &m"}

x = my_dict["emp_name"]
print(x)
#get method

x = my_dict.get("emp_branch")
print(x)

#iteration

my_dict = {"emp_name":"tom","emp_id":2013,"emp_branch":"cse","emp_university":"texas a &m"}

for key,values in my_dict.items():
    print(key,values)

#get values using keys

for x in my_dict.values():
    print(x)

#get method

x = my_dict.get("emp_branch")
print(x)

#change values
my_dict["emp_branch"] = "electronics"
print(my_dict)



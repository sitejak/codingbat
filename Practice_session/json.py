#python object to json object
# import json
# string = '''{"people":[{"emp_name": "John smith","emp_no.": "924367-567-23","emp_email": "johnsmith@gmail.com",
# "license": "false"},{"emp_name": "william smith","emp_no.": "560-555-5153","emp_email": "null","license": "true"}]}'''
#
#
# json_file = json.loads(string)
# print(type(json_file))
# new_file = json.dumps(json_file)
# print(type(new_file))


#json to python

# import json
#
# x= '{"name":"tom","age":24,"graduation_year":2020,"address":"Newyork","phonenumber":[{"home":48548589},{"cell":9875849645}]}}'
#
# python = json.loads(x)
# print(type(python))

#json to csv
import json
import csv
json_file = '{"student_list":[{"name":"Tom","age":25,"student_id":45654,"student_department":"IT","Address":"45th street Newyork"},{"name":"eric","age":25,"student_id":77788,"student_department":"cse","Address":"46th street Newyork"},{"name":"emily","age":25,"student_id":58487,"student_department":"IT","Address":"47th street Newyork"}]}'
y = json.loads(json_file)
# print(type(y))
my_file = y["student_list"]
# print(type(my_file))
file = open("mycsv.csv","w")
csv_writer = csv.writer(file)
# print(csv_writer)
#
count = 0
for employee in my_file:
    if count == 0:
        header = employee.keys()
        csv_writer.writerow(header)
        count = count+1
        # print(header)
        csv_writer.writerow(employee.values())
        result = employee.values()
        print(header)
        print(result)
file.close()









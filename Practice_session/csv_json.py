import csv
# import json


csv_file = "myfile.csv"
json_file = "mycsv1.csv"


data = {}
with open(csv_file) as file:
    csvReader = csv.DictReader(file)
    print(csvReader)


    for i in csvReader:
        student_cls_id = i[student_cls_id]
        data[student_cls_id] = i

print(data)
#
# x = json.dumps(data)
#
# file.close()
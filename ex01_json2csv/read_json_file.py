import json
import csv

#Open and extract datas from json file

file_name = input('write here your json file name please : ')

file_open = open("/Users/loicnguessie/Documents/Fac/M1/Efrei-Cours/Python/projects/
ex01_json2csv/"+file_name, )

json_file_load = json.load(file_open)

first_header = "json_file_load.items()[0][0]"

headers = [json_file_load.items()[0][1][0].items()[0][0], json_file_load.items()[0][1][0].items()[1][0]]

datas = []

for i in json_file_load.items()[0][1]:
	data = []
	for j in i.items():
		data.append(j[1])
	datas.append(data)


#the new csv file

with open("/Users/loicnguessie/Documents/Fac/M1/Efrei-Cours/Python/projects/ex01_json2csv/wF.csv","w") as file_write:
	writer = csv.writer(file_write)
	writer.writerow(headers)
	writer.writerows(datas)

file_open.close()
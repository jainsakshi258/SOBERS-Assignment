import pandas as pd
import csv

col_list1 =['timestamp', 'type', 'amount','from', 'to']
df1 = pd.read_csv("/Users/keshav174/Downloads/sakshi/3927bfab39b32d401dc0a4ca8db995bd/SOBERS_Assignment/bank1.csv", usecols=col_list1)

list1= []
for index, data in df1.iterrows():
	list1.append([data['timestamp'],data['type'],data['amount'],data['to'],data['from']])


col_list2 =['date', 'transaction', 'amounts','to', 'from']
df2 = pd.read_csv("/Users/keshav174/Downloads/sakshi/3927bfab39b32d401dc0a4ca8db995bd/SOBERS_Assignment/bank2.csv", usecols=col_list2)


list2 =[]
for index, data in df2.iterrows():
	list2.append([data['date'],data['transaction'],data['amounts'],data['to'],data['from']])


col_list3 =['date_readable','type','euro', 'cents', 'to', 'from']
df3 = pd.read_csv("/Users/keshav174/Downloads/sakshi/3927bfab39b32d401dc0a4ca8db995bd/SOBERS_Assignment/bank3.csv", usecols=col_list3)


list3=[]
for index, data in df3.iterrows():
	list3.append([data['date_readable'],data['type'],float(str(data['euro'])+'.'+str(data['cents'])),data['to'],data['from']])


fields =  ['date', 'transaction', 'amounts', 'to', 'from'] 
filename = "/Users/keshav174/Downloads/sakshi/3927bfab39b32d401dc0a4ca8db995bd/SOBERS_Assignment/final.csv"

with open(filename, 'w') as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(fields)
	csvwriter.writerows(list1)
	csvwriter.writerows(list2)
	csvwriter.writerows(list3)

csvfile.close()

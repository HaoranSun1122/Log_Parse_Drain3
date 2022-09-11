import pandas as pd
import csv

# csvfile = open('Parsed_Parameter.csv',encoding='utf-8')
# df = pd.read_csv(csvfile,engine='python')
# print(range(len(df)))
#
# for i in range(len(df)):
#     print(df[i])

from csv import reader
fileout = open('labels1.csv', 'w')

# open file
with open("Parsed_Parameter.csv", "r") as my_file:
    # pass the file object to reader()
    file_reader = reader(my_file)
    # do this for all the rows
    for i in file_reader:
        # print the rows
        print(i)
        fileout.write(i.replace('"', ''))
        print(i)
fileout.close()

# df = pd.read_csv("Parsed_Parameter.csv")
#
# error_bad_lines=False #加入参数
# df.drop(df.index[11175630:20743527],inplace=True)
# df.to_csv("Parsed_Parameter.csv",index=False,encoding="utf-8")

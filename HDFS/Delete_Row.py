import pandas as pd
import csv

# csvfile = open('Parsed_Parameter.csv',encoding='utf-8')
# df = pd.read_csv(csvfile,engine='python')
# print(range(len(df)))
#
# for i in range(len(df)):
#     print(df[i])

# from csv import reader
# fileout = open('labels1.csv', 'w')
#
# # open file
# with open("Parsed_Parameter.csv", "r") as my_file:
#     # pass the file object to reader()
#     file_reader = reader(my_file)
#     # do this for all the rows
#     for i in file_reader:
#         # print the rows
#         print(i)
#         fileout.write(i.replace('"', ''))
#         print(i)
# fileout.close()


# 14/09能用的删除行方法！！！
df = pd.read_csv("Parsed_Parameter1.csv", encoding='utf-8',sep = '\t')
# error_bad_lines=False #加入参数
print(df)
df.drop(df.index[11175628:19617607], inplace=True)
df.to_csv("Parsed_Parameter2.csv", index=False, encoding="utf-8")
df2 = pd.read_csv("Parsed_Parameter1.csv", encoding='utf-8',sep = '\t')
print(df2)
# 14/09能用的删除行方法！！！


# import pandas
#
# df = pandas.read_csv('Parsed_Parameter2.csv', encoding='utf-8',header=None,sep = '\t')
# print(df)
# df.replace('"', '', inplace=True, regex=True)
# df.to_csv("file.csv",header=False, index=False)
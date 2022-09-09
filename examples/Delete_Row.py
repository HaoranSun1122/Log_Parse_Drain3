import pandas as pd
import csv

csvfile = open('Parsed_Parameter.csv',encoding='utf-8')
df = pd.read_csv(csvfile,engine='python')
print(range(len(df)))

for i in range(len(df)):
    print(df[i])




# df = pd.read_csv("Parsed_Parameter.csv")
#
# error_bad_lines=False #加入参数
# df.drop(df.index[11175630:14506674],inplace=True)
# df.to_csv("data_new.csv",index=False,encoding="utf-8")

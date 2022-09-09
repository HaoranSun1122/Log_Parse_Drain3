import pandas as pd


file1 = open('Parsed_Parameter.csv', 'r').readlines()
fileout = open('Parsed_Parameter_New.csv', 'w')
for line in file1:
    # fileout.write(line.replace('"', ''))
    print(fileout.write(line.replace('"', '')))
fileout.close()





# df = pd.read_csv("Parsed_Parameter.csv")
#
# error_bad_lines=False #加入参数
# df.drop(df.index[11175630:14506674],inplace=True)
# df.to_csv("data_new.csv",index=False,encoding="utf-8")

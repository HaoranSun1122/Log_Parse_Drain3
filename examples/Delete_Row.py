import pandas as pd

df = pd.read_csv("Parsed_Parameter.csv")
error_bad_lines=False #加入参数
df.drop(df.index[11175630:23539049],inplace=True)
df.to_csv("data_new.csv",index=False,encoding="utf-8")

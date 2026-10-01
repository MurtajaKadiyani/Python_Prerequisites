import pandas as pd
from io import StringIO
Data = '{"employee_name": "James", "email": "james@gmail.com", "job_profile": [{"title1":"Team Lead", "title2":"Sr. Developer"}]}'
df = pd.read_json(StringIO(Data))
print(df)
df.to_json()
print(df)
df.to_json(orient='records')
print(df)
df.to_json(orient='index')
print(df)

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data", header= None)
print(df.head())
df.to_csv("wine.csv")

headers = {"User-Agent": "Mozilla/5.0"}

url="https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/"
df = pd.read_html(url, storage_options=headers)

print(df[0])

url="https://en.wikipedia.org/wiki/Mobile_country_code"
pd.read_html(url,match="Country",header=0, storage_options=headers)[0]

df_excel = pd.read_excel('../data.xlsx')
df_excel.to_pickle('df_excel')
pd.read_pickle('df_excel')


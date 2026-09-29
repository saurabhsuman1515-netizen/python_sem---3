import pandas as pd
df = { 'Name': ["Alex","BOb","Clarke"],'Age':[10,12,13]}
pop = pd.DataFrame(df)
print('Details :   \n' , pop,'\n')
pop.to_csv('output5.csv')
print(df['Name'])
print (df["Age"])

import pandas as pd

a = pd.read_csv("book.csv")

print(a,"\n")
print(a.head(2))
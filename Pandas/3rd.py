import pandas as pd
print(pd.__version__)

d ={'one' : pd.Series([1,2,3],index=['a','b','c']),
    'two' : pd.Series([1,2,3,4],index = ['a','b','c','d'])}
df = pd.DataFrame(d)
print(df)
print("Adding a new column by Passing as series: ")
df["three"]=pd.Series([10,20,30],index =['a','b','c'])
print (df)
print("Adding new coloumn using existing the coloumn data frame: ")
df['four'] = df['one']+df['three']
print(df)

import pandas as pd
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']), 'two': pd.Series([1, 2, 3, 4], 
    index=['a', 'b', 'c', 'd']), 'three': pd.Series([10, 20, 30], index=['a', 'b', 'c'])}
df = pd.DataFrame(d)

print ("Our dataframe is:")
print (df)

# using del function
print ("Deleting the first column using DEL function:")

del df['one']
print (df)

#using pop function

print ("Deleting another column using POP function:")
df.pop('two')
print (df)

d = {'one' : pd.Series([1,2,3],index=['a','b','c']),
     'two' : pd.Series([1,2,3,4],index=['a','b','c','d'])}
df = pd.DataFrame(d)
print(df.iloc[2])

d = {'one' : pd.Series([1,2,3],index=['a','b','c']),
     'two' : pd.Series([1,2,3,4],index=['a','b','c','d'])}
df = pd.DataFrame(d)
print(df.iloc[2:4])
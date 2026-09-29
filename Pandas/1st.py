import pandas as pd

pop = pd.Series(
    [38, 26, 19, 19],
    index=['ca', 'tx', 'ny', 'fl']
)
# population, in millions
print(pop)
pop.to_csv('output1.csv')




df = { 'ca': [35,37,38],'tx':[23,24,26],'md':[5,5,6]}
pop = pd.DataFrame(df)
print('population : \n' , pop,'\n')
pop.to_csv('output2.csv')



pop = pd.DataFrame(df,index = [2010,2012,2014])
print('population : \n',pop,'\n')
pop.to_csv('output3.csv')


df = {'ca':[35,37,38],'tx':[23,24,26],'md':[5,5,6]}
pop=pd.DataFrame(df)
print('population:\n' , pop,'\n')
pop.to_csv('output4.csv')

import pandas as pd

#Q.1 - Create a dataframe with your name , age , mail id and phone number and add your friends’s information to the same.
data={'Name':['Piyush Kumar'],'Age':[20],'Email':['piyushkp@gmail.com'],'mob no.':['7508882281']}
df=pd.DataFrame(data)
df.loc[1]=['Ayush',22,'ayushkp1000@gmail.com','9905448263']
df.loc[2]=['Ankit',21,'ankit@gmail.com','90060105698']
df.loc[3]=['Ritesh',20,'ritesh@gmail.com','7081388816']
print(df)

"""Q.2 - 
Import the data and print the following :
a.) First 5 rows of Dataframe 
b.) First 10 rows of the Dataframe 
c.) find basic statistics on the particular dataset. 
d.) Find the last 5 rows of the dataframe 
e.) Extract the 2nd column and find basic statistics on it."""

df=pd.read_csv('dataset.csv')
# 2.a
print(df.head(5))
# 2.b
print(df.head(10))
# 2.c
print(df['MinTemp'].describe())

print(df['MaxTemp'].describe())
# 2.d
print(df.tail(5))
# 2.e
new_data=[df.iloc[:,2].sum(),df.iloc[:,2].mean(),df.iloc[:,2].median(),df.iloc[:,2].nunique(),df.iloc[:,2].max(),df.iloc[:,2].min()]
print(new_data)

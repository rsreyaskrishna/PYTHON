import numpy as np
import pandas as pd

# Load the data
df = pd.read_csv('/Users/sruthikrishna/Downloads/customer1.txt', sep=',', header=None)
df.columns = ['id', 'fname', 'lname', 'age', 'prof', 'location']
print("*"*50)
# 1. Age above 50
df1 = df.loc[df['age'] > 50, ['fname', 'lname', 'age', 'prof', 'location']]
print(df1)
print("*"*50)
# 2. Age range 25 to 40
df2 = df.loc[(df['age'] >= 25) & (df['age'] <= 40), ['fname', 'lname', 'age', 'prof']]
print(df2)
print("*"*50)
# 3. Working in India
df3 = df.loc[df['location'] == 'india', ['fname', 'lname', 'age', 'prof']]
print(df3)
print("*"*50)
# 4. Top 5 oldest employees
df4 = df.sort_values(by='age', ascending=False)[['fname', 'lname', 'age', 'prof']].head(5)
print(df4)
print("*"*50)
# 5. Youngest 3 employees
df5 = df.sort_values(by='age')[['fname', 'lname', 'age', 'prof']].head(3)
print(df5)
print("*"*50)
# 6. Youngest 3 employees working in India
df6 = df.loc[df['location'] == 'india'].sort_values(by='age')[['fname', 'lname', 'age']].head(3)
print(df6)
print("*"*50)
# 7. Doctors working in India
df7 = df.loc[(df['location'] == 'india') & (df['prof'] == 'Doctor'), ['fname', 'lname', 'age', 'prof']]
print(df7)
print("*"*50)
# 8. Youngest pilot
df8 = df.loc[df['prof'] == 'Pilot'].sort_values(by='age')[['fname', 'lname', 'age']].head(1)
print(df8)
print("*"*50)
# 9. Oldest doctor
df9 = df.loc[df['prof'] == 'Doctor'].sort_values(by='age', ascending=False).head(1)
print(df9)
print("*"*50)
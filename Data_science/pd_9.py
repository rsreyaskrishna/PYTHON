# converting an External file to dataframe
import numpy as np
import pandas as pd

df = pd.read_csv('/Users/sruthikrishna/Downloads/sample4.txt', sep=',', header=None)

df.columns = ['id', 'fname', 'lname', 'age', 'phno', 'location']  # to give header tag to columns
print(df)


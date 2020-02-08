import numpy as np
import pandas as pd

# import data
df = pd.read_csv('smsspamCollection.tsv', sep='\t')
print(df.head())

print(len(df))

# check for missing values:
print(df.isnull().sum()) #if there is 1 then there is a missing value.

# take a quick look at the ham and spam label column
df['label'].unique()

df['label'].value_counts()

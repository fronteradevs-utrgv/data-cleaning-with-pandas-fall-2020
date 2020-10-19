# import libraries
import pandas as pd

# read csv file into a pandas dataframe
df = pd.read_csv("COVID19_line_list_data.csv")
print(df.head)

# look at the case_in_country
print(df['case_in_country'])
print(df['case_in_country'].isnull())

# delete column from dataframe
del df['summary']
del df['Unnamed: 3']
del df['age']

# deleting records with nan values from the gender column
df.dropna(subset = ["gender"], inplace=True)

print(df.head)

# total missing values for each column in the df  
print(df.isnull().sum())

# export to new csv file on machine to visualize for next workshop
df.to_csv("Downloads/COVID_complete.csv", index=False)

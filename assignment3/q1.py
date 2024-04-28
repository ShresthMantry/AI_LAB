import pandas as pd

data = {'Std_Name': ['Student1', 'Student2', 'Student3', 'Student4'],
        'Roll_no': [101, 102, 103, 104],
        'CPI': [75, 58, 62, 70]}

df = pd.DataFrame(data)

filtered_df = df[df['CPI'] > 60]

mean_cpi = df['CPI'].mean()
median_cpi = df['CPI'].median()
std_dev_cpi = df['CPI'].std()


print("Original DataFrame:")
print(df)

print("\nFiltered DataFrame:")
print(filtered_df)

print("\nOverall Mean CPI:", mean_cpi)
print("Overall Median CPI:", median_cpi)
print("Overall Standard Deviation CPI:", std_dev_cpi)

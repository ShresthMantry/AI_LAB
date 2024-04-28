import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 17, 30, 22],
        'Salary': [50000, -1000, 75000, 60000]}

dirty_data = pd.DataFrame(data)

clean_data = dirty_data[(dirty_data['Age'] >= 18) & (dirty_data['Salary'] >= 0)]


print("Original DataFrame:")
print(dirty_data)

print("\nCleaned DataFrame:")
print(clean_data)

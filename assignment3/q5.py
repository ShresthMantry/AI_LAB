import pandas as pd

data = {'TimeStamp': ['2024-02-02 08:30:00', '2024-02-02 14:45:00', '2024-02-02 21:15:00']}
time_df = pd.DataFrame(data)
time_df['TimeStamp'] = pd.to_datetime(time_df['TimeStamp'])

time_df['Hour'] = time_df['TimeStamp'].dt.hour


print("Original DataFrame:")
print(time_df[['TimeStamp']])

print("\nDataFrame with 'Hour' column:")
print(time_df[['TimeStamp', 'Hour']])

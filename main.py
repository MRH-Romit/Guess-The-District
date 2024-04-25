import csv
import pandas

data=pandas.read_csv('weather_data.csv')
print(data)


data_dict=data.to_dict()
print("temp column:\n ")
temp_list=data['temp'].to_list()


print(f"average temp: {data['temp'].mean():.2f}")
print("max temp: ",data['temp'].max())
print("lowest temp: ",data['temp'].min())

# in sorting order

sorted_data=data.sort_values(by='temp')
sorted_df = data.sort_values(by=['day', 'temp'], ascending=[True, False])
print(sorted_data)
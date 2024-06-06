import pandas as pd


file_path = 'D:\Guess The District\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'
squirrel_data = pd.read_csv(file_path)


color_counts = squirrel_data['Primary Fur Color'].value_counts().reset_index()
color_counts.columns = ['Primary Fur Color', 'Count']

# Display the color categorization counts
print(color_counts)

# Path for the new CSV file
output_file_path = 'D:\Guess The District\Squirrel_Color_Categorization.csv'

# Save the DataFrame to a new CSV file
color_counts.to_csv(output_file_path, index=False)

print(f"Data saved to {output_file_path}")


import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
file_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0078__Day74_Aggregate_and_Merge_Data_w_Pandas__240814\NewProject\r00-r09 START\r00_env_START\data\sets.csv'
df = pd.read_csv(file_path)

# Calculate the average number of parts per LEGO set for each year
parts_per_set = df.groupby('year').agg({'num_parts': pd.Series.mean})

# Display the first few rows to verify the result
print(parts_per_set.head())
print(parts_per_set.tail())

# Exclude the last two years from the data
parts_per_set_trimmed = parts_per_set[:-2]

# Create a scatter plot to visualize the trend
plt.figure(figsize=(10, 6))
plt.scatter(parts_per_set_trimmed.index, parts_per_set_trimmed['num_parts'], color='b', marker='o')
plt.title('Average Number of Parts per LEGO Set Over Time (Excluding Last 2 Years)')
plt.xlabel('Year')
plt.ylabel('Average Number of Parts')
plt.grid(True)
plt.show()
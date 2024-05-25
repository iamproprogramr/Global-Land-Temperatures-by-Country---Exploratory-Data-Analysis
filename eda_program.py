#This program is written by muhammad yousaf Email:yousafsahiwal3@gmail.com
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('GlobalLandTemperaturesByCountry.csv')


print("First few rows of the dataset:")
print(df.head())
print("\nDataset Information:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())
print("\nMissing Values:")
print(df.isnull().sum())

df.dropna(inplace=True)
df['dt'] = pd.to_datetime(df['dt'])
df['Year'] = df['dt'].dt.year
df_grouped = df.groupby(['Country', 'Year'])['AverageTemperature'].mean().reset_index()



#1
plt.figure(figsize=(12, 6))
country = 'United States'
country_data = df_grouped[df_grouped['Country'] == country]
plt.plot(country_data['Year'], country_data['AverageTemperature'], marker='o')
plt.title(f'Average Temperature Over Time in {country}')
plt.xlabel('Year')
plt.ylabel('Average Temperature (°C)')
plt.grid(True)
plt.savefig('average_temperature_over_time_US.png')
plt.show()

#2
plt.figure(figsize=(12, 6))
sns.histplot(df['AverageTemperature'], bins=30, kde=True)
plt.title('Distribution of Average Temperatures')
plt.xlabel('Average Temperature (°C)')
plt.ylabel('Frequency')
plt.grid(True)
plt.savefig('distribution_of_average_temperatures.png')
plt.show()

#3
plt.figure(figsize=(12, 6))
top_countries = df['Country'].value_counts().index[:10]
sns.boxplot(x='Country', y='AverageTemperature', data=df[df['Country'].isin(top_countries)])
plt.title('Box Plot of Average Temperatures by Country')
plt.xlabel('Country')
plt.ylabel('Average Temperature (°C)')
plt.xticks(rotation=90)
plt.grid(True)
plt.savefig('box_plot_by_country.png')
plt.show()

#4
plt.figure(figsize=(12, 8))
heatmap_data = df_grouped[df_grouped['Country'].isin(top_countries)]
heatmap_data_pivot = heatmap_data.pivot(index='Year', columns='Country', values='AverageTemperature')
sns.heatmap(heatmap_data_pivot, cmap='coolwarm', annot=False)
plt.title('Heatmap of Average Temperatures for Top Countries Over Years')
plt.xlabel('Country')
plt.ylabel('Year')
plt.savefig('heatmap_by_country.png')
plt.show()

print("\nInsights Summary:",)
print(f"1. The dataset contains temperature records from {df['dt'].min()} to {df['dt'].max()}.")
print("2. Missing values were found and dropped.")
print("3. The average temperature over time can be visualized for specific countries.")
print("4. The distribution of average temperatures shows a clear pattern.")
print("5. Box plots and heatmaps reveal variations in temperatures across different countries and years.")

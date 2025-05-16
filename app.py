import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Data ingestion
df = pd.read_csv('weather_data.csv')
print(df)

# Data cleaning
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(df.iloc[:, 2:5].values)
df.iloc[:, 2:5] = imputer.transform(df.iloc[:, 2:5].values)

# This is to remove rows with nan values for date and weather_condition
df = df.dropna()

df.loc[:, 'date'] = pd.to_datetime(df['date'], format='mixed', dayfirst=True, errors='coerce')
df = df.dropna()
df.loc[:,'temperature_fahrenheit'] = df['temperature_celsius'] * 9/5 + 32
df = df[df['weather_condition'].str.lower() != 'unknown']


# Data output
# Here we're making sure the outputs folder exists
os.makedirs('outputs', exist_ok=True)
df.to_csv('outputs/transformed_weather_data.csv', index=False)

df.loc[:, 'temperature_celsius'] = pd.to_numeric(df['temperature_celsius'], errors='coerce')
top5 = df.nlargest(5, 'temperature_celsius')

with open('outputs/top5_temperatures.txt', 'w') as file:
    file.write(top5.to_string(index=False))


# Bonus
avg_temp = df.groupby('city')['temperature_celsius'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(data=avg_temp, x='city', y='temperature_celsius', palette='coolwarm', hue='city')
plt.title('Average Temperature per City')
plt.xlabel('City')
plt.ylabel('Average Temperature (°C)')
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('outputs/average_temperature_per_city.png')
plt.show()
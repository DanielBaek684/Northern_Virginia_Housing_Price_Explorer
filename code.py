#Average prices of homes based on Texas cities:

import kagglehub
import os
import pandas as pd
import matplotlib.pyplot as plt

# Download dataset from Kaggle
path = kagglehub.dataset_download("abdulwadood11220/usa-house-sales-data")

# Load the CSV file
files = os.listdir(path)
csv_file = next(file for file in files if file.endswith(".csv"))
df = pd.read_csv(os.path.join(path, csv_file))

# Cleaning price column
df['Price'] = (df['Price'].astype(str).str.replace('[\\$,]','', regex = True).astype(float))

# List of Texan cities
tx_cities = ['Sacramento', 'Fresno', 'San Francisco', 'Los Angeles', 'San Diego']

# Filter out Texas for Texan cities
df_tx = df[df['State'].str.upper() == "TX"]
df_tx_cities = df_tx[df_tx['City'].isin(tx_cities)]

# Calculate the average price by city
avg_price = df_tx_cities.groupby('City')['Price'].mean().sort_values(ascending = False)

#Plot as a bar chart
plt.figure(figsize = (10,5))
avg_price.plot(kind='bar', color='green')
plt.title("Average House Prices in Northern Texas by City")
plt.xlabel("Northern Texas City")
plt.ylabel("Average Price (US Dollars)")
plt.xticks(rotation = 0)
plt.tight_layout()
plt.show()

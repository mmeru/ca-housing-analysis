import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the CSV file
file_path = 'housing.csv'
housing_data = pd.read_csv(file_path)

# Exploratory Data Analysis - Creating scatter plots for various variables
sns.set(style="whitegrid")

# Scatter plot for median house value
plt.figure(figsize=(10, 8)) 
plt.scatter(housing_data['longitude'], housing_data['latitude'], alpha=0.4,
            c=housing_data['median_house_value'], cmap='jet', label='Median House Value')
plt.colorbar(label='Median House Value')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Geographical Distribution of Median House Value')

plt.tight_layout()
plt.show()

# Setting up an Interactive Map using Plotly
fig = px.scatter_mapbox(housing_data, lat="latitude", lon="longitude", 
                        color="median_house_value", size="population",
                        color_continuous_scale=px.colors.cyclical.IceFire, 
                        size_max=15, zoom=5, 
                        mapbox_style="carto-positron",
                        title="Interactive Map of Median House Value and Population")
fig.show()
# Exploratory Data Analysis with Python

This code performs exploratory data analysis (EDA) on a dataset related to California housing data. It utilizes various Python libraries to load, visualize, and analyze the data.

## Data Loading
- The code starts by importing necessary libraries, including `pandas`, `matplotlib`, `seaborn`, and `plotly.express`.
- It specifies the file path as 'housing.csv' and uses `pd.read_csv()` to load the data from the CSV file into a Pandas DataFrame named `housing_data`.

## Data Visualization
- EDA begins with data visualization to gain insights into the dataset.
- `sns.set(style="whitegrid")` sets the style for Seaborn plots, creating a white grid background.

### Scatter Plot of Median House Value
- A scatter plot is created using Matplotlib to visualize the geographical distribution of median house values.

### Interactive Map with Plotly
- An interactive map is created using Plotly Express to visualize the median house value and population by latitude and longitude.

This code is a part of the data exploration process and helps visualize the geographical distribution of median house values and population in the dataset.

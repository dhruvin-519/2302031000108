
import pandas as pd

# Load the dataset
df = pd.read_csv(r'C:/Users/dhruv/OneDrive/Desktop/sales_data.csv')

# Display the first few rows of the DataFrame
print(df.head())
# Display basic information about the DataFrame
print(df.info())

# Display summary statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())
# Calculate total sales for each product
df['Total_Sales'] = df['Quantity'] * df['Price']
total_sales_per_product = df.groupby('Product')['Total_Sales'].sum().reset_index()

# Calculate total quantity sold for each product
total_quantity_per_product = df.groupby('Product')['Quantity'].sum().reset_index()

# Merge the two results
sales_summary = pd.merge(total_sales_per_product, total_quantity_per_product, on='Product', suffixes=('_Sales', '_Quantity'))

print(sales_summary)
import matplotlib.pyplot as plt # type: ignore

# Set the figure size
plt.figure(figsize=(10, 5))

# Bar plot for total sales
plt.subplot(1, 2, 1)
plt.bar(sales_summary['Product'], sales_summary['Total_Sales'], color='blue')
plt.title('Total Sales per Product')
plt.xlabel('Product')
plt.ylabel('Total Sales ($)')

# Bar plot for total quantity sold
plt.subplot(1, 2, 2)
plt.bar(sales_summary['Product'], sales_summary['Quantity'], color='orange')
plt.title('Total Quantity Sold per Product')
plt.xlabel('Product')
plt.ylabel('Quantity Sold')

# Show the plots
plt.tight_layout()
plt.show()

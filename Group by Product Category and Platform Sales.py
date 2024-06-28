#Calculate total order(total sales price * quantity)
#Group by Product Category
#Rank according to total order
import pandas as pd
from datetime import datetime


#Read the Daily Sales File
daily_sales = pd.read_csv(r'C:/Users/Zemo/Documents/Python Tutorial/5th Week For Tutorial/Daily_Sales.csv')

#Calculate total order per product category (price * quantity)
daily_sales['Total Order'] = daily_sales['Price'] * daily_sales['Quantity']

#Group by Product Category -- Then sum the Total Order
#total_order_per_category = daily_sales.groupby('Platform')['Total Order'].sum().reset_index()
total_order_per_category = daily_sales.groupby(['Product Category', 'Platform'])['Total Order'].sum().reset_index()





#Rank the categories by total order(Highest to lowest)
total_order_per_category['Rank'] = total_order_per_category['Total Order'].rank(ascending=False).astype(int)

#Sort the dataframe by rank
total_order_per_category_sorted = total_order_per_category.sort_values(by='Rank')

#Generate the filename for the new csv file
date_today = datetime.now().strftime("%Y-%m-%d")
output_filename = fr'C:\Users\Zemo\Documents\Python Tutorial\5th Week For Tutorial\Sales_per_Platform_category_{date_today}.csv'

#Save the sorted dataframe to a new csv file
total_order_per_category_sorted.to_csv(output_filename,index=False)

print(f"File '{output_filename}' saved! ")

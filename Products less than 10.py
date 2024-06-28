import pandas as pd
from datetime import datetime


#Filte current inventory, save products with less than 10 quantity
#File path Current Inventory
current_inventory_file = r"C:/Users/Zemo/Documents/Python Tutorial/5th Week For Tutorial/Current_inventory.csv"

#Read current inventory csv file
current_inventory_df = pd.read_csv(current_inventory_file)


#Generate file name new csv file
date_today = datetime.now().strftime("%Y-%m-%d")
output_filename = fr'C:\Users\Zemo\Documents\Python Tutorial\5th Week For Tutorial\Stockout_Products_{date_today}.csv'


#Filter current inventory less than 10 quantity
current_inventory_df[current_inventory_df['Quantity']< 10].to_csv(output_filename,index=False)

#Save the filtered csv file
#not_active_inventory_df.to_csv(output_filename,index=False)
#5 mins.
print(f"File '{output_filename}' saved! ")

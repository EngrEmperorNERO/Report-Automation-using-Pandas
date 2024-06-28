import pandas as pd
from datetime import datetime


#file path
current_inventory_file = r"C:/Users/Zemo/Documents/Python Tutorial/5th Week For Tutorial/Current_inventory.csv"
incoming_product_file = r"C:/Users/Zemo/Documents/Python Tutorial/5th Week For Tutorial/Incoming_product.csv"

#Read the current inventory and incoming product
current_inventory_df = pd.read_csv(current_inventory_file)
incoming_products_df = pd.read_csv(incoming_product_file)

#Find SKU on incoming products file that are not in current inventory
missing_products_df = incoming_products_df[~incoming_products_df['SKU'].isin(current_inventory_df['SKU'])]

#Generate file name for the new csv file
date_today = datetime.now().strftime("%Y-%m-%d")
output_filename = fr'C:\Users\Zemo\Documents\Python Tutorial\5th Week For Tutorial\Products_not_in_current_inventory_{date_today}.csv'


#Save the missing products to a new csv file
missing_products_df.to_csv(output_filename,index=False)

print(f"File '{output_filename}' saved! ")


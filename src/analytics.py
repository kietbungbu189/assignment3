#2.1 check if stock levels are above threshold
#required_stocklevel = 20 
#2.1.1 Method 1
#print(f"\nCHECK IF STOCK LEVELS ARE ABOVE THRESHOLD")
#stock_to_check = []
#for cell in df_data['Stock levels']:
#    if pd.notna(cell):
#        if int(float(cell)) < required_stocklevel:
#            print(f"Stock of {cell} is low, please reorder")
#            stock_to_check.append(cell)
#    else: 
#        print(f"data for {cell} is blank, please check database")

#2.1.2 Method 2
#low_stock = df_data[df_data['Stock levels']<required_stocklevel]
#print(low_stock.head())

def check_low_stock(table, stock_column):
    required_stocklevel = 20
    low_stock = table[stock_column]<=required_stocklevel
    return table[low_stock]
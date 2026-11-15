import pulp
import pandas as pd

def optimize(dim_supplier, restock_table):
    restock_dict = {}
    for SKU, qty in zip(restock_table['SKU'], restock_table['Quantity to order']):
        restock_dict[SKU] = qty
#matching/filtering step
# Method 1
#    to_order = []
#    dim_supplier_dict = {}
#    for SKU in restock_table['SKU']:
#print(my_series.values)
#        if SKU in dim_supplier['SKU'].values
#            to_order.append(SKU)
#To transition from your earlier set intersection (&) pattern to filtering your...
#...supplier table with .isin(demand_map.keys()), you shift from comparing... 
#...matching rows inside a single table to checking whether each... 
#...supplier row's SKU exists in your external restock dictionary
# Method 2
    to_order = set(restock_dict) & set(dim_supplier_dict)
#this is the same as the step converting DataFrame into dictionary above
#    id_movie=average_rating.loc[average_rating.rating==5.0].index
    dim_supplier.loc[dim_supplier.SKU.isin(to_order)].head()
#save to a variable
    filtered_supplier = dim_supplier.loc[dim_supplier.SKU.isin(to_order)]
import pulp
import pandas as pd

def optimize(dim_supplier_withSKU, restock_table):
#P1
    restock_dict = {}
    for SKU, qty in zip(restock_table['SKU'], restock_table['Quantity to order']):
        restock_dict[SKU] = qty
#matching/filtering step
# Method 1
#    to_order = []
#    for SKU in restock_table['SKU']:
#print(my_series.values)
#        if SKU in dim_supplier_withSKU['SKU'].values
#            to_order.append(SKU)
#To transition from your earlier set intersection (&) pattern to filtering your...
#...supplier table with .isin(demand_map.keys()), you shift from comparing... 
#...matching rows inside a single table to checking whether each... 
#...supplier row's SKU exists in your external restock dictionary
# Method 2
    to_order = set(restock_dict) & set(dim_supplier_withSKU['SKU'])
#this is the same as the step converting DataFrame into dictionary above
#    id_movie=average_rating.loc[average_rating.rating==5.0].index
    dim_supplier_withSKU.loc[dim_supplier_withSKU.SKU.isin(to_order)].head()
#save to a variable
    filtered_supplier = dim_supplier_withSKU.loc[dim_supplier_withSKU.SKU.isin(to_order)]

#P2 
    to_minimize_prob = pulp.LpProblem("Restock_Order", pulp.LpMinimize)
    
#P3
    order_qty_choices = {}
    user_supply_switches = {}
    for index, row_ in filtered_supplier.iterrows():
        order_qty_choices[index] = pulp.LpVariable(f"order_qty{index}", lowBound=0, cat="Integer")
        user_supply_switches[index] = pulp.LpVariable(f"supply_switch{index}", lowBound=0, cat="Binary")
    
#P4
    per_item_cost = {}
    for index, row_ in filtered_supplier.iterrows():
        per_item_cost[index] = (row_['Per-unit purchase cost'] + row_['Holding_Cost'])*order_qty_choices[index] + user_supply_switches[index]*row_['Shipping cost']    
#    print(my_series.values)
    per_item = pulp.lpSum(per_item_cost.values())
    to_minimize_prob += per_item
    
#P5
#for key, value in person.items():
#    print(key, "→", value)
    for key, value in restock_dict.items():
#        if filtered_supplier['SKU'] == key
#if statement is the right logic, just not used appropriately structure-wise
        filtered_for_restock.index = filtered_supplier['SKU'] == key
        filtered_for_restock = filtered_supplier[filtered_for_restock]
    return filtered_supplier

import pandas as pd
import numpy as np

def build_dim_supplier(raw):
    suppliers = (
        raw[["Supplier name", "Location"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )
    suppliers.insert(0, "Supplier index", suppliers.index)
    return suppliers

def build_dim_logistics(raw):
    logistics = raw[['Shipping carriers', 'Transportation modes', 'Routes']].drop_duplicates().reset_index(drop=True)
    logistics.insert(0, 'Logistics index', logistics.index)
    return logistics

def build_dim_product(raw):
    product = raw[['SKU', 'Product type', 'Price']].drop_duplicates().reset_index(drop=True)
    return product

def attach_keys(keep, drop, key):
    merge6 = pd.merge(keep, drop, how="left", on=key, validate="many_to_one")
    return merge6

def options(dim_product, dim_supplier, dim_logistics, options_per_sku=3, seed=8):
    ngaunhien = np.random.default_rng(seed)
    options_to_choose_rows = []
    for index, pdt in dim_product.iterrows():
#pick random choice of combination of 3 'available' suppliers/routes from... 
#...their existing pandas DataFrame, this is not using Numpy random yet         
        supplier_options = dim_supplier.sample(options_per_sku, replace=False, random_state=int(ngaunhien.integers(0, 2**32)))
        logistics_options = dim_logistics.sample(options_per_sku, replace=False, random_state=int(ngaunhien.integers(0, 2**32)))

#unpack suppliers_to_choose_from and routes_to_choose_from
#3.1 extract Aug 2025
#for column, index in zip(columns_names, target_column_position):
#    columns[column] = df_data.iloc[:,index]
#3.2 extract Oct 2026
#for column2, index2 in zip(columns_names2, target_column_position2):
#    columns2[column2] = df_data2.iloc[:,index2]

        for (supplier_index, supplier_option), (logistics_index, logistics_option) in zip(supplier_options.iterrows(), logistics_options.iterrows()):
            new_table = {}
            new_table['SKU'] = pdt['SKU']
            new_table['Base price'] = pdt['Price']
            n_rows = len(new_table)
            new_table['Per-unit purchase cost'] = ngaunhien.uniform(10.0, 50.0)
            new_table['Shipping cost'] = ngaunhien.uniform(2.0, 15.0)
            new_table['Minimum order quantity'] = ngaunhien.integers(10, 101)
            new_table['Max capacity'] = ngaunhien.integers(500, 5001)
            new_table['Supplier index'] = int(supplier_index)
            new_table['Logistics index'] = int(logistics_index)
            options_to_choose_rows.append(new_table)
        
        print(f"Row {index}: product {pdt['SKU']} has type {pdt['Product type']} and price {pdt['Price']}")
    return pd.DataFrame(options_to_choose_rows)
    
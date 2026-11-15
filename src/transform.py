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

def options(dim_product, dim_supplier, dim_logistics, seed=8):
    ngaunhien = np.random.default_rng(seed)
    options_to_choose_rows = []
    for index, pdt in dim_product.iterrows():
        new_table = {}
        new_table['SKU'] = pdt['SKU']
        new_table['Base price'] = pdt['Price']
#pick random choice of combination of 3 'available' suppliers/routes from... 
#...their existing pandas DataFrame, this is not using Numpy random yet         
        new_table['suppliers_to_choose_from'] = dim_supplier.choice(dim_supplier, 3, replace=False)
        new_table['routes_to_choose_from'] = dim_logistics.sample(dim_logistics, 3, replace=False)
        print(f"Row {index}: product {pdt['SKU']} has type {pdt['Product type']} and price {pdt['Price']}")
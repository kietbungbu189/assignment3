import pandas as pd

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
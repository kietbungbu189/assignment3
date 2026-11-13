from src.config import RAW_CSV
from src.extract import read_fact_csv
from src.transform import build_dim_supplier
from src.transform import build_dim_logistics
from src.transform import build_dim_product
from src.transform import attach_keys

def main():
    raw = read_fact_csv(RAW_CSV)
    suppliers = build_dim_supplier(raw)
    print(f"Raw rows: {len(raw)}")
    print(f"Supplier-location combinations: {len(suppliers)}")
    print(suppliers.head())

    logistics = build_dim_logistics(raw)
    print(f"Raw rows: {len(raw)}")
    print(f"Shipping carriers-Transportation modes-Routes combinations: {len(logistics)}")
    print(logistics.head())

    products = build_dim_product(raw)
    print(f"Raw rows: {len(raw)}")
    print(f"SKU records: {len(products)}")
    print(products.head())

    merge1 = attach_keys(raw, suppliers, ['Supplier name', 'Location'])
    merge2 = attach_keys(merge1, logistics, ['Shipping carriers', 'Transportation modes', 'Routes'])
    merge2 = merge2.drop(columns=['Supplier name', 'Location', 'Shipping carriers', 'Transportation modes', 'Routes', 'Product type', 'Price'])

if __name__ == "__main__":
    main()


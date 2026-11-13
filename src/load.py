from pathlib import Path
from src.config import DB
import sqlite3

def create_db(dim1, dim2, dim3, fact):
    datadir = Path(DB)
    datadir.parent.mkdir(parents=True, exist_ok=True)
    db_connect = sqlite3.connect(datadir)
    db_connect.execute("PRAGMA foreign_keys=ON")

    query_drop_facttable = 'DROP TABLE IF EXISTS supply_chain_datas'
    query4 = 'CREATE TABLE supply_chain_datas  (SKU VARCHAR(20), Availability INTEGER, "Number of products sold" INTEGER, "Revenue generated" REAL, "Customer demographics" VARCHAR(20), "Stock levels" INTEGER, "Lead times" REAL, "Order quantities" INTEGER, "Shipping times" REAL, "Shipping costs" REAL, "Lead time" REAL, "Production volumes" INTEGER, "Manufacturing lead time" REAL, "Manufacturing costs" REAL, "Inspection results" VARCHAR(20), "Defect rates" REAL, "Costs" REAL, "Supplier index" INTEGER, "Logistics index" INTEGER, FOREIGN KEY (SKU) REFERENCES products(SKU), FOREIGN KEY ("Supplier index") REFERENCES suppliers("Supplier index"), FOREIGN KEY ("Logistics index") REFERENCES logistics("Logistics index"))'
    query_drop = 'DROP TABLE IF EXISTS products'
    query = 'CREATE TABLE products (SKU VARCHAR(20) PRIMARY KEY, "Product type" VARCHAR(20), Price REAL);'
    query_drop2 = 'DROP TABLE IF EXISTS logistics'
    query2 = 'CREATE TABLE logistics ("Logistics index" INTEGER PRIMARY KEY, "Shipping carriers" VARCHAR(20), "Transportation modes" VARCHAR(20), Routes VARCHAR(20));'
    query_drop3 = 'DROP TABLE IF EXISTS suppliers'     
    query3 = 'CREATE TABLE suppliers ("Supplier index" INTEGER PRIMARY KEY, "Supplier name" VARCHAR(20), Location VARCHAR(20));'

    db_connect.execute(query_drop_facttable)
    db_connect.execute(query_drop)
    db_connect.execute(query)
    db_connect.execute(query_drop2)
    db_connect.execute(query2)
    db_connect.execute(query_drop3)
    db_connect.execute(query3)
    db_connect.execute(query4)


#load into db
#1 identify target
#done by config.py
#target_fileoraddress = "C:/Users/USER/Downloads/study docs/Comp604/assignment/assignment2/New Version/dim_Logistics.csv"

#2 open target
#done by extract.py
#with open(target_fileoraddress, mode="r") as response_or_file:
    #line_or_data = response_or_file.readline()
#response_or_file = pd.read_csv(target_fileoraddress)

#2.1 extract data and save into variable:
#done by transform.py
#oltp_product = pd.DataFrame({'Logistics index':response_or_file['Logistics index'], 'Shipping carriers':response_or_file['Shipping carriers'], 
#                             'Transportation modes':response_or_file['Transportation modes'], 'Routes':response_or_file['Routes']}) 

#3 load into sql:
#doing here, but instead of loading simultaneouly with creating tables as... 
#...below (creating done by python automatically), here tables are created manually first...
#...and the DataFrame from step 2.1 (which is from using function in transform.py as...
#...said above) is then saved to variable "raw" in main and loaded using function...
#...in load.py (which is here)
#connection1 = sqlite3.connect('database.db')
#oltp_product.to_sql('logistics', connection1)

    dim1.to_sql('products', db_connect, if_exists="append", index=False)
    dim2.to_sql('logistics', db_connect, if_exists="append", index=False)
    dim3.to_sql('suppliers', db_connect, if_exists="append", index=False)
    fact.to_sql('supply_chain_datas', db_connect, if_exists="append", index=False)

    db_connect.commit()
    db_connect.close()
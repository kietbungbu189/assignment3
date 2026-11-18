from src.config import WEBSITE
from src.extract import extract_website
from src.extract import scrape_books
from src.load import create_csv
import requests
from src.transform import parse_book
from src.config import OUTPUT_CSV
import pandas as pd
from src.log import log_analysis


def main():
    session_main = requests.Session()
#Dependency Injection    
    file_or_data_main = scrape_books(session_main, 1)
    print(file_or_data_main[:500])

    data_dict = parse_book(file_or_data_main)
    df = pd.DataFrame(data_dict)

    create_csv(df, OUTPUT_CSV)

    log_analysis(df)

if __name__ == "__main__":
    main()


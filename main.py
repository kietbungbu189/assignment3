from src.config import WEBSITE
from src.extract import extract_website
from src.extract import scrape_books
import requests


def main():
    session_main = requests.Session()
#Dependency Injection    
    file_or_data_main = scrape_books(session_main, 1)
    print(file_or_data_main[:500])

if __name__ == "__main__":
    main()


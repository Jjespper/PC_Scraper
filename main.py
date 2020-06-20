from scrapping import scrapping
from convert_dataframe import convert_dataframe
from load_sql import load_sql

def main():
    articles_list, categories_list, prices_list, stock_list =scrapping()
    dataset = convert_dataframe(articles_list, categories_list, prices_list, stock_list)
    load = load_sql(dataset)
    
if __name__ == "__main__":
    main()
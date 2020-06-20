import pandas as pd
import datetime

def convert_dataframe(articles_list, categories_list, prices_list, stock_list):
        
    data_tuples = list(zip(articles_list, categories_list, prices_list, stock_list))
    data = pd.DataFrame(data_tuples, columns=['Articulo','Categoria', 'Precio', 'Stock'])
    data['Precio'] = data['Precio'].astype(float)

    now = datetime.date.today()

    data['Fecha'] = now
    
    return data


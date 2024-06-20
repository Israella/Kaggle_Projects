import pandas as pd
import os
import numpy as np
import requests

# Lista de arquivos CSV
file_list = ["Challenge-ETL-DW\olist_customers_dataset.csv","Challenge-ETL-DW\olist_order_items_dataset.csv","Challenge-ETL-DW\olist_order_payments_dataset.csv",
             "Challenge-ETL-DW\olist_order_reviews_dataset.csv","Challenge-ETL-DW\olist_orders_dataset.csv","Challenge-ETL-DW\olist_products_dataset.csv"]

# Novos nomes para os arquivos CSV
file_name = ["CustomersData","ItemsData","PaymentsData","ReviewsData","OrdersData","ProductsData"]

# Atribuindo nomes aos DF
dataframes = {}
for file, name in zip(file_list, file_name):
    dataframes[name] = pd.read_csv(file)





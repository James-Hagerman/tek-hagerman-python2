import mysql.connector
# import MySQLdb
import pandas as pd
from app import rel_table
import csv
import sys
from sqlalchemy import create_engine
from flask_migrate import Migrate

db = mysql.connector.connect(    
    host = "localhost",
    user = "root",
    passwd = '1A2s3D4f5G6h7J8k9L0z1Z2x3C4v5B6n7M',
    database = 'adoption')


engine = create_engine('mysql+pymysql://root:1A2s3D4f5G6h7J8k9L0z1Z2x3C4v5B6n7M@localhost/adoption')

csv_data_puppies = pd.read_csv('puppies_data.csv')
csv_data_owners = pd.read_csv('owners_data.csv')

print(csv_data_puppies.head(20))
print(csv_data_owners.head(20))

csv_data_puppies.to_sql('puppies', con = engine, if_exists = 'append', index = False)
csv_data_owners.to_sql('owners', con = engine, if_exists = 'append', index = False)

# df_rel = pd.read_sql_table('rel_table', engine)
# print(df_rel)


# rel_df = pd.merge(df_rel, csv_data_owners, how = 'outer', left_on = 'owner_id', right_index = True)
# rel_df = rel_df.drop(['name', 'puppy_id'], axis = 1)
# print(rel_df)
# rel_df = pd.merge(rel_df, csv_data_puppies, how = 'left', right_index = True, left_on = 'pup_id')


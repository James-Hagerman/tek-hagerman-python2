import mysql.connector
# import MySQLdb
import pandas as pd
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




merging = pd.merge(csv_data_puppies, csv_data_owners, how = 'inner', on = 'pup_id')
# print(merging)
# flask_migrate = True 


# pd.merge(petdata, ownerdata, how = left, on ownerid)
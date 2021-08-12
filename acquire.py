import pandas as pd
import env
import os

def get_sql_url(database):
    return f'mysql+pymysql://{env.user}:{env.password}@{env.host}/{database}'

def get_titanic_data():
    file_name = 'titanic.csv'

    if os.path.isfile(file_name):
        return pd.read_csv(file_name)

    else:
        df = pd.read_sql('SELECT * FROM passengers', get_sql_url('titanic_db'))
        df.to_csv(file_name, index = False)
        
        return df

def get_iris_data():
    file_name = 'iris.csv'

    if os.path.isfile(file_name):
        return pd.read_csv(file_name)
    else:
        df = pd.read_sql('SELECT * FROM measurements JOIN species ON species.species_id = measurements.species_id', get_sql_url('iris_db'))
        df.to_csv(file_name, index=False)

        return df

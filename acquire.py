# Acquire Telecommunications Data

import os
import pandas as pd
import env

def get_connection(db, user=env.user, host=env.host, password=env.password):
    '''
    Returns a formatted url to access a SQL database.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

    
def get_telco_data():
    '''
    Returns Telecommunication Data
    '''
    file = 'telco_data.csv'

    if os.path.isfile(file):
        return pd.read_csv('telco_data.csv')
    else:
        df = pd.read_sql("""
                        select *
                        from customers
                        join internet_service_types using(internet_service_type_id)
                        join contract_types using(contract_type_id)
                        join payment_types using(payment_type_id);
                        """,
                        get_connection('telco_churn')
                        )
        
        df.to_csv('telco_data.csv', index=False)
        return df


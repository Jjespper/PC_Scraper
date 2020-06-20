from sqlalchemy import create_engine
from configparser import ConfigParser

def load_sql(data):

    config = ConfigParser()
    config.read('/home/jacobo/Config/database.ini')
    user = config['MYSQL']['user']
    password = config['MYSQL']['password']
    ip = config['MYSQL']['ip']
    port = config['MYSQL']['port']
    database = config['MYSQL']['database']
    con = create_engine('mysql://'+user+':'+password+'@'+ip+':'+port+'/'+database)
    data.to_sql(con=con, name='TABLA_DE_PRUEBA', if_exists='append', index=False)
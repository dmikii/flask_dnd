import warnings
warnings.simplefilter(action='ignore')
import pandas as pd
csv = "monsters_alt.csv"
df = pd.read_csv(csv)

from sqlalchemy import create_engine
conn_string = 'postgresql:///monsters_db'

conn = create_engine(conn_string)
df.to_sql('monsters', conn, if_exists='replace')

def test_method():
    pass
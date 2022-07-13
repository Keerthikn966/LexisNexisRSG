# Import libraries
import pandas as pd
import psycopg2
from config.config import config

# Connect to PostgreSQL
params = config(config_db='database.ini')

try:
    con = psycopg2.connect(**params)
    # Read the table
    cur = con.cursor()
    cur.execute("""SELECT * FROM cms.blogs;""")
    # published_blogs
    df = pd.read_sql("select * from cms.Blogs where Published_on is not null", con)
    con.commit()
    for i, g in df.groupby('author'):
        g.to_csv('{}-published-blogs.csv'.format(i.split('/')[0]), index=False)
    con.commit()
    #drafted_blogs
    df = pd.read_sql("select * from cms.Blogs where Published_on is  null", con)
    for i, g in df.groupby('author'):
        g.to_csv('{}-drafted-blogs.csv'.format(i.split('/')[0]), index=False)
    con.commit()

except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if con is not None:
        con.close()



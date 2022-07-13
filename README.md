Python and Database challenge

This is collection of script files that connect to postgresql and creates the table 'Blogs' in specified schema 'CMS'
and use python to query the database and export the data into multiple CSV files

The psycopg2 is the postgresql connector used to connect to python.

database.ini has database configuration file like hostname, db name,username, password and port.

To parse the information from the database.ini , config.py is created. 

createtable.py contains python code which connects to postgresql, creates the table and inserts the data into the table

db_conn.py contains code written that will load the table that fits with our input (config_db and query) 

main.py has skeleton code that test the postgresql connection via python and pythonpostgresql_multiplefiles.py has the logic that queries te database and writes to files


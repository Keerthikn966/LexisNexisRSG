# Import libraries
import pandas as pd
import psycopg2
from config.config import config

# Connect to PostgreSQL
params = config(config_db='database.ini')
con = psycopg2.connect(**params)
print('Python connected to PostgreSQL!')
# Create table
cur = con.cursor()
cur.execute("""
CREATE TABLE cms.Blogs(
id INT NOT NULL,
  Author varchar(200) not null,
  Published_on date,
  Blog_Text text,
  Created_On date);
""")
print('Table created in PostgreSQL')

# Insert values to the table

cur.execute("""
insert into cms.blogs (id,Author,Published_on,Blog_Text,Created_On) values
(111,'Jennifer Thomas','2022-01-05','Cloud Storage in a minute-Managing file storage for applications can be complex, but it doesn’t have to be. In this episode of Cloud Bytes, we show you how Cloud Storage allows enterprises and developers alike to store and access their data seamlessly without compromising security or hindering scalability. Watch to learn how Cloud Storage can help you store your applications data at an enterprise level','2022-01-01'),
(111,'Jennifer Thomas',null,'Big Query in a minute-Storing and querying massive datasets can be time consuming and expensive without the right infrastructure. In this episode of Cloud Bytes, we give you an overview of BigQuery, Googles fully-managed data warehouse. Watch to learn how to ingest, store, analyze, and visualize big data with ease!','2022-02-03'),
(222,'Joanna Smith','2022-02-05','Google Kubernetes Engine in a minute-Google Kubernetes Engine (GKE) - an enterprise-grade platform that is useful for containerized applications. Watch to learn how GKE can increase developer productivity, simplify platform operations, and provide greater observability for vulnerabilities for data and containers alike. ','2022-02-23'),
(222,'Joanna Smith',null,'Compute Engine in a minute-Google Compute Engine (GCE) is an infrastructure as a service (IaaS) offering that allows clients to run workloads on Google''s physical hardware.Google Compute Engine provides a scalable number of virtual machines (VMs) to serve as large compute clusters for that purpose. GCE can be managed through a RESTful application program interface (API), command line interface or web console. Compute Engine pricing is on a pay-per-usage basis with a one minute minimum, charged on a per-second basis.','2022-03-12'),
(333,'Priyanka Vergadia','2022-03-27','what is app Enginee-App Engine is a fully managed, serverless platform for developing and hosting web applications at scale. You can choose from several popular languages, libraries, and frameworks to develop your apps, and then let App Engine take care of provisioning servers and scaling your app instances based on demand','2022-04-04'),
(444,'Data pilot',null,'what is cloud spanner-Google Cloud Spanner is a distributed relational database service that runs on Google Cloud. It is designed to support global online transaction processing deployments, SQL semantics, highly available horizontal scaling and transactional consistency.','2022-05-24');
""")

print('Values inserted to PostgreSQL')

# Close the connection
con.commit()
con.close()

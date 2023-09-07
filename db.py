from sqlalchemy import create_engine

# Replace the values below with your MySQL database credentials
username ="root"
password = "root"
host = "localhost"
database = "point"
port = "8889"

# Create the connection URL with the MySQL driver
url = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'

# Create the engine with the connection URL
engine = create_engine(url)

# Use the engine to perform database operations
# For example, you can execute SQL queries using the `engine.execute()` method
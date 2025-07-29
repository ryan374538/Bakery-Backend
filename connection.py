from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

username = "root"
password = "2480"
database = "order_db"

# Change the driver and dialect to PostgreSQL
path = f"postgresql+psycopg2://{username}:{password}@localhost/{database}"

data = create_engine(path)

Session = sessionmaker(bind=data)

session = Session()

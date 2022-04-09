#step 1: create engine for sql-alchemy
from sqlalchemy import create_engine
#for step2
from sqlalchemy.ext.declarative import declarative_base
#for step3
from sqlalchemy.orm import sessionmaker

SQL_DATABASE_URL = "sqlite:///./transactions.db"    #create url for local database
engine = create_engine(SQL_DATABASE_URL,connect_args={"check_same_thread":False})   #creating engine for database

#step2 create base
base = declarative_base()

#create a session of database
SESSION = sessionmaker(autocommit=False,autoflush=False,bind=engine)
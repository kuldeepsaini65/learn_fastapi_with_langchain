from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQL_ALCHEMY_DATABASE_URL = "mysql://root:@localhost:3306/fastapi_learn"

SQL_DATABASE_URL = "mysql://root:@localhost:3306/fastapi_learn"

'''
echo -> echo in SQLAlchemy prints all generated SQL queries to the console. It is mainly used for debugging and logging during development. It is optional and not mandatory unless query-level logging is required. 
it does basic SQL logging, but it is not a proper logging system.
'''
engine = create_engine(url = SQL_DATABASE_URL)


sessionLocal = sessionmaker(bind = engine, autoflush=False, autocommit = False)

Base = declarative_base()






"""
.. module:: database
   :synopsis: Connects to the database and creates content table under the Content database

.. moduleauthor:: Sebastian Schwindt <github.com/sschwindt>


"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

# Connect to mysql database
engine = create_engine('mysql://root:password@localhost/Content', convert_unicode=True)
metadata = MetaData()

# db_session, used for persistence operation (connection) to the database
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

# initialize database (create table)
def init_db():
    """
        **Initialize Database**

        This creates a content table under the Content database.

    """
    import newAPI.models
    metadata.create_all(bind=engine)

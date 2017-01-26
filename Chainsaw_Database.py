from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Contestant(Base):
    """Creates a record for each Contestant"""

    __tablename__ = "Record_Holders"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    country = Column(String)
    catches = Column(Integer)

    def __repr__(arg):
        ''' String for testing purposes '''
        
        return 'Contestant: id = {} name = {} country = {} catches = {}'.format(self.id, self.name, self.country, self.catches)

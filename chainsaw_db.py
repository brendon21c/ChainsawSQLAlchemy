from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from base import Base

class Contestant(Base):
    """Creates a record for each Contestant"""

    __tablename__ = "Record_Holders"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    country = Column(String)
    catches = Column(Integer)

    def __repr__(self):
        ''' String for testing purposes '''

        return 'Contestant: id = {} name = {} country = {} catches = {}'.format(self.id, self.name, self.country, self.catches)

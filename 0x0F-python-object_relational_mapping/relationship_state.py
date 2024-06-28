# relationship_state.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base
from relationship_city import City

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state", cascade="all, delete-orphan")

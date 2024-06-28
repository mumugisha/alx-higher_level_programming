# relationship city

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from base import Base


class City(Base):
    __tablename__ = 'cities'

    id = Column(
        Integer, primary_key=True, autoincrement=True, nullable=False
    )
    name = Column(String(128), nullable=False)
    state_id = Column(
        Integer, ForeignKey('states.id', ondelete='CASCADE'),
        nullable=False
    )
    state = relationship("State", back_populates="cities")

from sqlalchemy import Column, Integer, String
from .database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    user_email = Column(String)
    description = Column(String, nullable=True)
from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False, index=True)
    image_url = Column(String, nullable=False, default="")
    tag = Column(String, nullable=False, default="")
    weight = Column(String, nullable=False, default="")
    price = Column(Float, nullable=False, default=0.0)
    rating = Column(Float, nullable=False, default=0.0)
    old_price = Column(Float, nullable=True)

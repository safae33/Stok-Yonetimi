from app.db.base_class import Base
from .product import *
from ...auth.models.user import UserBasic

from sqlalchemy import Column, Integer, String, SMALLINT, ForeignKey, BOOLEAN, Table, DateTime, Float
from sqlalchemy.orm import relationship


class Stock(Base):
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'))

    import_unit_price = Column(Integer)
    money_type = Column(String(5))
    for_sell = Column(BOOLEAN, default=False)
    sell_unit_price = Column(Float)
    sell_unit_quantity = Column(Integer)


class Transaction(Base):
    id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey('stock.id'))
    from_id = Column(Integer, ForeignKey('userbasic.id'))
    to_id = Column(Integer, ForeignKey('userbasic.id'))
    user = Column(Integer, ForeignKey('userbasic.id'))

    date_ = Column(DateTime)
    is_create_transaction = Column(BOOLEAN, default=False)    
    quantity = Column(Integer)
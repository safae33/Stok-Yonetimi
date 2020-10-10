"""
Categories, Product, Img_Url
"""
from app.db.base_class import Base

from sqlalchemy import Column, Integer, String, SMALLINT, ForeignKey, BOOLEAN, Table, DateTime
from sqlalchemy.orm import relationship


class Category(Base):
    """
    Ürün kategorilerine ait model
    """
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    detail = Column(String(150))
    isFav = Column(BOOLEAN, nullable=False)
    parent_cat = Column(Integer, ForeignKey('category.id'))

    child_cats = relationship("Category", backref="category")


class Product(Base):
    """
    Ürün modeli
    """
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    public_id = Column(String(20))
    main_url = Column(String(100))

    img_urls = relationship('Img_Url', cascade="all,delete",
                            backref='product')
    value = relationship('Product_Spec_Value', cascade="all,delete",
                         backref='product', uselist=False)


class Img_Url(Base):
    """
    Ürüne ait resimlerin url'lerinin tutulacağı model
    """
    id = Column(Integer, primary_key=True)
    prod_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    url = Column(String(100), nullable=False)


class Product_Spec_Type(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    values = relationship("Product_Spec_Value", cascade="all,delete",
                          backref="product_spec_type")


class Product_Spec_Value(Base):
    id = Column(Integer, primary_key=True)
    unit = Column(Integer, ForeignKey("unit.id"))
    product_spec_id = Column(Integer, ForeignKey(
        'product_spec_type.id'), nullable=False)
    product_id = Column(Integer, ForeignKey(
        'product.id'), nullable=False)

    valueDate = relationship(
        "Value_Date", backref="product_spec_value", uselist=False)
    valueString = relationship(
        "Value_String", backref="product_spec_value", uselist=False)
    valueInteger = relationship(
        "Value_Integer", backref="product_spec_value", uselist=False)
    valueSmallint = relationship(
        "Value_Smallint", backref="product_spec_value", uselist=False)


class Unit(Base):
    id = Column(Integer, primary_key=True)
    unit_id = Column(SMALLINT)


class Value_Date(Base):
    id = Column(Integer, primary_key=True)
    parentId = Column(Integer, ForeignKey("product_spec_value.id"))
    value = Column(DateTime, nullable=False)


class Value_String(Base):
    id = Column(Integer, primary_key=True)
    parentId = Column(Integer, ForeignKey("product_spec_value.id"))
    value = Column(String(500), nullable=False)


class Value_Integer(Base):
    id = Column(Integer, primary_key=True)
    parentId = Column(Integer, ForeignKey("product_spec_value.id"))
    value = Column(Integer, nullable=False)


class Value_Smallint(Base):
    id = Column(Integer, primary_key=True)
    parentId = Column(Integer, ForeignKey("product_spec_value.id"))
    value = Column(SMALLINT, nullable=False)


product_category = Table('product_category',
                         Base.metadata,
                         Column('product_id', Integer, ForeignKey(
                             'product.id'), primary_key=True),
                         Column('category_id', Integer, ForeignKey('category.id'), primary_key=True))

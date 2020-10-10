"""
UserBasic, UserDetails
"""
from app.db.base_class import Base

from sqlalchemy import Column, Integer, String, SMALLINT, ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash


class UserBasic(Base):
    id = Column(Integer, primary_key=True)
    mail = Column(String(50), nullable=False, unique=True)
    pw_hash = Column(String(128), nullable=False)
    type_ = Column(SMALLINT, nullable=False)

    details = relationship('UserDetails', cascade="all,delete",
                           backref='userbasic', uselist=False)  # one-to-many dden farklı
    # olarak yalnızca uselist=False ekleniyor relationship e o kadar. çohyi.


class UserDetails(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('userbasic.id'), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    # one-to-one ilişki için gerekli durum bu 2 tabloddaki
    title = Column(String(50), nullable=False)

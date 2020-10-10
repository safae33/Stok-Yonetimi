from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from fastapi import Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from ..db_funcs import get_db

from app.db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)


class CRUDBase(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        """
        self.model = model


    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        """
        Temel get işleri. Hangi modelden çağrıldıysa id yollanıp belirli şey alınır.
        """
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(
        self, db: Session,  skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        """
        Çalışıyor
        """
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session,  obj) -> ModelType:
        """
        Çalışıyor
        """
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    # def update(
    #     self, 
    #     db: Session,
    #     *,
    #     db_obj: ModelType,
    # ) -> ModelType:
    #     """
    #     buna bakmadım sıkıldm.
    #     """
    #     if isinstance(obj_in, dict):
    #         update_data = obj_in
    #     else:
    #         update_data = obj_in.dict(exclude_unset=True)
    #     for field in obj_data:
    #         if field in update_data:
    #             setattr(db_obj, field, update_data[field])
    #     db.add(db_obj)
    #     db.commit()
    #     db.refresh(db_obj)
    #     return db_obj

    def remove(self, db: Session, id: int) -> ModelType:
        """
        CASCADE SİLMEK İSTENİYORSA;

        X-TO-ONE SIKINTISIZ OLUYOR

        X-TO-MANY İÇİN MODEL USELİST=TRUE VE MODEL SCHEMASINDA NESTED ALAN MANY=TRUE OLCAK.
        """
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj

from fastapi import APIRouter, requests, Depends
from sqlalchemy.orm import Session

from app.db.db_funcs import get_db


wms = APIRouter()


@wms.get('/test')
def login(db: Session = Depends(get_db)):
    """
    test için bir route
    """
    return {"result": "success",
            "data": [1, 2, 3]}


@wms.get('/getMinimalProducts')
def getMinimalProducts(db: Session = Depends(get_db)):
    """
    tüm ürünlerin detaysız bilgilerini döndüren route
    """

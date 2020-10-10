from app.db.crud.base import CRUDBase
from ..models import UserBasic

class CRUDUser(CRUDBase[UserBasic]):
    pass
    
userBasic = CRUDUser(UserBasic)
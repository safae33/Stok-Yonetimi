from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash, check_password_hash

from app.db.db_funcs import get_db
from .schemas import UserBasicSchema
from .models import UserBasic, UserDetails, UserBasicMa
from .crud.crud_user_basic import userBasic

auth = APIRouter()


@auth.get('/login')
def login(userBasicRequest: UserBasicSchema, db: Session = Depends(get_db)):
    """
    giriş metodu. mail ve şifre bilgileri eşleşirse token return edecek.
    daha sonraki request'ler bu token ile yapılacak.
    """
    user = UserBasic()
    user.mail = userBasicRequest.mail
    user.pw_hash = generate_password_hash(userBasicRequest.passwd)
    user.type_ = 1
    db.add(user)
    db.commit()
    db.refresh(user)

    return {"result": user,
            "data": [1, 2, 3]}

@auth.get('/login1')
def login(userBasicRequest: UserBasicSchema, db: Session = Depends(get_db)):
    """
    giriş metodu. mail ve şifre bilgileri eşleşirse token return edecek.
    daha sonraki request'ler bu token ile yapılacak.
    """
    user = UserDetails()
    user.user_id = 3
    user.first_name = "safa"
    user.last_name = "yıldırım"
    user.title = "kıraaal"
    db.add(user)
    db.commit()
    db.refresh(user)

    return {"result": user,
            "data": [1, 2, 3]}

@auth.get('/login2')
def login(userBasicRequest: UserBasicSchema, db: Session = Depends(get_db)):
    """
    giriş metodu. mail ve şifre bilgileri eşleşirse token return edecek.
    daha sonraki request'ler bu token ile yapılacak.
    """
    user = db.query(UserBasic).filter(UserBasic.id==3).first()
    userMa = UserBasicMa(exclude=("pw_hash",))
    output = userMa.dump(user)

    return {"result": output}
            

@auth.get('/login3')
def login(userBasicRequest: UserBasicSchema, db: Session = Depends(get_db)):
    """
    giriş metodu. mail ve şifre bilgileri eşleşirse token return edecek.
    daha sonraki request'ler bu token ile yapılacak.
    """
    user = userBasic.remove(db, 3)
    userMa = UserBasicMa(exclude=("pw_hash",))
    output = userMa.dump(user)

    return {"result": output}
            

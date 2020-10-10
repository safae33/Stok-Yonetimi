from ..user import *

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

class UserDetailsSchema(SQLAlchemyAutoSchema):
    """
    SqlAlchemy modellerini direkt json olarak almamızı sağlayan bir araç marshmallow. Test ettim. gayet güzel işime
    yarar bir arkdaş. hatta bayıldım.
    """
    class Meta:
        model = UserDetails
        include_relationships = True
        load_instance = True


class UserBasicMa(SQLAlchemyAutoSchema):
    """
    SqlAlchemy modellerini direkt json olarak almamızı sağlayan bir araç marshmallow. Test ettim. gayet güzel işime
    yarar bir arkdaş. hatta bayıldım.
    """
    class Meta:
        model = UserBasic
        include_fk = True
        load_instance = True
    details = Nested(UserDetailsSchema, many=True, exclude=("userbasic",))


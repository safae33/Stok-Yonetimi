from pydantic import BaseModel

class UserBasicSchema(BaseModel):
     mail: str
     passwd: str
from pydantic import BaseModel
from typing import Optional

class SignUpModel(BaseModel):    
    id:Optional[int] = None
    username:str
    email:str
    password:str
    is_staff:Optional[bool]
    is_active:Optional[bool]

    class Config:
        from_attributes=True
        json_schema_extra={
            'example': {
                'username': 'JohnDoe',
                'email': 'email@email.com',
                'password': 'password',
                'is_staff': False,
                'is_active': True
            }
        }
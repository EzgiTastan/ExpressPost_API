from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional
from typing_extensions import Annotated


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

#PostCreate is the same with PostBase
class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class Post(PostBase):
    id: int
    # no need to write these due to inheritance:
    # title: str
    # content: str
    # published: bool
    created_at: datetime
    owner_id : int
    owner: UserOut

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    #direction of the vote:
    dir: Annotated[int, Field(le=1)]
    #anything less than 1 will be allowed.    
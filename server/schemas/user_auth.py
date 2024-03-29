from pydantic import BaseModel
from server.schemas.user import UserSchema


class JWTPayload(BaseModel):
    id: str
    uuid: str
    exp: int
    iat: int


class UserAuthSchema(BaseModel):
    id: str
    method: str
    oauth_id: str
    user_id: int
    user: UserSchema

    class Config:
        orm_mode = True

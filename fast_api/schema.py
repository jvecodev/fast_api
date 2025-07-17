from pydantic import BaseModel, EmailStr


# Base modal é a classe que define a estrutura dos dados que serão recebidos ou enviados
class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    name: str
    email: EmailStr
    id: int


class UserDB(UserSchema):
    id: int

# Schema de resposta para lista de usuários
class UserList(BaseModel):
    users: list[UserPublic]

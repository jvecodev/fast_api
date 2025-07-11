from pydantic import BaseModel

# Base modal é a classe que define a estrutura dos dados que serão recebidos ou enviado pela
class Message(BaseModel):
    message: str
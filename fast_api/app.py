from fastapi import FastAPI, HTTPException
from http import HTTPStatus
from fast_api.schema import Message, UserSchema, UserPublic, UserDB, UserList

app = FastAPI( title='FastAPI Example',)

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello World'}


@app.get('/second/', status_code=HTTPStatus.OK, response_model=Message)
def second_funcion():
    return {'message': 'Hello World 2'}


@app.post('/user/', status_code=HTTPStatus.CREATED, response_model=UserPublic)  
def create_user(user: UserSchema):
    user_db = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_db)
    return user_db


@app.get('/user/', response_model=UserList)
def get_users():
    return {'users': database}

@app.put('/user/{user_id}', response_model=UserPublic)
# Atualiza pelo ID, criando uma variável na URL
def update_user(user_id: int, user: UserSchema):
    user_db = UserDB(**user.model_dump(), id=user_id)

    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            #Not found == 404
            status_code = HTTPStatus.NOT_FOUND,
            detail = 'Fala aí doidão, usuário não encontrado!'
        )

    '''
     Verifica se o usuário existe, equivalente ao Select no SQL
     Estamos usando o - 1 para ajustar o índice, já que o ID começa em 1
    '''

    database[ user_id - 1] = user_db

    return user_db

@app.delete('/user/{user_id}',response_model=UserPublic, status_code=HTTPStatus.OK)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Fala aí doidão, usuário não encontrado!'
        )
    
    return database.pop(user_id - 1)
    
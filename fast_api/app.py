from fastapi import FastAPI
from http import HTTPStatus
from fast_api.schema import Message  

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message) 


def read_root():
    return {'message': 'Hello World'}  

@app.get('/second', status_code=HTTPStatus.OK, response_model=Message) 


def second_funcion():
    return {'message': 'Hello World 2'}  



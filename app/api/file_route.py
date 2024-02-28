from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from app.schemas.FileSchema import FileSchema, AlterFileSchema,SearchFileSchema, DeleteFileSchema
from app.controllers.file_controller import create_file, edit_file,search_file, delete_file,is_valid_type_extension
from app.database import SessionLocal
from typing import Annotated
from fastapi import UploadFile, Form, File, Body
import json

file_routes = APIRouter(prefix='/files')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
db = SessionLocal()

@file_routes.post('/create')
async def create_file_route(data: FileSchema , token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        # Valida se o tipo de extensão do arquvio e permitido.
        is_valid_type_extension(data.file_type)
        # Cria o arquivo e registra ele no banco de dados.
        create_file(db,data)
    except Exception as e:
       if str(e) == "File type not accept.":
        raise HTTPException(406,detail=str(e))
       elif str(e) == "File not found.":
        raise HTTPException(404,detail=str(e))
       elif str(e) == "Error in alter file in Database.":
        raise HTTPException(500,detail=str(e))

    return {'status': 'ok'}


@file_routes.post('/search')
async def search_file_route(data: SearchFileSchema):
    result = None
    try:
       result = search_file(db,data)
    except Exception as e:
       raise HTTPException(404,detail=str(e))
    
    
    return result

@file_routes.post('/edit')
async def edit_file_route(data: AlterFileSchema, token: Annotated[str, Depends(oauth2_scheme)]):
    edit_file(db, data)
 
    return "OK"


@file_routes.post('/delete')
async def delete_file_route(data:DeleteFileSchema, token: Annotated[str, Depends(oauth2_scheme)]):
   try:
      delete_file(db, data)
   except Exception as e:
       if str(e) == "File not exists":
        raise HTTPException(404,detail=str(e))
       elif str(e) == "Error delete file":
        raise HTTPException(500,detail=str(e))
      

   return {'status': 'ok'}

import base64, magic, uuid
from os import path, mkdir, remove, rename
from sqlalchemy.orm import Session
from app.models.FileModel import File
from app.schemas.FileSchema import FileSchema, AlterFileSchema, SearchFileSchema, DeleteFileSchema

DEFAULT_PATH = './app/data/'
TYPE_EXTENSIONS_ACCEPTS = ['gif', 'jpeg', 'webp', 'png']


def create_file(db: Session,  data: FileSchema):
    # Validate if has a folder.
    user_folder_path = path.join(DEFAULT_PATH, str(data.id_user))
    
    if not path.exists(user_folder_path):
        mkdir(user_folder_path) 


    url_file = path.join(user_folder_path, f"{data.file_name}")

    if db.query(File).filter_by(file_url = f"{url_file}.{data.file_type}").first() is not None:
        url_file = f"{url_file}_{uuid.uuid4()}"
    
    # the file type is added after searching the database so you can add it
    # at the end without needing to use more processing.
    data.file_url = f"{url_file}.{data.file_type}"

    # Validade if file type is image using magic numbers.
    file_data = base64.b64decode(data.file)

    # Types of images aceppets
    types_accepts = ['image/jpg', 'image/jpeg', 'image/png', 'image/gif', 'image/webp']

    if magic.from_buffer(file_data, mime=True) not in types_accepts:
        return 'ERROR' 
    
    # Write file to disk
    with open(data.file_url, 'wb') as img:
        img.write(file_data)

    # Create database record
    file_db  = File(
        id_user=data.id_user,
        file_name=data.file_name,
        file_type=data.file_type,
        file_description=data.file_description,
        file_size=data.file_size,
        file_hash=data.file_hash,
        public=data.public,
        file_url=data.file_url,
    )

    try:
        db.add(file_db)
        db.commit()
    except Exception as e:
        db.rollback()
        print('error')
        raise Exception ({
            "menssage":"Error in create file in Database.",
            "error": str(e)
        })
        

    return 'OK' 


def edit_file(db: Session,  data: AlterFileSchema):

    file_db =  db.query(File).filter_by(id = data.id).first() 
    if(file_db is None):
        raise Exception ("File not found.")
    
    new_url = None
    
    if data.file_name is not None and file_db.file_name != data.file_name:
        if data.file_type is not None and file_db.file_type != data.file_type:
            new_url = f"{DEFAULT_PATH}{file_db.id_user}/{data.file_name}.{data.file_type}"
            rename(file_db.file_url, new_url)
        else:
            new_url = f"{DEFAULT_PATH}{file_db.id_user}/{data.file_name}.{file_db.file_type}"
            rename(file_db.file_url, new_url)


    if new_url is None and data.file_type is not None and file_db.file_type != data.file_type:
        new_url = f"{DEFAULT_PATH}{file_db.id_user}/{file_db.file_name}.{data.file_type}"
        rename(file_db.file_url, new_url)


    try:
        db.query(File).filter_by(id = file_db.id).update({
            File.file_name: data.file_name or file_db.file_name,
            File.file_url: new_url or file_db.file_url,
            File.file_description: data.file_description or file_db.file_description,
            File.file_type: data.file_type or file_db.file_type,
            File.public: data.public if data.public != None else file_db.public
        })
    except Exception as e:
        db.rollback()
        raise Exception ("Error in alter file in Database.")
    else:
        db.commit()

    return "OK"


def search_file(db: Session, data: SearchFileSchema):
    
    result = None
    try:
        match data.type_search: 
            case "id_user":
               result = db.query(File).filter_by(id_user=data.id_user).all()
            case "file_name":
               result = db.query(File).filter_by(file_name=data.file_name).all()
            case "file_description":
               result = db.query(File).filter_by(file_description=data.file_description).all()
            case "id_file":
               result = db.query(File).filter_by(id=data.id_file).all()
            case _:
                raise(Exception("the type search parameter is missing or wrong."))   
    except:
        raise Exception("Failed to fetch files")


    return result


def delete_file(db: Session, data: DeleteFileSchema):
    file = db.query(File).filter_by(id=data.id).first()
    if file is None:
          raise Exception("File not exists")
    
    file_url = file.file_url
    try:
        db.delete(file)
        db.commit()
        remove(file_url)
    except:
        raise Exception("Error delete file")
    
    return "OK"


def is_valid_type_extension(file_content_type):
    if(not file_content_type in TYPE_EXTENSIONS_ACCEPTS):
        raise Exception ("File type not accept.")
    
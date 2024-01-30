from pydantic import BaseModel
from fastapi import UploadFile



class FileSchema(BaseModel):
    id:               int   | None
    id_user:          int   | None
    file_url:         str   | None
    file_name:        str   | None
    file_description: str   | None
    file_type:        str   | None
    file_hash:        str   | None
    file_size:        float | None
    file:             str   | None
    public:           bool  | None

class AlterFileSchema(BaseModel):
    id:               int   | None
    file_name:        str   | None
    file_description: str   | None
    file_type:        str   | None
    public:           bool  | None

class DeleteFileSchema(BaseModel):
    id:               int   | None
    token:            str   | None


class SearchFileSchema(BaseModel):
    type_search:      str   | None
    id_file:          int   | None
    id_user:          int   | None
    file_name:        str   | None
    file_description: str   | None
    skip:             int   | None
    limit:            int   | None
    token:            str   | None
    
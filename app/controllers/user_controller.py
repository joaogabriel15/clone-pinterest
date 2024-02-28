from sqlalchemy.orm import Session
from app.models.UserModel import User
from app.schemas.UserSchema import UserSchema, LoginSchema
from app.utils.auth import get_password_hash


def create_user(db: Session,  user: User):
    if(not db.query(User).filter_by(email = user.email).first() == None):
        return "Email já cadastrado!"

    try:
        user.hashed_password = get_password_hash(user.hashed_password)
        db.add(user)
    except:
        db.rollback()
        return False
    else:
        db.commit()
        
    return True


def get_users(db: Session, data:UserSchema):
    result_dicts = []
    try:
        result = db.query(User.id, User.name, User.email, User.birth, User.is_active).filter(
                (User.id == data.id)|
                (User.name.ilike(f'%{data.name}%'))|
                (User.email.like(f'%{data.email}%'))|
                (User.birth == data.birth)|
                (User.is_active ==data.is_active)
                ).all() 
        
        keys = ['id', 'name', 'email', 'birth', 'is_active']
        result_dicts = [dict(zip(keys, values)) for values in result]

    except:
        raise Exception("Failed to fetch files")


    return result_dicts

def get_user(db: Session, data:LoginSchema):
    result = None
    result = db.query(User).filter((User.id==data.id) | (User.email==data.email)).first()
    """   try:
        result = db.query(User).filter_by(id=data.id).first()
    except:
        raise Exception("Failed to fetch user") """

    return result

def alter_user(db: Session, user: User):
    return db.query(User).filter_by(id = user.id).update(user)

def delete_user(db: Session, user_id: int):
    return db.query(User).filter_by(id = user_id).delete()
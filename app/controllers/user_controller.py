from sqlalchemy.orm import Session
from app.models.UserModel import User
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

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session):
    return db.query(User).all()

def alter_user(db: Session, user: User):
    return db.query(User).filter_by(id = user.id).update(user)

def delete_user(db: Session, user_id: int):
    return db.query(User).filter_by(id = user_id).delete()
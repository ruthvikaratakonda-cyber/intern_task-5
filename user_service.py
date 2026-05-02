from app.schemas.user_schema import UserCreate

fake_db = []

def create_user(user: UserCreate):
    user_data = user.dict()
    fake_db.append(user_data)
    return {"message": "User created", "user": user_data}
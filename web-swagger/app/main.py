from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from .models import User, SessionLocal, UserToken
import uuid


tags_metadata = [
    {
        'name': 'users',
        'description': 'Operations for administering user accounts'
    },
    {
        'name': 'auth',
        'description': 'API endpoints for tokens'
    },
    {
        'name': 'flag',
        'description': 'Requires token authorisation from a logged in user.'
    }
]

app = FastAPI(
    title="Administration Portal",
    description='Administrating access to our apps API',
    version="0.0.1-beta",
    openapi_tags=tags_metadata
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    raise HTTPException(status_code=400, detail="Invalid API endpoint, please refer to documentation")


@app.post("/api/admin/users/create", tags=['users'])
def create_user(username: str, name: str, email: str, password: str, db: Session = Depends(get_db)):
    user = User(
        username=username,
        name=name,
        email=email
    )
    user.set_password(password)

    db.add(user)
    db.commit()
    db.refresh(user)

    return {"message": f"User: '{username}' created successfully."}


@app.post("/api/admin/users/delete", tags=['users'])
def delete_user(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"message": f"User: '{username}' deleted successfully."}


@app.get("/api/admin/users/list", tags=['users'])
def list_user(db: Session = Depends(get_db)):
    users = db.query(User).limit(100).all()

    users_list = []
    for user in users:
        users_list.append({
            'username': user.username,
            'name': user.name,
            'email': user.email
        })

    return {"users": users_list}


@app.post("/api/auth/login", tags=['auth'])
def login_user(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return HTTPException(status_code=401, detail="Invalid credentials")

    if not user.verify_password(password):
        return HTTPException(status_code=401, detail="Invalid credentials")

    new_token = str(uuid.uuid4())
    user_token = UserToken(token=new_token, user_id=user.id)

    db.add(user_token)
    db.commit()

    return {
        'token': new_token
    }


@app.post("/api/auth/logout", tags=['auth'])
def logout_user(token: str, db: Session = Depends(get_db)):
    token = db.query(UserToken).filter(UserToken.token == token).first()
    if not token:
        return HTTPException(status_code=401, detail="Invalid token")

    db.delete(token)
    db.commit()

    return {"message": "Token has been revoked"}



@app.get("/api/auth/active", tags=['users'])
def list_sessions(db: Session = Depends(get_db)):
    return {"tokens": []}


@app.get("/api/flag/read")
def read_flag(token: str, db: Session = Depends(get_db)):
    token = db.query(UserToken).filter(UserToken.token == token).first()

    if token is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    token_user = db.query(User).filter(User.id == token.user_id).first()
    if token_user is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    flag_string = 'flag{f1ag_f0r_t3st1ng}'

    flag_file = 'flag_user.txt'
    if token_user.username == 'admin':
        flag_file = 'flag_admin.txt'

    with open(f'/{flag_file}') as f:
        flag_string = f.read()

    return {"message": f"Token accepted, flag is: {flag_string}"}

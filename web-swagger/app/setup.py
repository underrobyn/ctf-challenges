from datetime import datetime, timedelta
from models import User, UserToken, SessionLocal
import string
import random
import uuid


ADMIN_USERNAME = 'admin'


def get_random_password(length: int = 16) -> str:
    allowed = string.ascii_letters + string.digits
    pwd = [random.choice(allowed) for i in range(0, length)]
    return ''.join(pwd)


def create_admin_user() -> None:
    db = SessionLocal()
    user = User(
        username=ADMIN_USERNAME,
        name='Mx Admin',
        email='appadmin@mail.internal.clam-corp.com'
    )
    password = get_random_password(24)
    print(password)
    user.set_password(password)
    db.add(user)
    db.commit()


def create_admin_token() -> None:
    db = SessionLocal()
    user = db.query(User).filter(User.username == ADMIN_USERNAME).first()
    new_token = str(uuid.uuid4())
    user_token = UserToken(
        token=new_token,
        user_id=user.id,
        expires_at=datetime.utcnow() + timedelta(minutes=1)
    )
    db.add(user_token)
    db.commit()


if __name__ == '__main__':
    create_admin_user()
    create_admin_token()

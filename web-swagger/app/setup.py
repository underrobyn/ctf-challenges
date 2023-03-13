from models import User, SessionLocal
import string
import random


def get_random_password(length: int = 16) -> str:
    allowed = string.ascii_letters + string.digits
    pwd = [random.choice(allowed) for i in range(0, length)]
    return ''.join(pwd)


def create_admin_user() -> None:
    db = SessionLocal()
    user = User(username='admin', name='Mx Admin', email='webmaster@localhost.localdomain')
    password = get_random_password(24)
    print(password)
    user.set_password(password)
    db.add(user)
    db.commit()


if __name__ == '__main__':
    create_admin_user()

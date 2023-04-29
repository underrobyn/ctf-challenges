from datetime import datetime, timedelta
from os import environ
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from passlib.context import CryptContext


SQLALCHEMY_DATABASE_URL = "sqlite:////tmp/app.db"
if 'DATABASE_URI' in environ:
    SQLALCHEMY_DATABASE_URL = environ['DATABASE_URI']

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
pwd_context = CryptContext(schemes=["argon2", "bcrypt"], deprecated="auto")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    tokens = relationship("UserToken", back_populates="user")

    def verify_password(self, password: str):
        return pwd_context.verify_and_update(password, self.hashed_password)

    def set_password(self, password: str):
        self.hashed_password = pwd_context.hash(password, scheme="argon2")


class UserToken(Base):
    __tablename__ = "user_tokens"

    id = Column(Integer, primary_key=True, index=True)
    token = Column(String, unique=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="tokens")
    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, default=datetime.utcnow() + timedelta(minutes=60))

    @property
    def is_expired(self):
        return datetime.utcnow() > self.expires_at


Base.metadata.create_all(bind=engine)

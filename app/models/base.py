from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, Mapped, mapped_column
from datetime import datetime
from sqlalchemy import Column, Integer, String, func, ForeignKey, DateTime
from flask_sqlalchemy import SQLAlchemy



class Base(DeclarativeBase):
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise
        
    def commit(self):
        try:
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise
        
    def add(self):
        try:
            db.session.add()
        except Exception:
            db.session.rollback()
            raise


db = SQLAlchemy(model_class=Base)

class TimestampModel(db.Model):
    __abstract__ = True
    time_created: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=func.now())
    time_updated: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), server_onupdate=func.now())
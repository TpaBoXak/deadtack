from app.models.base import db

from datetime import datetime
from sqlalchemy import Integer, String,  ForeignKey, DateTime, Numeric, text, Boolean, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Deadline(db.Model):
    __tablename__ = "deadlines"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    end_date: Mapped[datetime] = mapped_column(Date, nullable=False)
    priority: Mapped[int] = mapped_column(Integer, nullable=False)
    
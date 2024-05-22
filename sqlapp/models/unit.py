from sqlalchemy import Column, Integer, String

from .base import Base


class Unit(Base):
    __tablename__ = "unit"
    
    id = Column(Integer, primary_key=True)
    unit_name = Column(String(100), unique=True)
    short_name = Column(String(50), unique=True)

    def __repr__(self):
        return f"Unit(id={self.id}, Название_ЕИ: {self.unit_name}, Сокращение: {self.short_name})"
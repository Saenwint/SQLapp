from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class ProdClass(Base):
    __tablename__ = "prod_class"

    id = Column(Integer, primary_key=True)
    class_name = Column(String(100), unique=True)
    unit_id = Column(Integer, ForeignKey('unit.id'))
    parent_id = Column(Integer, ForeignKey('prod_class.id'))

    unit = relationship("Unit")
    children = relationship("ProdClass", back_populates="parent")
    parent = relationship("ProdClass", remote_side=[id], back_populates="children", uselist=False)

    def __repr__(self):
        return f"ProdClass(id={self.id}, Название_класса: {self.class_name}, id_ЕИ={self.unit_id}, id_Родителя={self.parent_id})"
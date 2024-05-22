from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base

class EnumClassifier(Base):
    __tablename__ = "enum_classifier"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey('enum_classifier.id'))
    unit_id = Column(Integer, ForeignKey('unit.id'))

    parent = relationship("EnumClassifier", remote_side=[id], back_populates="children", uselist=False)
    children = relationship("EnumClassifier", back_populates="parent")
    positions = relationship("EnumPosition", back_populates="classifier")
    unit = relationship("Unit")

    def __repr__(self):
        return f"EnumClassifier(id={self.id}, Название_перечисления: {self.name}, id_Родителя={self.parent_id})"
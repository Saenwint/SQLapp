from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Param(Base):
    __tablename__ = "param"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    short_name = Column(String(20))
    unit_id = Column(Integer, ForeignKey('unit.id'))
    enum_classifier_id = Column(Integer, ForeignKey('enum_classifier.id'))

    enum_classifier = relationship("EnumClassifier")
    unit = relationship("Unit")

    def __repr__(self):
        return f"Param(id={self.id}, Название_параметра: {self.name}, id_ЕИ={self.unit_id}, id_Перечисления={self.enum_classifier_id})"

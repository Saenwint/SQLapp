from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from .base import Base

class EnumPosition(Base):
    __tablename__ = "enum_position"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    short_name = Column(String)
    integer_value = Column(Integer)
    real_value = Column(Float)
    string_value = Column(String)
    classifier_id = Column(Integer, ForeignKey('enum_classifier.id'))
    
    classifier = relationship("EnumClassifier", back_populates="positions")

    def __repr__(self):
        integer_value_str = f", integer_value={self.integer_value}" if self.integer_value is not None else ""
        real_value_str = f", real_value={self.real_value}" if self.real_value is not None else ""
        string_value_str = f", string_value='{self.string_value}'" if self.string_value is not None else ""
    
        return f"EnumPosition(id={self.id}, Название_позиции: {self.name}, Сокращение: {self.short_name}{integer_value_str}{real_value_str}{string_value_str}, id_Перечисления={self.classifier_id})"

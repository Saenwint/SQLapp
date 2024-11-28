from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship

from .base import Base

class Product(Base):
    __tablename__ = "product"
    id_product = Column(Integer, primary_key=True)
    product_name = Column(String(150), unique=True)
    prod_class_id = Column(Integer, ForeignKey('prod_class.id'))
    enum_classifier_id = Column(Integer, ForeignKey('enum_classifier.id'))
    price = Column(Float)
    quantity = Column(Integer)
    is_base_specification = Column(Boolean, default=False)  # Базовая спецификация
    specification_version = Column(Integer, default=1)  # Версия спецификации

    prod_class = relationship("ProdClass")
    enum_classifier = relationship("EnumClassifier")

    def __repr__(self):
        return f"Product(id={self.id_product}, Название_продукта: {self.product_name}, id_Класса={self.prod_class_id}, id_Перечисления={self.enum_classifier_id}, Стоимость={self.price}, Количество={self.quantity}, Базовая_спецификация={self.is_base_specification}, Версия_спецификации={self.specification_version})"
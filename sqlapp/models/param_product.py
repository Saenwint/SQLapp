from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from .base import Base

class ParamProduct(Base):
    __tablename__ = "param_product"

    id = Column(Integer, primary_key=True)
    value = Column(Integer)
    product_id = Column(Integer, ForeignKey('product.id_product'))
    param_class_id = Column(Integer, ForeignKey('param_class.id'))

    product = relationship("Product")
    param_class = relationship("ParamClass")    


    def __repr__(self):
        return f"ProductParam(id={self.id}, id_Продукта={self.product_id}, id_Параметра_Класса={self.param_class_id}, Значение={self.value})"

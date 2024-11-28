from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base

class SpecificationLine(Base):
    __tablename__ = "specification_line"
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id_product'))
    component_id = Column(Integer, ForeignKey('product.id_product'))
    quantity = Column(Float)  # Норма расхода

    product = relationship("Product", foreign_keys=[product_id])
    component = relationship("Product", foreign_keys=[component_id])

    def __repr__(self):
        return f"SpecificationLine(id={self.id}, Продукт_ID={self.product_id}, Компонент_ID={self.component_id}, Количество={self.quantity})"